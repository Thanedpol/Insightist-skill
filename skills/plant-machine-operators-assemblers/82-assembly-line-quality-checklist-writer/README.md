# Assembly Line Quality Checklist Writer

**ผู้ช่วยทำแบบตรวจสอบคุณภาพประจำสถานีงานและบันทึกข้อบกพร่องที่ตรวจสอบย้อนกลับได้ สำหรับพนักงานในสายการประกอบ**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 8 · ผู้ควบคุมเครื่องจักรโรงงานและผู้ประกอบชิ้นงาน (Plant and Machine Operators, and Assemblers) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 82 · ผู้ประกอบชิ้นงาน (Assemblers) |
| **Skill ID** | `82-assembly-line-quality-checklist-writer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

พนักงานประกอบเครื่องจักรกล พนักงานประกอบอุปกรณ์ไฟฟ้า พนักงานประกอบอุปกรณ์อิเล็กทรอนิกส์
และพนักงานประกอบชิ้นส่วนยานยนต์ รวมถึงหัวหน้าไลน์ที่ต้องการรูปแบบบันทึกข้อบกพร่องมาตรฐานไว้วิเคราะห์อัตราของเสีย

### ทำอะไรได้บ้าง

- สร้าง **แบบตรวจสอบคุณภาพประจำสถานีงาน** ระบุสถานีงาน รุ่น/รหัสชิ้นงาน กะ และผู้ตรวจสอบ
- จัดกลุ่ม **จุดตรวจตามประเภท** เช่น ความครบถ้วนของชิ้นส่วน (ตาม BOM) ความถูกต้องของการประกอบ ค่าที่วัดได้ และลักษณะภายนอก
- กำหนด **เกณฑ์ผ่าน/ไม่ผ่านของแต่ละจุดตรวจ** ที่ตัดสินได้จริงหน้างาน
- เรียง **ลำดับการตรวจให้ทันจังหวะการผลิต (takt time)** โดยไม่ทำให้ไลน์สะดุด
- ออกแบบ **บันทึกข้อบกพร่องที่ตรวจสอบย้อนกลับได้** มีหมายเลขชิ้นงาน/lot วันเวลา สถานี สาเหตุเบื้องต้น การจัดการ และผู้บันทึก
- แยก **เส้นทางยกระดับปัญหา** ระหว่างข้อบกพร่องที่แก้หน้างานได้ กับที่ต้องแจ้งหัวหน้าไลน์หรือ QC ทันที
- สรุป **อัตราของเสียต่อกะ** เพื่อเทียบแนวโน้มข้ามกะหรือข้ามวัน

### ตัวอย่างคำสั่ง

- "ช่วยทำ QC checklist สถานีประกอบชุดสายไฟรถยนต์ กะเช้าตรวจ 150 ชิ้น พบขั้วต่อไม่ล็อก 2 ชิ้น"
- "ขอรูปแบบ defect log สำหรับไลน์ประกอบอุปกรณ์อิเล็กทรอนิกส์"
- "ทำ checklist ตรวจสอบคุณภาพงานประกอบก่อนส่งชิ้นงานไปสถานีถัดไป"

### สิ่งที่จะได้รับ

เอกสาร 2 ส่วน — (1) **แบบตรวจสอบคุณภาพประจำสถานีงาน** เป็นตารางจุดตรวจ เกณฑ์ ผลผ่าน/ไม่ผ่าน และหมายเหตุ
(2) **บันทึกข้อบกพร่อง** ที่มีฟิลด์สำหรับตรวจสอบย้อนกลับครบ ปิดท้ายด้วยสรุปกะ จำนวนที่ตรวจ ผ่าน ไม่ผ่าน และอัตราของเสีย (%)

### ขอบเขตและข้อควรระวัง

- **ไม่กำหนดค่ามาตรฐานเฉพาะเจาะจงขึ้นเอง** (เช่น ค่าแรงบิด ระยะห่าง) จะอ้างอิงตามมาตรฐานงาน (Work Instruction) ของรุ่นนั้น
- ควรตรวจสอบเกณฑ์กับฝ่ายวิศวกรรมหรือ QC ก่อนนำไปใช้จริง
- ใส่เฉพาะจุดตรวจที่สถานีงานนั้นทำได้จริง ไม่ใส่จุดที่ต้องใช้เครื่องมือหรือขั้นตอนที่สถานีไม่มี
- ข้อบกพร่องด้านความปลอดภัยหรือพบซ้ำเกินกำหนดต้องแจ้งหัวหน้าไลน์หรือ QC

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Assemblers of mechanical machinery, electrical equipment, electronic equipment and automotive
parts, plus line leaders who need a standard defect log to analyse scrap rates.

### What it can do

- Create a **workstation quality checklist** with station, model or part number, shift and inspector
- Group **check points by type**: part completeness (against the BOM), assembly correctness, measured values and appearance
- Set **pass/fail criteria for each check point** that can actually be judged at the station
- Order checks to **fit the line's takt time** so inspection does not slow the line
- Design a **traceable defect log** with part or lot number, date and time, station, likely cause, disposition and recorder
- Define **escalation paths**, separating defects the operator can fix on the spot from those that must go to the line leader or QC immediately
- Summarise the **defect rate per shift** so trends can be compared across shifts and days

### Example prompts

- "Make a QC checklist for a car wiring-harness station. The morning shift checked 150 units and found 2 connectors not fully latched."
- "Give me a defect log format for an electronics assembly line."
- "Create a quality checklist for assembled parts before they move to the next station."

### What you get

Two parts: (1) a **workstation quality checklist** table of check points, criteria, pass/fail result
and notes, and (2) a **defect tracking log** with all the fields needed for traceability. It ends
with a shift summary: units checked, passed, failed and defect rate (%).

### Scope and limitations

- **Does not invent specific specification values** (such as torque or clearances); refers to the Work Instruction for that model instead
- Check criteria with engineering or QC before using the checklist for real
- Includes only checks the station can actually perform, not ones needing tools or steps it lacks
- Safety-related defects, or defects that repeat beyond the set limit, must be escalated to the line leader or QC

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/82-assembly-line-quality-checklist-writer.zip`](../../../dist/82-assembly-line-quality-checklist-writer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
