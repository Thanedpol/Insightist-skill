# Technical Documentation and Code Review Assistant

**ผู้ช่วยเขียน API doc, architecture note, runbook และให้ feedback รีวิวโค้ดอย่างเป็นระบบ สำหรับนักพัฒนาและทีมดูแลระบบ**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 25 · ผู้ประกอบวิชาชีพด้านเทคโนโลยีสารสนเทศและการสื่อสาร (Information and Communications Technology Professionals) |
| **Skill ID** | `25-technical-documentation-and-code-review-assistant` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักพัฒนาซอฟต์แวร์ Web Developer นักวิเคราะห์ระบบ ผู้ดูแลฐานข้อมูล ผู้ดูแลระบบเครือข่าย และผู้เชี่ยวชาญความมั่นคงปลอดภัยไซเบอร์
รวมถึงบทบาทใหม่ที่ ISCO-08 ยังไม่มีรหัสแยก เช่น Data Scientist, ML Engineer และ Prompt Engineer ซึ่งจัดอยู่ในหมวดย่อยนี้เช่นกัน

### ทำอะไรได้บ้าง

- เขียน **API documentation** ครบทั้ง endpoint, method, request/response พร้อมตัวอย่าง, error handling และ authentication
- เขียน **architecture note** อธิบาย component หลัก การไหลของข้อมูล และจุดเสี่ยงหรือ single point of failure
- เขียน **runbook** แบบทำตามได้ทันทีตอนระบบขัดข้อง พร้อม checkpoint ว่าแต่ละขั้นสำเร็จหรือไม่
- ทำเอกสาร **สรุปช่องโหว่หรือขั้นตอนตอบสนองเหตุการณ์ (incident response)**
- **รีวิวโค้ดอย่างเป็นระบบ** เรียงตามความสำคัญ: logic และ edge case → ความปลอดภัย → ประสิทธิภาพ → การดูแลรักษา → มาตรฐานทีม
- จัดระดับ feedback เป็น **ต้องแก้ก่อน merge / ควรแก้แต่ไม่บล็อก / ข้อเสนอแนะเพิ่มเติม** พร้อมระบุไฟล์และบรรทัด

### ตัวอย่างคำสั่ง

- "รีวิวโค้ดให้หน่อย นี่คือ diff ของฟังก์ชัน verifyToken"
- "เขียน API doc สำหรับ endpoint สร้างคำสั่งซื้อ ให้ทีมพาร์ตเนอร์เรียกใช้"
- "เขียน runbook ขั้นตอนกู้คืนฐานข้อมูลเมื่อ replica ล่ม"

### สิ่งที่จะได้รับ

**เอกสารทางเทคนิค** 5 ส่วน — (1) ภาพรวม (2) รายละเอียด endpoint/component/ขั้นตอน (3) ตัวอย่างการใช้งานจริง
(4) ข้อผิดพลาดที่พบบ่อยและวิธีแก้ (5) ข้อควรระวัง/ข้อจำกัด หรือ **สรุปการรีวิวโค้ด** แบ่งเป็น 🔴 ต้องแก้ก่อน merge
🟡 ควรแก้แต่ไม่บล็อก 🟢 ข้อเสนอแนะเพิ่มเติม ปิดท้ายด้วยสรุปว่าพร้อม merge หรือต้องแก้ไขก่อน

### ขอบเขตและข้อควรระวัง

- อ่านโค้ดหรือข้อมูลระบบจริงทั้งหมดก่อนให้ความเห็น ไม่รีวิวจากโค้ดที่ตัดตอนมาบางส่วน และไม่คาดเดาพฤติกรรมที่ไม่ได้ตรวจสอบ
- ไม่ระบุพฤติกรรมของ API หรือระบบที่ไม่แน่ใจ จะระบุว่าต้องตรวจสอบเพิ่มแทนการสรุปเดา
- ตัวอย่างโค้ดและคำสั่งในเอกสารต้องตรวจแล้วว่าถูกไวยากรณ์และตรงกับระบบจริง ไม่คัดลอกมาโดยไม่ตรวจ
- ใช้ภาษาตรงประเด็น สุภาพ ไม่ตัดสินตัวบุคคล

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Software and web developers, systems analysts, database administrators, network administrators and
cybersecurity specialists, plus newer roles that ISCO-08 has no separate code for yet, such as data scientists,
ML engineers and prompt engineers, which also fall under this sub-major group.

### What it can do

- Write **API documentation** covering endpoints, methods, request and response formats with examples, error handling and authentication
- Write an **architecture note** describing key components, data flow and risks such as single points of failure
- Write a **runbook** that can be followed under pressure during an outage, with checkpoints to confirm each step worked
- Document **vulnerability summaries or incident response procedures**
- **Review code systematically** in priority order: logic and edge cases, security, performance, maintainability, then team conventions
- Rank feedback as **blocking, non-blocking or optional**, each tied to a specific file and line

### Example prompts

- "Please review this diff of the verifyToken function."
- "Write API docs for the create-order endpoint so our partner team can integrate."
- "Write a runbook for restoring the database when a replica goes down."

### What you get

Either **technical documentation** in five sections: (1) overview, (2) endpoint, component or step details,
(3) real usage examples, (4) common errors and troubleshooting, and (5) cautions and limitations; or a **code review summary**
grouped into 🔴 must fix before merge, 🟡 should fix but not blocking, and 🟢 optional suggestions, ending with a
ready-to-merge or needs-changes verdict.

### Scope and limitations

- Reads the full code or system details before commenting; does not review partial excerpts or guess at unverified behaviour
- Does not state API or system behaviour it isn't sure of; flags it for further checking instead
- Code samples and commands in documents must be checked for correct syntax and real system behaviour, not copied unverified
- Keeps feedback direct and polite, focused on the code rather than the person

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/25-technical-documentation-and-code-review-assistant.zip`](../../../dist/25-technical-documentation-and-code-review-assistant.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
