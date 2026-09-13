# ความเข้ากันได้กับเครื่องมือ AI Agent 44 ตัว

> ต่อยอดจาก [`CROSS_PLATFORM.md`](CROSS_PLATFORM.md) — เอกสารนี้บอกว่าเครื่องมือแต่ละตัวอ่าน skill ในคลังนี้ได้ไหม
> ต้องวางไฟล์ไว้ที่ไหน และมีข้อจำกัดอะไรบ้าง
>
> **ตรวจสอบล่าสุด: 13 กันยายน 2569 (2026)** — ทุกแถวตรวจจากเอกสารทางการ / README / source code ของเครื่องมือนั้นจริง
> (ลิงก์อยู่ในคอลัมน์สุดท้าย) เครื่องมือกลุ่มนี้เปลี่ยนเร็วมาก ถ้าจะใช้งานจริงควรเปิดลิงก์เช็คซ้ำอีกครั้ง

## สรุปสั้นๆ

| สถานะ | จำนวน | ความหมาย |
|---|---|---|
| ✅ อ่าน `SKILL.md` ได้โดยตรง | **37** | วางโฟลเดอร์ skill ไว้ใน path ที่ตารางบอก ใช้ได้เลย ไม่ต้องแปลงไฟล์ |
| 📥 นำเข้าผ่านแอป | **3** | อัปโหลด zip / ใส่ URL / ติดตั้งจาก marketplace ในหน้าแอป |
| 📄 รับได้แค่ `AGENTS.md` | **1** | ใช้ไฟล์ [`AGENTS.md`](../AGENTS.md) ที่ gen ไว้ให้แล้ว |
| ➖ ไม่ใช่ตัวที่รับ skill เอง | **3** | เป็น library / ตัวสั่งงาน agent อื่น / เลิกทำ agent แล้ว |

**ไม่ต้องสร้างไฟล์แปลงรายแพลตฟอร์ม** — `SKILL.md` ไฟล์เดียวใช้ได้ทั้ง 37 ตัว สิ่งที่ต้องทำมีแค่ "วางให้ถูกที่"

## ปัญหาจริงคือโครงสร้างโฟลเดอร์ (แก้ด้วย `scripts/install.py`)

คลังนี้เก็บ skill แยกตามหมวดอาชีพเป็น **2 ชั้น**: `skills/<หมวด>/<skill>/SKILL.md`
แต่เครื่องมือส่วนใหญ่ (เช่น Gemini CLI, OpenHands, VS Code) มองหาแค่ **ชั้นเดียว**: `<โฟลเดอร์ skills>/<skill>/SKILL.md`
ถ้า clone repo ไปวางทั้งก้อน หลายตัวจะหา skill ไม่เจอ ให้ใช้สคริปต์ที่ก๊อปแบบชั้นเดียวให้:

```bash
git clone https://github.com/Thanedpol/Insightist-skill.git
cd your-project
python3 ../Insightist-skill/scripts/install.py --target .agents/skills            # ทุก skill
python3 ../Insightist-skill/scripts/install.py --target .agents/skills --category managers
python3 ../Insightist-skill/scripts/install.py --list                              # ดูชื่อหมวด/skill
```

`--target` คือ path ในคอลัมน์ "วางไว้ที่" ของตารางด้านล่าง ใส่ได้ทั้งระดับโปรเจกต์ (`.agents/skills`) และระดับผู้ใช้ (`~/.agents/skills`)

## ข้อจำกัดที่ต้องรู้ก่อนใช้

- **VT Code จะข้าม skill ส่วนใหญ่ของคลังนี้** — VT Code จำกัด `description` ไม่เกิน 1024 **ไบต์** (ไม่ใช่ตัวอักษร)
  ภาษาไทย 1 ตัวใช้ 3 ไบต์ ทำให้ 63 จาก 67 skill เกินและถูกข้าม เครื่องมืออื่นนับเป็นตัวอักษรตามมาตรฐาน agentskills.io จึงไม่มีปัญหา
