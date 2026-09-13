# ความเข้ากันได้กับเครื่องมือ AI Agent อื่นๆ (44 ตัว)

> ต่อยอดจาก [`CROSS_PLATFORM.md`](CROSS_PLATFORM.md) ซึ่งยืนยันแล้วว่า Claude, OpenAI Codex, และ Gemini CLI
> อ่านโครงสร้าง `SKILL.md` เดียวกันได้ เอกสารนี้ตรวจสอบเพิ่มอีก 44 เครื่องมือ/แพลตฟอร์ม AI coding agent
> ว่ารองรับ `SKILL.md` โดยตรง หรือรองรับผ่านรูปแบบอื่น หรือยังไม่มีข้อมูลยืนยัน

## วิธีตรวจสอบ (เพื่อความโปร่งใส)

แต่ละเครื่องมือถูกค้นด้วย web search จริงจากเอกสารทางการ/README/repo สาธารณะ ไม่ใช่การเดาจากชื่อ
ตัวที่ข้อมูลดูน่าสงสัย (ชื่อไม่คุ้น หรือ URL เอกสารดูเฉพาะเจาะจงผิดปกติ) ถูกสุ่มตรวจซ้ำอีกรอบด้วยการดึงหน้าเว็บจริง
(ZeroClaw, Command Code, bub, Agentman, Vita AI, pi/badlogic) — ยืนยันว่าเอกสารที่อ้างถึงมีอยู่จริงตามที่รายงาน
ตัวที่หาข้อมูลยืนยันไม่ได้ ระบุตรงๆ ว่า **"ไม่พบข้อมูลยืนยันต่อสาธารณะ"** แทนการเดา ตามหลัก "ห้ามตอบเท็จ"

**หมวดผลลัพธ์ 4 แบบ:**
- ✅ **ยืนยันแล้ว** — เครื่องมืออ่านโฟลเดอร์ + `SKILL.md` (frontmatter `name`+`description`) โดยตรง ไม่ต้องแปลงไฟล์
- 🔁 **ใช้ได้ผ่านรูปแบบอื่น** — มีกลไกรับคำสั่งกำหนดเอง แต่เป็นไฟล์/รูปแบบคนละแบบ (เช่น `AGENTS.md`, `.cursorrules`,
  ไฟล์ guideline เฉพาะของแพลตฟอร์ม) ต้องแปลง/คัดลอกเนื้อหาไปใส่
- ➖ **ไม่เกี่ยวข้อง** — ไม่ใช่ agent ที่รับคำสั่งกำหนดเองแบบนี้ (เช่น เป็น framework ไม่ใช่ตัว agent)
- ❓ **ไม่พบข้อมูลยืนยันต่อสาธารณะ** — ค้นแล้วไม่เจอเอกสารที่ยืนยันได้ ไม่ได้แปลว่าใช้ไม่ได้ แค่ยังไม่มีหลักฐาน

## ผลลัพธ์ที่น่าสนใจที่สุด: `.agents/skills/` กลายเป็นมาตรฐานพฤตินัยแล้ว

จาก 44 เครื่องมือ มีมากกว่า 20 ตัวที่หันมาอ่าน path เดียวกันคือ **`.agents/skills/<skill-name>/SKILL.md`**
(บางตัวเรียกคู่ขนานกับ path เฉพาะของตัวเอง เช่น Cursor อ่านทั้ง `.cursor/skills/` และ `.agents/skills/`)
แปลว่า **การแพ็ก Insightist skill ไว้ใต้โฟลเดอร์ `.agents/skills/` ที่ root ของโปรเจกต์ ใช้ได้ทันทีกับเครื่องมือ
ส่วนใหญ่ในตารางด้านล่างโดยไม่ต้องแก้ไฟล์อะไรเลย** นี่คือเหตุผลที่ [`CROSS_PLATFORM.md`](CROSS_PLATFORM.md)
แนะนำ path นี้เป็นหลัก

## ตารางเต็ม 44 เครื่องมือ

