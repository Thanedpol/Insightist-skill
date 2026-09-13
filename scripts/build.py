#!/usr/bin/env python3
"""Regenerate every derived file from the contents of skills/.

Usage: python3 scripts/build.py          # rebuild everything
       python3 scripts/build.py --check  # exit 1 if anything is out of date (for CI)

Outputs:
  - catalog.json                       index of every skill
  - .claude-plugin/marketplace.json    Claude Code plugin marketplace
  - AGENTS.md                          skill index for agents that read AGENTS.md but not SKILL.md
  - README.md                          the auto-generated blocks between <!-- AUTO:... --> markers
  - dist/<skill-name>.zip              one installable package per skill

The zips are deterministic (fixed timestamps, LF line endings), so running this on
Windows, macOS or in CI produces byte-identical files and no spurious diffs.
"""
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
CATALOG_PATH = ROOT / "catalog.json"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
AGENTS_MD_PATH = ROOT / "AGENTS.md"
README_PATH = ROOT / "README.md"
REPO_URL = "https://github.com/Thanedpol/Insightist-skill"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TAGLINE_RE = re.compile(r"^\*\*(.+?)\*\*\s*$", re.MULTILINE)
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".py", ".sh"}
ZIP_DATE = (1980, 1, 1, 0, 0, 0)

# Display order follows ISCO-08 major group codes 1..9, then 0.
CATEGORY_LABELS = {
    "managers": "1 · ผู้จัดการ (Managers)",
    "professionals": "2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals)",
    "technicians-associate-professionals": "3 · เจ้าหน้าที่เทคนิคและผู้ประกอบวิชาชีพที่เกี่ยวข้อง (Technicians and Associate Professionals)",
    "clerical-support-workers": "4 · เสมียน / งานธุรการสนับสนุน (Clerical Support Workers)",
    "service-sales-workers": "5 · พนักงานบริการและผู้จำหน่ายสินค้า (Service and Sales Workers)",
    "skilled-agricultural-forestry-fishery-workers": "6 · ผู้ปฏิบัติงานที่มีฝีมือด้านการเกษตร ป่าไม้ และประมง (Skilled Agricultural, Forestry and Fishery Workers)",
    "craft-related-trades-workers": "7 · ช่างฝีมือและผู้ปฏิบัติงานที่เกี่ยวข้อง (Craft and Related Trades Workers)",
    "plant-machine-operators-assemblers": "8 · ผู้ควบคุมเครื่องจักรโรงงานและผู้ประกอบชิ้นงาน (Plant and Machine Operators, and Assemblers)",
    "elementary-occupations": "9 · ผู้ประกอบอาชีพงานพื้นฐาน (Elementary Occupations)",
    "armed-forces-occupations": "0 · ทหาร (Armed Forces Occupations)",
}


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            data[key.strip()] = val.strip()
    return data


def category_order(name: str) -> int:
    keys = list(CATEGORY_LABELS)
    return keys.index(name) if name in keys else len(keys)


def discover_skills() -> list:
    """Return one dict per skill folder, in ISCO display order."""
    skills = []
    if not SKILLS_DIR.is_dir():
        return skills
    categories = sorted(
        (d for d in SKILLS_DIR.iterdir() if d.is_dir()),
        key=lambda d: (category_order(d.name), d.name),
    )
    for category_dir in categories:
        for skill_dir in sorted(d for d in category_dir.iterdir() if d.is_dir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
            readme = skill_dir / "README.md"
            tagline = ""
            if readme.exists():
                m = TAGLINE_RE.search(readme.read_text(encoding="utf-8"))
                tagline = m.group(1).strip() if m else ""
            skills.append(
                {
                    "dir": skill_dir,
                    "id": skill_dir.name,
                    "name": fm.get("name", skill_dir.name),
                    "description": fm.get("description", ""),
                    "tagline": tagline,
                    "category": category_dir.name,
                    "category_label": CATEGORY_LABELS.get(category_dir.name, category_dir.name),
                    "rel": f"skills/{category_dir.name}/{skill_dir.name}",
                    "has_readme": readme.exists(),
                }
            )
    return skills


def short_description(skill: dict) -> str:
    """Tagline from the skill README, else the description up to its trigger phrases."""
    if skill["tagline"]:
        return skill["tagline"]
    desc = skill["description"]
    m = re.search(r"\s(ใช้เมื่อ|ใช้ skill นี้|ใช้ทุกครั้ง|Use when)", desc)
    if m:
        desc = desc[: m.start()]
    return desc.strip()


# ---------------------------------------------------------------- renderers

def render_zip(skill_dir: Path) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(p for p in skill_dir.rglob("*") if p.is_file()):
            data = path.read_bytes()
            if path.suffix.lower() in TEXT_SUFFIXES:
                data = data.replace(b"\r\n", b"\n")
            # keep the top-level folder name inside the zip (skill-creator convention)
            arcname = (Path(skill_dir.name) / path.relative_to(skill_dir)).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, data)
    return buf.getvalue()


def render_catalog(skills: list) -> str:
    entries = [
        {
            "id": s["id"],
            "name": s["name"],
            "description": s["description"],
            "category": s["category"],
            "category_label": s["category_label"],
            "path": f"{s['rel']}/SKILL.md",
            "readme": f"{s['rel']}/README.md" if s["has_readme"] else None,
            "zip": f"dist/{s['id']}.zip",
        }
        for s in skills
    ]
    doc = {
        "name": "Insightist Skills Library",
        "credit": "Insightist™",
        "source": REPO_URL,
        "count": len(entries),
        "skills": entries,
    }
    return json.dumps(doc, ensure_ascii=False, indent=2) + "\n"


