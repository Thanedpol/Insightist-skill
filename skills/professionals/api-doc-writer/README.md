# API Doc Writer

**ผู้ช่วยนักพัฒนา backend แปลงโค้ดหรือ spec ให้เป็นเอกสาร API ที่อ่านง่ายและเรียกใช้ได้จริง**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `api-doc-writer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักพัฒนาซอฟต์แวร์ฝั่ง backend วิศวกร API และ tech lead ที่ต้องส่งมอบเอกสารให้ทีม frontend/mobile
หรือพาร์ตเนอร์ภายนอกที่จะเชื่อมระบบ รวมถึงนักเขียนเอกสารเทคนิค (technical writer) และทีม support
ที่ต้องใช้เอกสาร error code ช่วยไล่ปัญหาจากลูกค้า

### ทำอะไรได้บ้าง

- แปลง **route handler, controller, OpenAPI/Swagger spec หรือ Postman collection** ให้เป็นเอกสารอ่านง่าย
- สรุป **Method + Path, คำอธิบาย และวิธี authentication** ของแต่ละ endpoint
- ทำ **ตาราง parameters** แยก path / query / body พร้อมชนิดข้อมูล ความจำเป็น ค่า default และ constraint
- ระบุ **response schema** กรณีสำเร็จ รวมถึง field ที่เกี่ยวกับการแบ่งหน้า (pagination)
- รวบรวม **error codes** พร้อมเงื่อนไขที่ทำให้เกิดและโครงสร้าง error response
- เขียน **ตัวอย่าง request/response (curl, JSON)** ด้วยค่าสมมติที่สมจริง copy ไปทดสอบได้ทันที
- จัดกลุ่ม endpoint ตาม resource เรียงตาม CRUD และแยก **จุดที่ต้องยืนยันเพิ่มเติม** ไว้ท้ายเอกสาร

### ตัวอย่างคำสั่ง

- "ช่วยเขียน API doc จาก route FastAPI ตัวนี้ให้หน่อย"
- "ทำ API reference ของ OpenAPI spec นี้ ส่งให้ทีม frontend อ่าน"
- "อธิบาย endpoint สร้างคำสั่งซื้อนี้ให้พาร์ตเนอร์เรียกใช้ได้"

### สิ่งที่จะได้รับ

เอกสาร API ที่เริ่มด้วยภาพรวม (Base URL และวิธี authentication) แล้วแบ่งเป็นกลุ่มตาม resource
แต่ละ endpoint มีตาราง parameters, response สำเร็จ, ตาราง error codes และตัวอย่าง request/response
ปิดท้ายด้วยหมายเหตุรายการที่ข้อมูลต้นทางยังไม่ครบและต้องเช็คกับทีม backend

### ขอบเขตและข้อควรระวัง

- ไม่เดาข้อมูลที่ไม่มีในโค้ดหรือ spec แต่จะระบุว่า **"ต้องยืนยันเพิ่มเติม"** แยกจากข้อมูลที่ยืนยันแล้ว
- **ไม่สร้าง error code ที่ไม่มีอยู่จริง** กรณีมาตรฐานที่อนุมานจาก logic จะทำเครื่องหมายให้ทีม backend ยืนยัน
- ตรวจให้ชื่อ field ในตัวอย่าง JSON ตรงกับ schema ทุกจุด แต่ควรทดสอบเรียก API จริงก่อนเผยแพร่เอกสาร

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Backend software developers, API engineers and tech leads who hand off endpoints to frontend or mobile
teams or to external integration partners, as well as technical writers and support teams who rely on
error-code documentation to troubleshoot customer issues.

### What it can do

- Turn **route handlers, controllers, OpenAPI/Swagger specs or Postman collections** into readable docs
- Summarise each endpoint's **method and path, purpose and authentication**
- Build a **parameters table** split into path, query and body, with type, required flag, default and constraints
- Document the **success response schema**, including pagination fields where relevant
- List **error codes** with the conditions that trigger them and the error response shape
- Write **copy-and-run request/response examples (curl, JSON)** with realistic sample values
- Group endpoints by resource in CRUD order and collect **open questions to confirm** at the end

### Example prompts

- "Write API docs for this FastAPI route."
- "Turn this OpenAPI spec into an API reference for the frontend team."
- "Document this create-order endpoint so a partner can call it."

### What you get

An API document that opens with an overview (base URL and authentication), then groups endpoints by
resource. Each endpoint has a parameters table, success response, error-code table and request/response
examples. It closes with notes on anything the source didn't cover that the backend team needs to confirm.

### Scope and limitations

- Doesn't guess missing details; gaps are flagged as **"needs confirmation"**, kept apart from verified information
- **Never invents error codes**; standard cases inferred from the logic are marked for backend confirmation
- Field names in examples are checked against the schema, but test against the live API before publishing

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/api-doc-writer.zip`](../../../dist/api-doc-writer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