- **Kiro ไม่อ่าน `.agents/skills`** ต้องวางที่ `.kiro/skills` เท่านั้น
- **Trae** อ่าน `.agents/skills` ได้หลังเปิด Settings › Skills & Commands › Import Settings › "Enable .agents Skills Directory"
- **Snowflake Cortex Code** ไม่อ่าน `.agents/skills` และเวอร์ชัน Desktop ข้ามโฟลเดอร์ที่ขึ้นต้นด้วยจุด
- **Hermes Agent** ต้องสั่ง `hermes skills trust` ก่อน skill ระดับโปรเจกต์จะโหลด
- **Roo Code หยุดให้บริการแล้ว (15 พ.ค. 2569)** repo ถูก archive — ยังอ่านได้ถ้ามีติดตั้งอยู่ แต่ไม่แนะนำ
- **ChatGPT (เว็บ/แอป)** ไม่ได้อ่านโฟลเดอร์ แต่ให้อัปโหลด skill — เปิดให้เฉพาะแพ็กเกจ Business / Enterprise / Healthcare / Edu
- **ชื่อ skill** ทุกตัวในคลังนี้ผ่านกฎชื่อของทุกเครื่องมือแล้ว (ตัวพิมพ์เล็ก ตัวเลข ขีดกลาง ≤ 64 ตัวอักษร ตรงกับชื่อโฟลเดอร์)

## ตารางเต็ม 44 เครื่องมือ

ในคอลัมน์ "วางไว้ที่": 📁 = ระดับโปรเจกต์ · 🏠 = ระดับผู้ใช้ (`~` = home directory)

