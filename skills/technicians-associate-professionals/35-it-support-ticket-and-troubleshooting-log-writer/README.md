# IT Support Ticket and Troubleshooting Log Writer

**ผู้ช่วยเขียน IT support ticket บันทึกการแก้ไขปัญหา และบันทึกฐานความรู้ สำหรับเจ้าหน้าที่ Helpdesk และช่างเทคนิคไอที**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 3 · เจ้าหน้าที่เทคนิคและผู้ประกอบวิชาชีพที่เกี่ยวข้อง (Technicians and Associate Professionals) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 35 · ช่างเทคนิคด้านสารสนเทศและการสื่อสาร (Information and Communications Technicians) |
| **Skill ID** | `35-it-support-ticket-and-troubleshooting-log-writer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

เจ้าหน้าที่ IT Support/Helpdesk ช่างเทคนิคเครือข่าย ช่างเทคนิคปฏิบัติการไอที ช่างเทคนิควิศวกรรมโทรคมนาคม
และช่างเทคนิคกระจายเสียงและโสตทัศนูปกรณ์ ที่ต้องบันทึกการรับแจ้ง การวินิจฉัย และการแก้ไขปัญหาอย่างเป็นระบบ

### ทำอะไรได้บ้าง

- เปิด **IT support ticket** ให้ครบข้อมูล: ผู้แจ้ง เวลา ระบบ/อุปกรณ์ อาการ และผลกระทบต่องาน
- จัด **หมวดปัญหาและระดับความสำคัญ** (ฮาร์ดแวร์ ซอฟต์แวร์ เครือข่าย สิทธิ์การเข้าถึง / วิกฤต-สูง-ปานกลาง-ต่ำ)
- เขียน **troubleshooting log** เรียงขั้นตอนวินิจฉัยที่ตรวจจริงพร้อมผลของแต่ละขั้น
- สรุป **สาเหตุที่แท้จริง (root cause)** จากหลักฐาน และ **วิธีแก้ไขที่ใช้จริง** พร้อมเวลาที่ใช้
- ทำ **บันทึกฐานความรู้ (knowledge-base entry)** สำหรับปัญหาที่อาจเกิดซ้ำ ให้ทีมค้นหาและใช้ต่อได้
- สรุป **เหตุขัดข้องของระบบ (incident)** หลังแก้ไขเสร็จ พร้อมสถานะปิดงานและสิ่งที่ต้องติดตาม

### ตัวอย่างคำสั่ง

- "เปิด ticket แจ้งปัญหา พนักงานเข้าอีเมลบริษัทไม่ได้ตั้งแต่เช้า ตรวจแล้วรหัสผ่านหมดอายุ"
- "เขียน troubleshooting log การแก้ปัญหา Wi-Fi ชั้น 5 หลุดบ่อย"
- "สรุปการแก้ปัญหาเครื่องพิมพ์ครั้งนี้เป็น knowledge base entry"

### สิ่งที่จะได้รับ

Ticket/log ที่มีหัวข้อมูล (หมายเลข ticket ผู้แจ้ง วันที่ ระบบ ระดับความสำคัญ) และเนื้อหา 6 ส่วน — (1) อาการที่พบตามคำแจ้ง
(2) ขั้นตอนการวินิจฉัย (3) สาเหตุที่แท้จริง (4) วิธีแก้ไขที่ใช้พร้อมเวลา (5) บันทึกความรู้ (ถ้าปัญหาเกิดซ้ำได้) (6) สถานะปิดงานและสิ่งที่ต้องติดตาม

### ขอบเขตและข้อควรระวัง

- ไม่เดาสาเหตุที่ยังไม่ได้ตรวจสอบหลักฐาน หากไม่แน่ใจจะระบุว่า "ยังไม่สามารถระบุสาเหตุแน่ชัด"
- บันทึกเฉพาะขั้นตอนวินิจฉัยและวิธีแก้ที่ทำจริงและตรวจผลได้ ไม่ใช่คำแนะนำทั่วไปที่ยังไม่ได้ลอง
- ความถูกต้องของ log ขึ้นกับข้อมูลที่ช่างให้มา ควรทบทวนก่อนปิด ticket หรือเผยแพร่เป็นฐานความรู้

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

IT support and helpdesk staff, network technicians, IT operations technicians, telecommunications engineering
technicians and broadcasting or audio-visual technicians who need to document how issues were reported, diagnosed
and fixed.

### What it can do

- Open a complete **IT support ticket**: reporter, time, system or device, symptoms and business impact
- Assign a **problem category and priority** (hardware, software, network, access / critical, high, medium, low)
- Write a **troubleshooting log** listing the diagnostic steps actually taken and the result of each
- Record the **root cause** based on evidence and the **resolution actually applied**, with time taken
- Create a **knowledge-base entry** for issues likely to recur, so the team can find and reuse the fix
- Summarise a **system incident** after it is resolved, with closing status and any follow-up

### Example prompts

- "Open a ticket: an employee can't access company email since this morning; the password had expired."
- "Write a troubleshooting log for the frequent Wi-Fi drops on the 5th floor."
- "Turn this printer fix into a knowledge-base entry."

### What you get

A ticket or log with a header (ticket number, reporter, date, system, priority) and six sections: (1) reported symptoms,
(2) diagnostic steps, (3) root cause, (4) resolution and time taken, (5) knowledge-base entry (if the issue may recur),
and (6) closing status and follow-up.

### Scope and limitations

- Does not guess at causes that haven't been verified; if unsure, it states that the root cause could not yet be confirmed
- Records only diagnostic steps and fixes that were actually carried out and checked, not untested general advice
- The log is only as accurate as the technician's input, so review it before closing the ticket or publishing it to the knowledge base

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/35-it-support-ticket-and-troubleshooting-log-writer.zip`](../../../dist/35-it-support-ticket-and-troubleshooting-log-writer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
