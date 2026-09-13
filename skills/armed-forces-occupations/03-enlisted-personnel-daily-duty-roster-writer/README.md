# Enlisted Personnel Daily Duty Roster Writer

**ผู้ช่วยจัดตารางเวรประจำวันและตารางกิจวัตรกองพักสำหรับพลทหาร แบบเป็นธรรมและตรวจสอบได้**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 0 · ทหาร (Armed Forces Occupations) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 03 · พลทหารและทหารยศอื่นๆ (Armed Forces Occupations, Other Ranks) |
| **Skill ID** | `03-enlisted-personnel-daily-duty-roster-writer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

พลทหารกองประจำการและพลทหารอาสาสมัคร รวมถึงผู้บังคับหมู่ ผู้บังคับหมวด หรือนายทหารชั้นประทวน
ที่ต้องจัดเวรรักษาการณ์ เวรทำความสะอาด เวรครัว และตารางกิจวัตรประจำวันของกองพัก

### ทำอะไรได้บ้าง

- จัดทำ **ตารางเวรประจำวัน** แยกประเภทเวร เช่น เวรรักษาการณ์ทั่วไป เวรทำความสะอาด เวรครัว พร้อมช่วงเวลาชัดเจน
- **หมุนเวียนรายชื่อเวรอย่างเป็นธรรม** ไม่ให้ใครเข้าเวรถี่เกินไป และเว้นวันพักที่เหมาะสม
- ทำ **ตารางกิจวัตรประจำวันกองพัก** ตั้งแต่เวลาปลุก ออกกำลังกาย อาหาร ทำความสะอาด ไปจนถึงเข้านอน
- สร้าง **แบบบันทึกการเข้าเวร (Duty Log)** มีช่องลงชื่อ เวลาเริ่ม-เลิกเวร และผู้รับมอบเวรต่อ
- สรุป **รายงานเวรประจำวัน** ส่งผู้บังคับหมวด/หมู่ รวมถึงการสลับหรือขาดเวรพร้อมเหตุผลเชิงธุรการ
- ตรวจทานว่าไม่มีชื่อซ้ำเวรในเวลาเดียวกัน และตารางครอบคลุมทุกวันในช่วงที่กำหนด

### ตัวอย่างคำสั่ง

- "ช่วยทำตารางเวรยามหน้าหมวดพัก 3 ผลัดต่อวัน สำหรับพลทหาร 12 นาย"
- "ขอตารางกิจวัตรกองพักตั้งแต่ตื่นนอนจนเข้านอน"
- "จัดเวรประจำวันทั้งเวรทำความสะอาดและเวรครัว พร้อมแบบบันทึกการเข้าเวร"

### สิ่งที่จะได้รับ

เอกสาร 4 ส่วน ได้แก่ (1) ตารางเวรประจำวันแยกประเภทเวรและช่วงเวลา (2) ตารางกิจวัตรประจำวันกองพัก
(3) บันทึกการเข้าเวรสำหรับส่งมอบเวร และ (4) สรุปรายงานเวรประจำวัน เช่น จำนวนผลัดเวรและการสลับ/ขาดเวร

### ขอบเขตและข้อควรระวัง

- ใช้สำหรับ **งานจัดตารางเวรและกิจวัตรประจำวันเชิงธุรการเท่านั้น**
- ไม่เกี่ยวข้องกับการวางกำลังเชิงยุทธวิธี ข้อมูลลับ หรือข้อมูลความมั่นคงที่ละเอียดอ่อน
- ใช้ชื่อหน่วยและบุคคลแบบทั่วไป/สมมติ ไม่ระบุข้อมูลระบุตัวตนจริงที่ละเอียดอ่อน

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Enlisted soldiers (conscripts and volunteers), and the squad leaders, platoon leaders or NCOs
who assign guard, cleaning and kitchen duties and set the daily barracks routine.

### What it can do

- Draft a **daily duty roster** by duty type, such as general guard, cleaning and kitchen duty, with clear shift times
- **Rotate names fairly** so no one pulls duty too often, with suitable rest days
- Set out the **daily barracks routine**, from wake-up, exercise, meals and cleaning through to lights out
- Create a **duty log** for sign-in, shift start and end times, and the handover to the next person
- Prepare a **daily duty report** for the platoon or squad leader, noting any swaps or missed shifts with administrative reasons
- Check that no one is double-booked and that every day in the period is covered

### Example prompts

- "Make a three-shift daily guard roster for a 12-soldier squad."
- "Give me a barracks daily routine from wake-up to lights out."
- "Set up today's cleaning and kitchen duties, with a duty log."

### What you get

A four-part document: (1) the daily duty roster by duty type and shift, (2) the daily barracks routine,
(3) a duty log for handovers, and (4) a daily duty report with the number of shifts and any swaps or absences.

### Scope and limitations

- For **administrative duty rostering and daily routine scheduling only**
- Does not cover tactical deployment, classified material or sensitive security information
- Uses generic or fictional unit and personnel names, never sensitive real identities

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/03-enlisted-personnel-daily-duty-roster-writer.zip`](../../../dist/03-enlisted-personnel-daily-duty-roster-writer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
