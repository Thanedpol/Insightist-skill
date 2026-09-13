# Insightist Skills Library

**Skills for use through Claude, Codex, Gemini and other agents that support the `SKILL.md` standard.**
คลังรวม "Skills" ข้ามแพลตฟอร์ม ครอบคลุมงานความรู้ (knowledge work) หลากสายอาชีพ
เขียนโดยทีม **Insightist™**

> 🇹🇭 เอกสารนี้เขียนเป็นภาษาไทยเป็นหลัก / 🇬🇧 English summary below each section.

---

## นี่คืออะไร (What is this)

`SKILL.md` คือฟอร์แมตมาตรฐานที่ Anthropic เริ่มต้นไว้สำหรับ Claude แต่ตอนนี้กลายเป็นมาตรฐานกลาง
ที่ Claude Code, Claude Cowork, OpenAI Codex, Gemini CLI, Cursor และ agent อื่น ๆ อ่านได้เหมือนกัน
— skill 1 ตัวคือโฟลเดอร์ที่มีไฟล์ `SKILL.md` (คำสั่ง/ขั้นตอนการทำงาน) บวกไฟล์เสริม (ตัวอย่าง, สคริปต์)
ที่ทำให้ agent ทำงานเฉพาะทางได้ดีขึ้นและ trigger ถูกจังหวะ

โปรเจกต์นี้เป็นเฟส **Framework + Taxonomy + Pilot**: วางโครงหมวดหมู่ให้ครอบคลุมทุกสายอาชีพในระยะยาว
แล้วเริ่มสร้าง skill คุณภาพสูงจริง 24 ตัว ใน 8 หมวดตั้งต้น ก่อนขยายต่อ (ดู [`docs/TAXONOMY.md`](docs/TAXONOMY.md)
สำหรับ roadmap เต็ม)

*`SKILL.md` is Anthropic's original format for Claude, now a cross-agent standard also read by
Codex, Gemini CLI, Cursor, and more. This repo is a Framework + Taxonomy + Pilot phase: 24 real,
usable skills across 8 categories, with a documented roadmap to expand toward full occupational
coverage.*

## หมวดหมู่ & Skills (24 ตัว ใน 8 หมวด)

| หมวด | Skills |
|---|---|
| 💼 **กลยุทธ์ / บริหารธุรกิจ**<br>`business-strategy` | `business-model-canvas-builder` · `swot-competitive-analysis` · `okr-goal-setter` |
| 💰 **การเงิน / บัญชี**<br>`finance-accounting` | `financial-ratio-analyzer` · `budget-variance-report` · `invoice-expense-tracker` |
| 📢 **การตลาด / งานขาย**<br>`marketing-sales` | `sales-proposal-writer` · `customer-persona-builder` · `social-content-planner` |
| 👥 **งานบุคคล / HR**<br>`hr-people-ops` | `job-description-writer` · `interview-scorecard-builder` · `onboarding-plan-generator` |
| ⚖️ **กฎหมาย / Compliance**<br>`legal-compliance` | `contract-clause-reviewer` · `nda-drafting-assistant` · `policy-compliance-checklist` |
| 💻 **เทคโนโลยี / ข้อมูล**<br>`technology-data` | `code-review-checklist` · `data-cleaning-playbook` · `api-doc-writer` |
| 🏭 **ปฏิบัติการ / โลจิสติกส์**<br>`operations-supply-chain` | `inventory-reorder-planner` · `process-sop-writer` · `vendor-comparison-matrix` |
| 🎓 **การศึกษา / ฝึกอบรม**<br>`education-training` | `lesson-plan-builder` · `training-needs-assessment` · `quiz-generator` |

ดูรายละเอียดแต่ละ skill ได้ใน `catalog.json` หรือเปิดไฟล์ `skills/<category>/<skill-name>/SKILL.md` ตรงๆ

## วิธีติดตั้ง / ใช้งาน แยกตามแพลตฟอร์ม