| # | เครื่องมือ | ผู้พัฒนา | ผล | อ่านจาก path ใด / ต้องทำอะไร |
|---|---|---|---|---|
| 1 | ChatGPT & Codex (Codex CLI) | OpenAI | ✅ ยืนยันแล้ว | `.agents/skills/`, `~/.agents/skills/` |
| 2 | Gemini CLI | Google | ✅ ยืนยันแล้ว | `~/.gemini/skills/` หรือ `.agents/skills/` |
| 3 | GitHub Copilot | GitHub | ✅ ยืนยันแล้ว | `.github/skills/`, `.agents/skills/`, `~/.copilot/skills/` |
| 4 | VS Code (Copilot Chat "Agent Skills") | Microsoft | ✅ ยืนยันแล้ว | `.github/skills/`, `.agents/skills/`, `~/.claude/skills/` |
| 5 | Cursor | Cursor Inc. | ✅ ยืนยันแล้ว | `.cursor/skills/` หรือ `.agents/skills/` (อ่าน `.claude/skills/`, `.codex/skills/` ด้วย) |
| 6 | Junie | JetBrains | ✅ ยืนยันแล้ว | `.junie/skills/` หรือ `.agents/skills/` |
| 7 | Mistral AI Vibe | Mistral AI | ✅ ยืนยันแล้ว | `.vibe/skills/` หรือ `.agents/skills/` |
| 8 | Trae | ByteDance | 🔁 ใช้ได้ผ่านรูปแบบอื่น | มี "Skills"/"Rules" ของตัวเองที่ `.trae/skills/` — ยืนยัน format ตรง SKILL.md เป๊ะไม่ได้ (เอกสารทางการดึงเนื้อหาเต็มไม่ได้) ควรทดสอบจริงก่อนใช้งานสำคัญ |
| 9 | Kiro | AWS | ✅ ยืนยันแล้ว | `.kiro/skills/` |
| 10 | Goose | Block | ✅ ยืนยันแล้ว | `.agents/skills/` (รองรับ path เก่า `.goose/skills/`, `.claude/skills/` ด้วย) |
| 11 | Amp | Sourcegraph | ✅ ยืนยันแล้ว | `.agents/skills/` หรือ `~/.config/agents/skills/` |
| 12 | OpenCode | SST | 🔁 ใช้ได้ผ่านรูปแบบอื่น | อ่าน `AGENTS.md` (ไม่มี skills-folder ในตัว) — ใส่เนื้อหา/ลิงก์ skill ไว้ใน AGENTS.md |
| 13 | OpenHands | OpenHands | ✅ ยืนยันแล้ว | `.agents/skills/` (path เก่า `.openhands/skills/` ก็ยังได้) |
| 14 | Roo Code | Roo Code | 🔁 ใช้ได้ผ่านรูปแบบอื่น | `.roo/rules/` (ไม่ใช่ SKILL.md) แต่ auto-load `AGENTS.md` ด้วย — คัดลอกเนื้อหา body ไปวาง |
| 15 | Factory (Droid) | Factory.ai | ✅ ยืนยันแล้ว | `.factory/skills/` |
| 16 | Tabnine | Tabnine | 🔁 ใช้ได้ผ่านรูปแบบอื่น | ไฟล์ "Guidelines" ที่ `.tabnine/guidelines/` — แปลง body ของ skill เป็น guideline 1 ไฟล์ |
| 17 | Qodo | Qodo | 🔁 ใช้ได้ผ่านรูปแบบอื่น | Custom agent เป็นไฟล์ `.toml` ใต้ `agents/` — ต้อง repackage เนื้อหาใหม่ |
| 18 | Databricks Genie Code | Databricks | 🔁 ใช้ได้ผ่านรูปแบบอื่น | อ่าน `AGENTS.md`/`CLAUDE.md` อัตโนมัติ หรือใส่ผ่าน `.assistant_instructions.md` |
| 19 | Snowflake Cortex Code | Snowflake | ✅ ยืนยันแล้ว | สแกนหา `SKILL.md` ในไดเรกทอรีลึกสุด 10 ชั้น (ไม่ต้องอยู่ในโฟลเดอร์ซ่อน) |
| 20 | Spring AI | Spring / VMware | ➖ ไม่เกี่ยวข้องโดยตรง | เป็น Java framework ไม่ใช่ agent สำเร็จรูป — มี community add-on (`spring-ai-agent-utils`) ที่รองรับ SKILL.md ถ้านักพัฒนาต่อเอง |
| 21 | Laravel Boost | Laravel | 🔁 ใช้ได้ผ่านรูปแบบอื่น | สร้างไฟล์ `.ai/guidelines/*.md`, `AGENTS.md`, `CLAUDE.md` อัตโนมัติ — ใส่เนื้อหา skill ไว้ในนั้น (ระวังถูก regenerate ทับ) |
| 22 | Pulumi Neo | Pulumi | 🔁 ใช้ได้ผ่านรูปแบบอื่น | อ่าน `AGENTS.md` ที่ root หรือ subdirectory |
| 23 | Hermes Agent | Nous Research | ✅ ยืนยันแล้ว | `~/.hermes/skills/<category>/<skill>/SKILL.md` หรือ `.agents/skills/` |
| 24 | OpenClaw | OpenClaw | ✅ ยืนยันแล้ว | `.agents/skills/`, `~/.agents/skills/` |
| 25 | ZeroClaw | ZeroClaw Labs | ✅ ยืนยันแล้ว (ตรวจซ้ำแล้ว) | รองรับทั้ง `SKILL.md` และ `SKILL.toml` |
| 26 | Letta (MemGPT เดิม) | Letta | ✅ ยืนยันแล้ว | ใช้มาตรฐานเปิด agentskills.io — `.agents/skills/` หรือ `~/.letta/skills/` |
| 27 | Mux / Xum | Coder | ❓ ไม่พบข้อมูลยืนยันต่อสาธารณะ | ผลิตภัณฑ์ดูเหมือนเปลี่ยนชื่อเป็น Xum แล้ว ไม่พบเอกสารผู้ใช้เรื่อง skills |
| 28 | Ona | Ona | 🔁 ใช้ได้ผ่านรูปแบบอื่น | อ่าน `AGENTS.md` ที่ root repo อัตโนมัติ |
| 29 | Emdash | General Action | ❓ ไม่พบข้อมูลยืนยันต่อสาธารณะ | เป็นตัวสั่งงาน agent อื่น (Claude Code/Codex ฯลฯ) ความเข้ากันได้จึงน่าจะขึ้นกับ backend agent ที่เลือก แต่ไม่มีเอกสารยืนยันชัด |
| 30 | Superconductor | Superconductor | 🔁 ใช้ได้ผ่านรูปแบบอื่น (ยังไม่ยืนยัน 100%) | มีแผง "Skills and MCP Servers" ของตัวเอง และรัน backend agent ได้หลายตัว (Claude Code ฯลฯ) — ไม่พบเอกสารยืนยันกลไก SKILL.md ของตัวเองโดยตรง |
| 31 | Workshop (Workshop.ai) | Workshop.ai | ❓ ไม่พบข้อมูลยืนยันต่อสาธารณะ | เอกสารที่เข้าถึงได้เน้นสร้างแอป/แดชบอร์ด ไม่พบเรื่อง skills/AGENTS.md |
| 32 | Piebald | Piebald | 🔁 น่าจะใช้ได้ (ยังไม่ยืนยัน 100%) | หน้าเว็บอ้างถึงมาตรฐาน agentskills.io เดียวกับ Letta แต่ไม่พบหน้าเอกสาร skills ของตัวเองโดยตรง |
| 33 | Firebender | Firebender | 🔁 ใช้ได้ผ่านรูปแบบอื่น | ไฟล์ `.mdc` ใต้ `.firebender/rules/` (frontmatter คนละแบบกับ SKILL.md) |
| 34 | Command Code | Command Code | ✅ ยืนยันแล้ว (ตรวจซ้ำแล้ว) | `.commandcode/skills/`, `~/.commandcode/skills/`, รองรับ `.agents/skills/` แบบ legacy ด้วย |
| 35 | VT Code | vinhnx | ✅ ยืนยันแล้ว | `.agents/skills/` (repo-level มาก่อน user-level) |
| 36 | Deep Code | Vegamo | ✅ ยืนยันแล้ว | `.deepcode/skills/` หรือ `.agents/skills/` |
| 37 | Autohand Code CLI | Autohand | ✅ ยืนยันแล้ว | `.autohand/skills/` — ประกาศชัดว่า auto-copy จากตำแหน่งของ Claude/Codex ได้ |
| 38 | pi | badlogic | ✅ ยืนยันแล้ว (ตรวจซ้ำแล้ว) | ใช้ "pi/Claude Code format" เดียวกัน — ถ้าจะให้ Claude Code เห็นด้วย ต้อง symlink ทีละ skill (Claude Code มองลึกแค่ 1 ชั้น) |
| 39 | fast-agent | evalstate | ✅ ยืนยันแล้ว | อ่านได้ทั้ง `.claude/skills/`, `.agents/skills/`, `.fast-agent/skills/` |
| 40 | nanobot | HKUDS | ❓ ไม่รองรับ SKILL.md แบบวางไฟล์ตรงๆ | "skills" ของมันคือ Python module ที่ลงทะเบียนแบบโปรแกรม ไม่ใช่ไฟล์ markdown ที่วางแล้วใช้ได้เลย |
| 41 | bub | bub.build | ✅ ยืนยันแล้ว (ตรวจซ้ำแล้ว) | `.agents/skills/<name>/SKILL.md` — ตรวจสอบชื่อโฟลเดอร์กับ `name` เข้มงวดมาก |
| 42 | Agentman | Agentman | ✅ ยืนยันแล้ว (ตรวจซ้ำแล้ว) | ประกาศชัดว่า "compatible with Anthropic's Agent Skills specification" — import เป็น `.skill`/`.zip` ผ่าน Skill Builder |
| 43 | Vita (Vita AI) | Vita AI | ❓ ไม่พบข้อมูลยืนยันต่อสาธารณะ (ตรวจซ้ำแล้ว) | หน้าเว็บทางการไม่มีกลไก skills/plugin/custom-instructions ใดๆ เลย |
| 44 | Google AI Edge Gallery | Google | ✅ ยืนยันแล้ว | มี Skill Manager จริงในแอป — import skill แบบ text-only ผ่าน URL หรือไฟล์ในเครื่อง |