def render_marketplace(skills: list) -> str:
    marketplace = {
        "name": "insightist-skills",
        "owner": {"name": "Insightist", "url": "https://github.com/Thanedpol"},
        "plugins": [
            {
                "name": s["id"],
                "source": f"./{s['rel']}",
                "description": s["description"],
            }
            for s in skills
        ],
    }
    return json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n"


def render_agents_md(skills: list, path_prefix: str = "", source_note: str = "") -> str:
    """Skill index in AGENTS.md form. path_prefix is prepended to each skill's folder path."""
    lines = [
        "# Insightist™ Skills — AGENTS.md",
        "",
        "<!-- Generated by scripts/build.py (or scripts/install.py --agents-md). Do not edit by hand. -->",
        "",
        "This file lists the Insightist™ Agent Skills available in this project.",
        "",
        "**Instructions for the AI agent:**",
        "",
        "1. When the user's request matches one of the skills below, open that skill's `SKILL.md` "
        "and follow it exactly before answering.",
        "2. Read only the skill you need. Do not load every skill up front.",
        "3. If no skill matches, answer normally.",
        "",
    ]
    if source_note:
        lines += [source_note, ""]
    lines += [f"Total: {len(skills)} skills.", ""]
    current, current_is_first = None, True
    for s in skills:
        if s["category"] != current:
            current = s["category"]
            lines += [f"## {s['category_label']}", ""] if current_is_first else ["", f"## {s['category_label']}", ""]
            current_is_first = False
        folder = f"{path_prefix}{s['id']}" if path_prefix else s["rel"]
        lines.append(f"- `{folder}/SKILL.md` — **{s['id']}**: {short_description(s)}")
    lines += [
        "",
        "---",
        "",
        f"*Insightist™ Skills Library — {REPO_URL}*",
        "",
    ]
    return "\n".join(lines)


def render_readme_blocks(text: str, skills: list) -> str:
    numbered = sum(1 for s in skills if re.match(r"\d\d-", s["id"]))
    legacy = len(skills) - numbered
    count_block = (
        f"รวม **{len(skills)} skills** ({numbered} skill ตามหมวดย่อย ISCO-08 "
        f"+ {legacy} skill เฉพาะงานจากเวอร์ชันแรก)"
    )
    table = [
        f"## {len(skills)} Skills ที่ใช้ได้วันนี้ (10 หมวดใหญ่ ISCO-08)",
        "",
        "กดชื่อ skill เพื่ออ่านคำอธิบายภาษาไทย/อังกฤษของแต่ละตัว",
        "",
        "| หมวดใหญ่ | Skills |",
        "|---|---|",
    ]
    by_cat = {}
    for s in skills:
        by_cat.setdefault(s["category"], []).append(s)
    for cat, items in by_cat.items():
        links = " · ".join(
            f"[`{s['id']}`]({s['rel']}/{'README.md' if s['has_readme'] else 'SKILL.md'})"
            for s in items
        )
        table.append(f"| {CATEGORY_LABELS.get(cat, cat)} · {len(items)} skills | {links} |")
    blocks = {"COUNT": count_block, "SKILLS": "\n".join(table)}
    for key, body in blocks.items():
        pattern = re.compile(
            rf"(<!-- AUTO:{key} -->)(.*?)(<!-- /AUTO:{key} -->)", re.DOTALL
        )
        if not pattern.search(text):
            print(f"warning: README.md has no <!-- AUTO:{key} --> block", file=sys.stderr)
            continue
        sep = "\n" if key == "SKILLS" else ""
        text = pattern.sub(lambda m: f"{m.group(1)}{sep}{body}{sep}{m.group(3)}", text)
    return text


# ---------------------------------------------------------------- main

def use_utf8_console() -> None:
    # Windows consoles default to a legacy code page and crash on Thai text.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    use_utf8_console()
    check = "--check" in sys.argv[1:]
    skills = discover_skills()

    outputs = {
        CATALOG_PATH: render_catalog(skills).encode("utf-8"),
        MARKETPLACE_PATH: render_marketplace(skills).encode("utf-8"),
        AGENTS_MD_PATH: render_agents_md(skills).encode("utf-8"),
    }
    if README_PATH.exists():
        readme = README_PATH.read_text(encoding="utf-8").replace("\r\n", "\n")
        outputs[README_PATH] = render_readme_blocks(readme, skills).encode("utf-8")
    for s in skills:
        outputs[DIST_DIR / f"{s['id']}.zip"] = render_zip(s["dir"])

    expected_zips = {DIST_DIR / f"{s['id']}.zip" for s in skills}
    stale_zips = [p for p in DIST_DIR.glob("*.zip") if p not in expected_zips] if DIST_DIR.is_dir() else []

    changed = []
    for path, data in outputs.items():
        current = path.read_bytes() if path.exists() else None
        if path.suffix in {".md", ".json"} and current is not None:
            current = current.replace(b"\r\n", b"\n")
        if current != data:
            changed.append(path)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if not check:
        for p in stale_zips:
            p.unlink()

    rel = lambda p: p.relative_to(ROOT).as_posix()
    if check:
        if changed or stale_zips:
            print("Out of date — run `python3 scripts/build.py`:")
            for p in changed:
                print(f"  ~ {rel(p)}")
            for p in stale_zips:
                print(f"  - {rel(p)} (no matching skill)")
            return 1
        print(f"All generated files are up to date ({len(skills)} skills).")
        return 0

    print(f"Built {len(skills)} skills: {len(changed)} file(s) updated, {len(stale_zips)} stale zip(s) removed.")
    for p in changed:
        print(f"  ~ {rel(p)}")
    for p in stale_zips:
        print(f"  - {rel(p)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
