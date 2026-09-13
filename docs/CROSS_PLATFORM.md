# กติกาการเขียนให้ใช้ได้ข้ามแพลตฟอร์ม (Claude / Codex / Gemini CLI)

> เอกสารนี้ตอบคำถาม "ทำไม SKILL.md ตัวหนึ่งใช้กับ Claude ได้ แต่พังเวลาเอาไปใช้กับ Codex หรือ Gemini"
> และวางกฎให้คนเขียน skill ใหม่ในคลังนี้ทำตาม เพื่อไม่ให้หลุดปัญหาซ้ำ

## 1. ข้อเท็จจริงที่ตรวจสอบแล้ว (ไม่ใช่การเดา)

ตรวจสอบเอกสารทางการของทั้งสามฝั่งแล้วพบว่า **รูปแบบไฟล์พื้นฐานไม่ใช่ปัญหา** — ทั้งสามแพลตฟอร์มอ่านโครงสร้างเดียวกัน:

- โฟลเดอร์ 1 อัน = 1 skill, ข้างในมี `SKILL.md` ที่มี YAML frontmatter (`name` + `description`) แล้วตามด้วยเนื้อหา Markdown
- ไม่มีแพลตฟอร์มไหน **บังคับ** ต้องมี manifest เพิ่มถึงจะทำงานได้:
  - **Claude** อ่าน `SKILL.md` ตรง ๆ
  - **OpenAI Codex** สแกนหาจาก `.agents/skills` (ใน repo, `$HOME/.agents/skills`, `/etc/codex/skills`) — ต้องการแค่ `name` + `description` ใน frontmatter เท่านั้น ส่วน `agents/openai.yaml` เป็นแค่ตัวเสริม metadata สำหรับ UI ไม่ใช่ของบังคับ
  - **Gemini CLI** สแกน `~/.gemini/skills/` หรือ `~/.agents/skills/` (user) และ `.gemini/skills/` หรือ `.agents/skills/` (workspace) — ไม่ต้องมี manifest เลยสำหรับ skill ธรรมดา ส่วน `gemini-extension.json` ใช้เฉพาะตอนทำ "extension" เต็มรูปแบบที่ผูก MCP server เท่านั้น
- Codex กับ Gemini CLI ใช้ path convention เดียวกันคือ `.agents/skills` ทำให้ก็อปโฟลเดอร์เดียวไปวางได้ทั้งสองฝั่ง
- ⚠️ Gemini CLI (และเครื่องมืออีกหลายตัว เช่น OpenHands) มองหา skill แค่ **ชั้นเดียว** (`.agents/skills/<skill>/SKILL.md`) ส่วนคลังนี้เก็บแยกหมวด 2 ชั้น จึงควรก๊อปด้วย `scripts/install.py` หรือ `npx skills add` ไม่ใช่วางทั้ง repo

**สรุป:** ไฟล์ `SKILL.md` ไฟล์เดียวที่เขียนถูกฟอร์แมต ใช้ได้ทั้ง 3 แพลตฟอร์มโดยไม่ต้องสร้างไฟล์แยกต่างหาก — ไม่จำเป็นต้องมี "เวอร์ชัน Claude" กับ "เวอร์ชัน Gemini" คนละไฟล์

## 2. แล้วอะไรทำให้ skill ใช้ข้ามแพลตฟอร์มไม่ได้จริง ๆ

ปัญหาตัวจริงไม่ใช่ฟอร์แมตไฟล์ แต่คือ **เนื้อหาข้างในที่อ้างอิงเฉพาะ Claude**:

### 2.1 ชื่อ tool เฉพาะของ Claude (ห้ามเด็ดขาด — เป็น error)

Codex กับ Gemini CLI ไม่มี tool ที่ชื่อพวกนี้ ถ้า skill สั่งว่า "ใช้ Bash tool รัน..." หรือ "เรียก SendUserFile ส่งไฟล์" แล้วเอาไปรันบน Codex/Gemini มันจะงงว่า tool นี้คืออะไร ตัวอย่างคำที่ห้ามเขียนใน body ของ SKILL.md:

- `Bash tool`, `Read tool`, `Write tool`, `Edit tool`, `Grep tool`, `Glob tool`
- `SendUserFile`, `Artifact tool`
- `AskUserQuestion`, `TaskCreate`, `TaskUpdate`
- `WebSearch tool`, `WebFetch tool`
- `ExitPlanMode`, `ReadNotifications`

**ให้เขียนยังไงแทน:** พูดถึง "การกระทำ" ไม่ใช่ "ชื่อ tool" — เช่นแทนที่จะเขียนว่า "ใช้ Bash tool รันคำสั่งนี้" ให้เขียนว่า "รันคำสั่งนี้ในเทอร์มินัล" หรือ "ให้ผู้ช่วย AI อ่านไฟล์นี้" แทน "ใช้ Read tool เปิดไฟล์" — ผลลัพธ์เหมือนกัน แต่ไม่ผูกกับชื่อ tool ของแพลตฟอร์มใดแพลตฟอร์มหนึ่ง