**สรุปคะแนน:** ยืนยันแล้วตรงๆ 22 ตัว (50%) · ใช้ได้ผ่านรูปแบบอื่น (ต้องแปลงไฟล์) 13 ตัว (30%) ·
ไม่เกี่ยวข้องโดยตรง 1 ตัว · ไม่พบข้อมูลยืนยัน 5 ตัว · น่าจะใช้ได้แต่ยังไม่ยืนยัน 100% อีก 2 ตัว
(Trae, Superconductor, Piebald นับรวมอยู่ในกลุ่มนี้)

## ข้อจำกัดของการตรวจสอบนี้

- ข้อมูลนี้เป็นภาพ ณ วันที่ 13 กันยายน 2569 — เครื่องมือเหล่านี้เปลี่ยนเอกสาร/ฟีเจอร์เร็วมาก ควรตรวจสอบซ้ำกับ
  เอกสารทางการล่าสุดก่อนใช้งานจริง โดยเฉพาะตัวที่ทำเครื่องหมาย "ยังไม่ยืนยัน 100%"
- บางเครื่องมือ (โดยเฉพาะกลุ่ม 27–33 ที่เป็นโปรเจกต์เล็ก/ใหม่) มีข้อมูลสาธารณะจำกัด — "ไม่พบข้อมูลยืนยัน" ไม่ได้
  แปลว่าใช้งานไม่ได้ แค่ไม่มีหลักฐานสาธารณะพอจะยืนยัน ควรทดสอบจริงเองถ้าต้องใช้เครื่องมือนั้น
- รายการนี้ตรวจ "มีกลไกรับ SKILL.md/คำสั่งกำหนดเองหรือไม่" เท่านั้น ไม่ได้ทดสอบว่า agent แต่ละตัว "ทำตาม" เนื้อหา
  skill ได้ดีแค่ไหนจริงๆ — คุณภาพการทำงานตาม skill ยังขึ้นกับโมเดลและความสามารถของแต่ละเครื่องมือ

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill)*