| # | เครื่องมือ | ผู้พัฒนา | สถานะ | วางไว้ที่ / วิธีใช้ | หมายเหตุ | แหล่งอ้างอิง |
|---|---|---|---|---|---|---|
| 1 | ChatGPT & Codex | OpenAI | ✅ | 📁 `.agents/skills` (โฟลเดอร์ปัจจุบันไล่ขึ้นถึง root ของ repo) · 🏠 `~/.agents/skills` · admin `/etc/codex/skills` | Codex CLI/IDE อ่านโฟลเดอร์ ส่วน ChatGPT ใช้อัปโหลด (เฉพาะ Business/Enterprise/Healthcare/Edu) · `agents/openai.yaml` เป็นไฟล์เสริม ไม่บังคับ | [Codex](https://learn.chatgpt.com/docs/build-skills) · [ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) |
| 2 | Gemini CLI | Google | ✅ | 📁 `.gemini/skills` หรือ `.agents/skills` · 🏠 `~/.gemini/skills` หรือ `~/.agents/skills` | มองลึกชั้นเดียว ต้องใช้ `install.py` | [docs](https://geminicli.com/docs/cli/skills/) |
| 3 | GitHub Copilot | GitHub | ✅ | 📁 `.github/skills`, `.claude/skills`, `.agents/skills` · 🏠 `~/.copilot/skills`, `~/.agents/skills` | ใช้ได้ทั้ง cloud agent, CLI, agent mode ใน VS Code/JetBrains | [docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| 4 | VS Code | Microsoft | ✅ | 📁 `.github/skills`, `.claude/skills`, `.agents/skills` · 🏠 `~/.copilot/skills`, `~/.claude/skills`, `~/.agents/skills` | ชื่อไม่ตรงโฟลเดอร์จะถูกข้ามเงียบๆ | [docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| 5 | Cursor | Cursor Inc. | ✅ | 📁 `.cursor/skills`, `.agents/skills`, `.claude/skills`, `.codex/skills` · 🏠 path เดียวกันใต้ `~` | | [docs](https://cursor.com/docs/context/skills) |
| 6 | Junie | JetBrains | ✅ | 📁 `.junie/skills`, `.agents/skills` · 🏠 `~/.junie/skills`, `~/.agents/skills` | | [docs](https://junie.jetbrains.com/docs/agent-skills.html) |
| 7 | Mistral AI Vibe | Mistral AI | ✅ | 📁 `.vibe/skills`, `.agents/skills` · 🏠 `~/.vibe/skills`, `~/.agents/skills` | skill ระดับโปรเจกต์โหลดเฉพาะโฟลเดอร์ที่ trust แล้ว | [docs](https://docs.mistral.ai/vibe/code/cli/skills) |
| 8 | Trae | ByteDance | ✅ | 📁 `.trae/skills` · 🏠 `~/.trae/skills` · หรืออัปโหลด `SKILL.md`/`.zip` ใน Settings › Skills & Commands | `.agents/skills` ต้องเปิด toggle ก่อน | [docs](https://docs.trae.ai/ide/skills) |
| 9 | Kiro | AWS | ✅ | 📁 `.kiro/skills` · 🏠 `~/.kiro/skills` (IDE/CLI) | ไม่อ่าน `.agents/skills` · เวอร์ชัน Web/Mobile ไม่มี global skills | [docs](https://kiro.dev/docs/skills/) |
| 10 | Goose | Agentic AI Foundation (เดิม Block) | ✅ | 📁 `.agents/skills` · 🏠 `~/.agents/skills` | ยังอ่าน `.goose/skills`, `.claude/skills` เพื่อความเข้ากันได้ย้อนหลัง | [docs](https://goose-docs.ai/docs/guides/context-engineering/using-skills/) |
| 11 | Amp | Amp (แยกออกจาก Sourcegraph) | ✅ | 📁 `.agents/skills` · 🏠 `~/.config/agents/skills`, `~/.agents/skills` | skill ระดับผู้ใช้ชื่อซ้ำจะบังตัวในโปรเจกต์ | [docs](https://ampcode.com/docs/customize/skills) |
| 12 | OpenCode | SST | ✅ | 📁 `.opencode/skills`, `.claude/skills`, `.agents/skills` · 🏠 `~/.config/opencode/skills`, `~/.agents/skills` | | [docs](https://opencode.ai/docs/skills/) |
| 13 | OpenHands | OpenHands | ✅ | 📁 `.agents/skills` · 🏠 `~/.agents/skills` | มองลึกชั้นเดียว ต้องใช้ `install.py` | [docs](https://docs.openhands.dev/overview/skills) |
| 14 | Roo Code | Roo Code | ✅ ⚠️ | 📁 `.roo/skills`, `.agents/skills` · 🏠 `~/.roo/skills`, `~/.agents/skills` | **หยุดให้บริการ 15 พ.ค. 2569** | [docs](https://roocodeinc.github.io/Roo-Code/features/skills) |
| 15 | Factory (Droid) | Factory.ai | ✅ | 📁 `.factory/skills`, `.agents/skills` · 🏠 `~/.factory/skills`, `~/.agents/skills` | | [docs](https://docs.factory.ai/cli/configuration/skills) |
| 16 | Tabnine | Tabnine | ✅ | CLI: 📁 `.agents/skills`, `.tabnine/agent/skills` · 🏠 `~/.agents/skills` — IDE plugin: 📁 `.tabnine/skills` | CLI โหลด skill โปรเจกต์เฉพาะโฟลเดอร์ที่ trust | [CLI](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills) |
| 17 | Qodo | Qodo | ➖ | — | Qodo Command/Gen CLI เลิกพัฒนาแล้ว ปลั๊กอินเหลือแต่งานรีวิวโค้ด ไม่มีตัวโหลด skill | [docs](https://docs.qodo.ai/agentic-toolbox/cli) |
| 18 | Databricks Genie Code | Databricks | ✅ | Workspace: `Workspace/.assistant/skills/<skill>/SKILL.md` · ผู้ใช้: `/Users/<user>/.assistant/skills/<skill>/SKILL.md` | เดิมชื่อ Databricks Assistant · แก้ skill แล้วต้องเปิดแชทใหม่ | [docs](https://docs.databricks.com/aws/en/genie-code/skills) |
| 19 | Snowflake Cortex Code | Snowflake | ✅ | CLI: 📁 `.cortex/skills` หรือ `.claude/skills` · 🏠 `~/.snowflake/cortex/skills` หรือ `~/.claude/skills` | ไม่อ่าน `.agents/skills` · Desktop ลงทะเบียนโฟลเดอร์เองได้ (สแกนลึก 10 ชั้น แต่ข้ามโฟลเดอร์ที่ขึ้นต้นด้วยจุด) | [docs](https://docs.snowflake.com/en/user-guide/cortex-code/extensibility) |
| 20 | Spring AI | Spring / VMware | ➖ | — | เป็น Java library ไม่ใช่ agent · ตัวเสริมจากชุมชน `spring-ai-agent-utils` โหลด `SKILL.md` ได้ถ้านักพัฒนาเขียนโค้ดชี้โฟลเดอร์เอง | [blog](https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills) |
| 21 | Laravel Boost | Laravel | ✅ | 📁 `.ai/skills/<skill>/SKILL.md` แล้วรัน `php artisan boost:update` | Boost ก๊อป skill ไปให้ agent แต่ละตัวเอง | [docs](https://laravel.com/docs/13.x/boost) |
| 22 | Pulumi Neo | Pulumi | 📄 | วาง [`AGENTS.md`](../AGENTS.md) ที่ root ของ repo (ใช้ `install.py --agents-md AGENTS.md`) | Neo โหลดได้เฉพาะแคตตาล็อก skill ของ Pulumi เอง ยังไม่มีวิธีเพิ่ม skill ของเราตรงๆ | [AGENTS.md](https://www.pulumi.com/blog/pulumi-neo-now-supports-agentsmd) · [skills](https://www.pulumi.com/docs/ai/skills) |
| 23 | Hermes Agent | Nous Research | ✅ | 📁 `.hermes/skills` หรือ `.agents/skills` · 🏠 `~/.hermes/skills` | สแกนลึกหลายชั้น · skill โปรเจกต์ต้อง `hermes skills trust` ก่อน · `~/.agents/skills` ต้องเพิ่มใน `skills.external_dirs` เอง | [docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) |
| 24 | OpenClaw | OpenClaw | ✅ | 📁 `skills`, `.agents/skills` ใน workspace · 🏠 `~/.agents/skills` | สแกนลึกได้ถึง 6 ชั้น | [docs](https://docs.openclaw.ai/tools/skills) |
| 25 | ZeroClaw | ZeroClaw Labs | ✅ | 🏠 `~/.zeroclaw/workspace/skills/<skill>/` | `SKILL.md` คือรูปแบบหลัก (`SKILL.toml` เป็นรูปแบบเก่าที่ยังรับอยู่) · ไม่อ่าน `.agents/skills` | [docs](https://docs.zeroclaw.com/master/en/tools/skills.html) |
| 26 | Letta | Letta | ✅ | 📁 `.agents/skills` · 🏠 `~/.letta/skills` | ซ้อนโฟลเดอร์ได้ | [docs](https://docs.letta.com/letta-agent/skills) |
| 27 | Mux (เปลี่ยนชื่อเป็น Xum) | Coder | ✅ | 📁 `.xum/skills`, `.agents/skills` · 🏠 `~/.xum/skills`, `~/.agents/skills` | `.mux/skills` เดิมยังอ่านได้ | [docs](https://xum.coder.com/agents/agent-skills) |
| 28 | Ona | Ona (เดิม Gitpod) | ✅ | 📁 `.ona/skills`, `.agents/skills`, `.claude/skills` | skill ระดับองค์กรต้องสร้างในหน้า Settings | [docs](https://ona.com/docs/ona/agents/skills) |
| 29 | Emdash | General Action | ➖ | — | เป็นตัวสั่งงาน agent อื่น (Claude Code, Codex, OpenCode ฯลฯ) — ให้ติดตั้ง skill กับ agent ที่เลือกใช้แทน | [docs](https://emdash.com/docs/skills) |
| 30 | Superconductor | Superconductor | ✅ | 📁 `.agents/skills` ใน repo | ส่งต่อ skill ให้ทุก agent ที่รันใน Superconductor | [docs](https://www.superconductor.com/docs/project/mcp-and-skills/custom-skills-from-your-repos) |
| 31 | Workshop | Workshop.ai | ✅ | 📁 `.workshop/skills` · หรือ Settings › Skills › Add (อัปโหลด .zip / import จาก GitHub) | ไม่อ่าน `.agents/skills` | [docs](https://docs.workshop.ai/core-concepts/skills) |
| 32 | Piebald | Piebald | ✅ | 📁 `.agents/skills`, `.claude/skills` · 🏠 `~/.agents/skills`, `~/.claude/skills` | | [docs](https://docs.piebald.ai/features/agentic/context) |
| 33 | Firebender | Firebender | ✅ | 📁 `.firebender/skills`, `.agents/skills` · 🏠 `~/.firebender/skills`, `~/.agents/skills` | จำกัดไฟล์ละ 100KB | [docs](https://docs.firebender.com/api-reference/skills) |
| 34 | Command Code | Command Code | ✅ | 📁 `.commandcode/skills`, `.agents/skills` · 🏠 `~/.commandcode/skills`, `~/.agents/skills` | | [docs](https://commandcode.ai/docs/skills) |
| 35 | VT Code | vinhnx | ✅ ⚠️ | 📁 `.agents/skills` · 🏠 `~/.agents/skills` | **จำกัด description ≤ 1024 ไบต์ → skill ภาษาไทย 63/67 ตัวถูกข้าม** | [guide](https://github.com/vinhnx/VTCode/blob/main/docs/skills/SKILLS_GUIDE.md) |
| 36 | Deep Code | Vegamo | ✅ | 📁 `.deepcode/skills`, `.agents/skills` · 🏠 `~/.deepcode/skills`, `~/.agents/skills` | | [docs](https://deepcode.vegamo.cn/en/docs/configuration/agent-skills) |
| 37 | Autohand Code CLI | Autohand | ✅ | 📁 `.autohand/skills`, `.agents/skills` · 🏠 `~/.autohand/skills`, `~/.agents/skills` | ก๊อปจาก `~/.claude/skills`, `~/.codex/skills` ให้อัตโนมัติ | [docs](https://github.com/autohandai/code-cli/blob/main/docs/agent-skills.md) |
| 38 | pi | badlogic | ✅ | 📁 `.pi/skills`, `.agents/skills` · 🏠 `~/.pi/agent/skills`, `~/.agents/skills` | | [docs](https://pi.dev/docs/latest/skills) |
| 39 | fast-agent | evalstate | ✅ | 📁 `.fast-agent/skills`, `.agents/skills`, `.claude/skills` | ตั้ง `skills.directories` ใน `fast-agent.yaml` แล้วจะแทนค่าเริ่มต้น | [docs](https://github.com/evalstate/fast-agent/blob/main/docs/docs/guides/skills.md) |
| 40 | nanobot | HKUDS | ✅ | 🏠 `~/.nanobot/workspace/skills/<skill>/SKILL.md` | | [docs](https://github.com/HKUDS/nanobot/blob/main/nanobot/skills/README.md) |
| 41 | bub | bub.build | ✅ | 📁 `.agents/skills` · 🏠 `~/.agents/skills` | ชื่อต้องตรงโฟลเดอร์เป๊ะ | [docs](https://bub.build/docs/getting-started/first-skill/) |
| 42 | Agentman | Agentman | 📥 | อัปโหลดไฟล์ `dist/<skill>.zip` ในหน้า Import ของ skills library | | [docs](https://agentman.ai/help/agentskills/import-skills-from-claude) |
| 43 | Vita AI | Vita AI | 📥 | ติดตั้งจาก marketplace ในแอป (ดึงจากแคตตาล็อก skills.sh) | ไม่มีอัปโหลดไฟล์หรือใส่ URL เอง | [docs](https://www.vita-ai.net/docs/features/agent-skills) |
| 44 | Google AI Edge Gallery | Google | 📥 | Skill Manager › "Load skill from URL" ใส่ URL ของ **โฟลเดอร์** skill (แอปจะต่อ `/SKILL.md` เอง) เช่น `https://raw.githubusercontent.com/Thanedpol/Insightist-skill/master/skills/managers/okr-goal-setter` · Android นำเข้าจากโฟลเดอร์ในเครื่องได้ | iOS มีบั๊กนำเข้าจาก URL ([#583](https://github.com/google-ai-edge/gallery/issues/583)) | [docs](https://github.com/google-ai-edge/gallery/blob/main/skills/README.md) |

## ข้อจำกัดของเอกสารนี้

- ตรวจแค่ว่าเครื่องมือ **โหลด** skill ได้หรือไม่ ไม่ได้วัดว่า agent แต่ละตัว **ทำตาม** เนื้อหา skill ได้ดีแค่ไหน — คุณภาพยังขึ้นกับโมเดลที่ใช้
- ตัวเลขและ path เป็นภาพ ณ วันที่ตรวจ ถ้าเจอข้อมูลที่เปลี่ยนไปแล้ว ส่ง PR แก้พร้อมลิงก์แหล่งอ้างอิงได้เลย

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill)*