### Claude.ai (Chat / Cowork) — อัปโหลด `.zip`
1. ไปที่ `dist/<skill-name>.zip` (มี zip ให้ครบทุก skill แล้ว)
2. ในหน้า Skills settings ของ Claude.ai → Upload skill → เลือกไฟล์ `.zip` นั้น

### Claude Code / Claude Cowork — ติดตั้งทั้ง marketplace ทีเดียว
```
/plugin marketplace add Thanedpol/Insightist-skill
/plugin install <skill-name>@insightist-skills
```
(ใช้ `.claude-plugin/marketplace.json` ที่มีอยู่แล้วในรีโปนี้)

หรือจะคัดลอกเฉพาะโฟลเดอร์ที่ต้องการไปไว้ใน `~/.claude/skills/` ก็ได้เช่นกัน

### OpenAI Codex
- วางโฟลเดอร์ skill (เช่น `skills/finance-accounting/financial-ratio-analyzer/`) ไว้ใน
  โฟลเดอร์ skills ของ Codex ตามคู่มือ `developers.openai.com/codex/skills`
- หรือใช้ `codex-marketplace add Thanedpol/Insightist-skill` ถ้าเชื่อมกับ Codex Marketplace

### Gemini CLI
- Gemini CLI อ่าน `SKILL.md` ได้โดยตรง (มาตรฐานเดียวกัน) — คัดลอกโฟลเดอร์ skill ไปยัง
  extension/skills directory ของ Gemini CLI ตามคู่มือ `geminicli.com/docs/cli/skills`

### แบบ copy-paste (ไม่ใช้เครื่องมือติดตั้งใดๆ)
เปิดไฟล์ `SKILL.md` ที่ต้องการ คัดลอกทั้งไฟล์ไปวางเป็น custom instruction / system prompt ได้ตรงๆ
เพราะแต่ละ skill ออกแบบให้เป็น self-contained อยู่แล้ว

## โครงสร้างรีโป

```
├── README.md
├── LICENSE
├── catalog.json                 # index รวมทุก skill (สร้างอัตโนมัติจาก scripts/build.py)
├── .claude-plugin/
│   └── marketplace.json         # ให้ติดตั้งผ่าน /plugin marketplace add ได้
├── docs/
│   └── TAXONOMY.md              # roadmap หมวด/อาชีพที่จะขยายต่อ
├── skills/
│   └── <category>/<skill-name>/SKILL.md
├── dist/
│   └── <skill-name>.zip         # แพ็กเกจติดตั้งต่อ 1 skill
└── scripts/
    ├── build.py                 # regenerate catalog.json + marketplace.json + zip ทุก skill
    └── validate.py              # เช็คว่าทุก SKILL.md ถูกต้องตามกติกา
```

## สร้าง / แก้ไข skill ใหม่

1. ทำตามรูปแบบ `skills/<category>/<skill-name>/SKILL.md` ของ skill ที่มีอยู่แล้ว —
   ต้องมี YAML frontmatter (`name`, `description`), ส่วน "เมื่อไหร่ควรใช้", "ขั้นตอนการทำงาน",
   "โครงสร้าง Output", "ตัวอย่าง", "เกณฑ์คุณภาพ" และปิดท้ายด้วยเครดิต Insightist™
2. รันตรวจสอบ:
   ```
   python3 scripts/validate.py
   ```
3. สร้าง catalog + marketplace manifest + zip ใหม่ทั้งหมด:
   ```
   python3 scripts/build.py
   ```
4. ดู [`docs/TAXONOMY.md`](docs/TAXONOMY.md) สำหรับหมวดที่ยังไม่ได้ทำ และแนวทางขยายต่อ

## เครดิต

สร้างและดูแลโดยทีม **Insightist™** — เปิดเป็น public library ให้ใครก็ใช้ได้ฟรีตาม [MIT License](LICENSE)

*Maintained by the Insightist™ team — released as a free, open public library under the MIT License.*
