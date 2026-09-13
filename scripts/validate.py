#!/usr/bin/env python3
"""Validate every SKILL.md in skills/ against the Insightist Skills Library rules.

Checks:
  - SKILL.md exists in each skill folder
  - YAML frontmatter has `name` and `description`
  - `name` matches the folder name
  - description is non-trivial length (helps triggering)
  - body line count <= 350 (hard cap) and warns if > 220 (soft target)
  - the closing Insightist credit line is present
  - a bilingual README.md exists next to SKILL.md and names the right Skill ID
  - no references to Claude-specific tool names or product names
    (cross-platform portability — see docs/CROSS_PLATFORM.md)

Usage: python3 scripts/validate.py
Exit code 0 = all good, 1 = at least one error.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
HARD_LINE_CAP = 350
SOFT_LINE_TARGET = 220
MIN_DESCRIPTION_CHARS = 40
MAX_DESCRIPTION_CHARS = 1024  # agentskills.io spec; most tools skip longer skills
MAX_NAME_CHARS = 64
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CREDIT_MARKER = "Insightist"

# Claude-specific tool names — never portable to Codex/Gemini CLI, hard error.
# See docs/CROSS_PLATFORM.md section 2.1.
FORBIDDEN_TOOL_TERMS = [
    "Bash tool",
    "Read tool",
    "Write tool",
    "Edit tool",
    "Grep tool",
    "Glob tool",
    "SendUserFile",
    "Artifact tool",
    "AskUserQuestion",
    "TaskCreate",
    "TaskUpdate",
    "WebSearch tool",
    "WebFetch tool",
    "ExitPlanMode",
    "ReadNotifications",
]

# Claude-specific product names — not always wrong, but worth a second look.
# See docs/CROSS_PLATFORM.md section 2.2.
RISKY_PLATFORM_TERMS = [
    "Claude Code",
    "Cowork",
    "Claude in Chrome",
    "claude.ai",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    data = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            data[key.strip()] = val.strip()
    return data


def main() -> int:
    errors = []
    warnings = []
    checked = 0

    if not SKILLS_DIR.is_dir():
        print(f"ERROR: {SKILLS_DIR} not found")
        return 1

    for category_dir in sorted(SKILLS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            checked += 1
            prefix = f"[{category_dir.name}/{skill_dir.name}]"

            if not skill_md.exists():
                errors.append(f"{prefix} missing SKILL.md")
                continue

            text = skill_md.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if fm is None:
                errors.append(f"{prefix} no YAML frontmatter found")
                continue

            name = fm.get("name", "")
            description = fm.get("description", "")

            if not name:
                errors.append(f"{prefix} frontmatter missing `name`")
            elif name != skill_dir.name:
                errors.append(
                    f"{prefix} name in frontmatter ('{name}') != folder name ('{skill_dir.name}')"
                )

            if name and (len(name) > MAX_NAME_CHARS or not NAME_RE.match(name)):
                errors.append(
                    f"{prefix} name must be lowercase letters/digits/single hyphens, <= {MAX_NAME_CHARS} chars"
                )

            if len(description) > MAX_DESCRIPTION_CHARS:
                errors.append(
                    f"{prefix} description is {len(description)} chars; the Agent Skills spec allows {MAX_DESCRIPTION_CHARS}"
                )

            if not description:
                errors.append(f"{prefix} frontmatter missing `description`")
            elif len(description) < MIN_DESCRIPTION_CHARS:
                warnings.append(
                    f"{prefix} description looks short ({len(description)} chars) — may under-trigger"
                )

            line_count = len(text.splitlines())
            if line_count > HARD_LINE_CAP:
                errors.append(f"{prefix} {line_count} lines exceeds hard cap of {HARD_LINE_CAP}")
            elif line_count > SOFT_LINE_TARGET:
                warnings.append(f"{prefix} {line_count} lines exceeds soft target of {SOFT_LINE_TARGET}")

            if CREDIT_MARKER not in text:
                warnings.append(f"{prefix} missing '{CREDIT_MARKER}' credit line")

            readme = skill_dir / "README.md"
            if not readme.exists():
                errors.append(f"{prefix} missing README.md (bilingual Thai/English description)")
            else:
                readme_text = readme.read_text(encoding="utf-8")
                if f"`{skill_dir.name}`" not in readme_text:
                    errors.append(f"{prefix} README.md does not mention Skill ID `{skill_dir.name}`")
                for anchor in ('<a id="th"></a>', '<a id="en"></a>'):
                    if anchor not in readme_text:
                        warnings.append(f"{prefix} README.md missing {anchor} section")

            for term in FORBIDDEN_TOOL_TERMS:
                if term.lower() in text.lower():
                    errors.append(
                        f"{prefix} references Claude-specific tool name '{term}' — "
                        f"breaks Codex/Gemini CLI portability (see docs/CROSS_PLATFORM.md)"
                    )

            for term in RISKY_PLATFORM_TERMS:
                if term.lower() in text.lower():
                    warnings.append(
                        f"{prefix} mentions Claude-specific product '{term}' — "
                        f"confirm this is intentional (see docs/CROSS_PLATFORM.md)"
                    )

    print(f"Checked {checked} skills.")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  ! {w}")
    if errors:
        print(f"\n{len(errors)} error(s):")
        for e in errors:
            print(f"  x {e}")
        return 1

    print("\nAll skills passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
