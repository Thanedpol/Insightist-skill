#!/usr/bin/env python3
"""Build catalog.json, .claude-plugin/marketplace.json, and per-skill .zip packages
from the contents of skills/.

Usage: python3 scripts/build.py
Outputs:
  - catalog.json                       (root)
  - .claude-plugin/marketplace.json    (root)
  - dist/<skill-name>.zip              (one per skill)
"""
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
CATALOG_PATH = ROOT / "catalog.json"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

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


def parse_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            data[key.strip()] = val.strip()
    return data


def zip_skill(skill_dir: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                # keep the top-level folder name inside the zip (skill-creator convention)
                arcname = Path(skill_dir.name) / path.relative_to(skill_dir)
                zf.write(path, arcname)


def main() -> None:
    entries = []

    for category_dir in sorted(SKILLS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        category = category_dir.name
        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))

            zip_path = DIST_DIR / f"{skill_dir.name}.zip"
            zip_skill(skill_dir, zip_path)

            entries.append(
                {
                    "id": skill_dir.name,
                    "name": fm.get("name", skill_dir.name),
                    "description": fm.get("description", ""),
                    "category": category,
                    "category_label": CATEGORY_LABELS.get(category, category),
                    "path": f"skills/{category}/{skill_dir.name}/SKILL.md",
                    "zip": f"dist/{skill_dir.name}.zip",
                }
            )

    CATALOG_PATH.write_text(
        json.dumps(
            {
                "name": "Insightist Skills Library",
                "credit": "Insightist™",
                "source": "https://github.com/Thanedpol/Insightist-skill",
                "count": len(entries),
                "skills": entries,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    marketplace = {
        "name": "insightist-skills",
        "owner": {"name": "Insightist", "url": "https://github.com/Thanedpol"},
        "plugins": [
            {
                "name": e["id"],
                "source": f"./skills/{e['category']}/{e['id']}",
                "description": e["description"],
            }
            for e in entries
        ],
    }
    MARKETPLACE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MARKETPLACE_PATH.write_text(
        json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Built catalog.json with {len(entries)} skills.")
    print(f"Built {MARKETPLACE_PATH.relative_to(ROOT)}.")
    print(f"Built {len(entries)} zip packages under dist/.")


if __name__ == "__main__":
    main()