### 2.2 ชื่อผลิตภัณฑ์เฉพาะ Claude (ระวัง — เป็น warning)

คำพวกนี้ไม่ผิดเสมอไป (บางที skill อาจตั้งใจพูดถึง Claude Code จริง ๆ) แต่ถ้าเจอในคลังนี้ควรเช็คอีกทีว่าจำเป็นต้องเจาะจงแพลตฟอร์มไหม: `Claude Code`, `Cowork`, `Claude in Chrome`, ลิงก์ `claude.ai`

### 2.3 สคริปต์ที่พึ่งของเฉพาะ Claude

ถ้า skill มี `scripts/` แนบมาด้วย ให้เขียนด้วย runtime ที่มีทุกที่ (เช่น `python3` standard library, bash ธรรมดา) หลีกเลี่ยง library ที่ต้อง pip install แพ็กเกจแปลก ๆ ที่หาไม่ได้ในเครื่อง user ทั่วไป เพราะ skill อาจถูกรันในเครื่อง/สภาพแวดล้อมที่ไม่มีเน็ตหรือ pip ใช้ไม่ได้

## 3. สิ่งที่ทำเพิ่มได้โดยไม่กระทบความเข้ากันได้

ไฟล์เสริมเฉพาะแพลตฟอร์มไม่ใช่ปัญหา ตราบใดที่ `SKILL.md` หลักยังพอร์ตได้ — แพลตฟอร์มอื่นจะมองข้ามไฟล์ที่ไม่รู้จักไปเฉย ๆ ตัวอย่างเช่น:

- `agents/openai.yaml` — ไฟล์เสริมของ Codex (optional) ใช้กำหนดชื่อ/ไอคอนที่แสดงใน UI, นโยบายการเรียกใช้ (`allow_implicit_invocation`) และ dependency เช่น MCP ([เอกสาร](https://learn.chatgpt.com/docs/build-skills))
- `gemini-extension.json` — ใช้เมื่ออยาก bundle เป็น Gemini extension เต็มรูปแบบ ซึ่งรวม skill, คำสั่ง, hook, theme, context หรือ MCP server ไว้ด้วยกันได้ (optional — skill ธรรมดาไม่ต้องใช้)
- โฟลเดอร์ `adapters/` แยกต่างหากสำหรับไฟล์เฉพาะแพลตฟอร์ม — ตัวอย่างแนวคิดนี้อยู่ใน repo [`theeranon/JamesSkills`](https://github.com/theeranon/JamesSkills) ซึ่งกันโฟลเดอร์ `adapters/` ไว้ "สำหรับ manifest ที่ gen ขึ้นหรือไฟล์เฉพาะ vendor และห้ามซ้ำกับเนื้อหาคำสั่งของ skill" (ตอนนี้ยังมีแค่ README อธิบายกติกา ยังไม่มีไฟล์ adapter จริง)

กติกาของคลังนี้: **ถ้าจะเพิ่มไฟล์เสริมเฉพาะแพลตฟอร์ม ให้แยกเป็นไฟล์/โฟลเดอร์ต่างหาก อย่าฝังไว้ใน `SKILL.md` หลัก**

## 4. เช็คอัตโนมัติ

`scripts/validate.py` สแกนคำต้องห้ามในข้อ 2.1 และ 2.2 ให้อัตโนมัติทุกครั้งที่รัน:

```
python3 scripts/validate.py
```

- เจอคำในกลุ่ม 2.1 (ชื่อ tool เฉพาะ Claude) → ขึ้น **error** ต้องแก้ก่อน merge
- เจอคำในกลุ่ม 2.2 (ชื่อผลิตภัณฑ์เฉพาะ Claude) → ขึ้น **warning** ให้ทบทวนว่าตั้งใจหรือเผลอ

ก่อนส่ง PR skill ใหม่ ให้รันเช็คนี้ผ่านก่อนเสมอ (ดูขั้นตอนเต็มใน [`README.md`](../README.md) หัวข้อ "อยากช่วยเพิ่ม Skill ใหม่?")

## 5. เข้ากันได้กับเครื่องมืออื่นอีกกี่ตัว?

นอกจาก Claude, Codex, Gemini CLI แล้ว ยังมีเครื่องมือ AI coding agent อีกจำนวนมากที่อ่านโครงสร้าง
`SKILL.md` แบบเดียวกันได้ — ดูผลตรวจสอบละเอียดอีก 44 เครื่องมือ (ChatGPT/Codex, GitHub Copilot, VS Code,
Cursor, Junie, Kiro, Goose, Amp, OpenHands ฯลฯ) พร้อม path ที่แต่ละตัวอ่านได้ที่
[`docs/TOOL_COMPATIBILITY.md`](TOOL_COMPATIBILITY.md) — สรุปสั้นๆ คือหลายเครื่องมือบรรจบกันที่โฟลเดอร์
`.agents/skills/<skill-name>/SKILL.md` ทำให้วาง skill ไว้ตรงนั้นที่เดียว ใช้ได้กับเครื่องมือส่วนใหญ่เลย

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill)*
