# Data Cleaning Playbook

**ผู้ช่วยนักวิเคราะห์ข้อมูลทำความสะอาดชุดข้อมูลอย่างเป็นระบบ พร้อมบันทึกว่าทำอะไรไปและทำไม**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `data-cleaning-playbook` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักวิเคราะห์ข้อมูล (data analyst) นักวิทยาศาสตร์ข้อมูล (data scientist) นักวิเคราะห์ BI และวิศวกรข้อมูล
ที่ต้องเตรียมข้อมูลดิบก่อนทำ dashboard รายงาน หรือ machine learning
รวมถึงผู้ที่รับผิดชอบงาน data audit หรือ data quality check เป็นระยะ

### ทำอะไรได้บ้าง

- ทำ **data profiling** ดูจำนวนแถว/คอลัมน์ ชนิดข้อมูล ค่าตัวอย่าง และสถิติเบื้องต้นก่อนแก้อะไร
- จัดการ **missing values** ด้วยกฎที่ชัดเจน เช่น ตัดคอลัมน์ ตัดแถว เติม median/mean/mode หรือใส่ "Unknown"
- หา **duplicates** ทั้งแบบ exact match และแบบ key-based พร้อมระวัง false duplicate
- ตรวจ **outliers** ด้วย IQR หรือ Z-score แล้วแยกว่าเป็นข้อมูลกรอกผิดหรือค่าจริงที่ผิดปกติ
- แก้ **inconsistent format** เช่น รูปแบบวันที่ (ISO 8601) ตัวพิมพ์และช่องว่าง หน่วย ชื่อหมวดหมู่ที่สะกดต่างกัน และชนิดข้อมูลผิด
- ทำ **validation pass** เช็คว่าจำนวนแถวและผลรวมสำคัญยังสมเหตุสมผลเมื่อเทียบกับต้นฉบับ
- เขียน **log การเปลี่ยนแปลงพร้อมเหตุผล** ให้ตรวจสอบย้อนหลังได้

### ตัวอย่างคำสั่ง

- "ช่วยทำความสะอาดข้อมูลลูกค้าในไฟล์ CSV นี้หน่อย ข้อมูลรกมาก"
- "หา duplicate และเช็ค missing value ในยอดขายชุดนี้ก่อนทำ dashboard"
- "ทำไมตัวเลขรวมไม่ตรงกัน ช่วยเตรียมข้อมูลก่อนวิเคราะห์ให้ที"

### สิ่งที่จะได้รับ

สรุปการทำความสะอาดข้อมูลที่มีตารางเปรียบเทียบก่อน-หลัง (จำนวนแถว คอลัมน์ missing values แถวซ้ำ)
รายละเอียดสิ่งที่ทำพร้อมเหตุผลใน 4 หัวข้อ (missing values, duplicates, outliers, inconsistent format)
จุดที่ต้องให้เจ้าของข้อมูลยืนยัน และสรุปสถานะว่าข้อมูลพร้อมใช้ต่อกับงานอะไรได้บ้าง

### ขอบเขตและข้อควรระวัง

- **ไม่ลบ outlier ทิ้งอัตโนมัติ** ต้องตรวจที่มาก่อน ค่าจริงที่ผิดปกติจะเก็บไว้และทำเครื่องหมาย
- **ไม่เติมค่าแบบเดาสุ่ม** ทุกการเติมหรือลบต้องมีเหตุผลทางสถิติหรือ business logic กำกับ
- ข้อมูลที่ไม่แน่ใจจะแยกไว้ให้เจ้าของข้อมูลยืนยัน ควรเก็บไฟล์ต้นฉบับไว้เสมอ

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Data analysts, data scientists, BI analysts and data engineers who prepare raw data before building
dashboards, reports or machine-learning models, as well as anyone running periodic data audits or
data-quality checks.

### What it can do

- Run **data profiling**: row and column counts, data types, sample rows and basic statistics before changing anything
- Handle **missing values** with clear rules: drop the column or row, fill with median, mean or mode, or label as "Unknown"
- Find **duplicates**, both exact matches and key-based, while watching for false duplicates
- Detect **outliers** with IQR or Z-score and tell data-entry errors apart from genuine extreme values
- Fix **inconsistent formats**: dates (to ISO 8601), casing and stray spaces, units, variant category spellings and wrong data types
- Do a **validation pass** to confirm row counts and key totals still make sense against the original
- Keep a **change log with reasons** so every decision can be audited later

### Example prompts

- "Clean up the customer data in this CSV. It's a mess."
- "Find duplicates and check missing values in this sales data before I build a dashboard."
- "Why don't the totals match? Prep this data for analysis."

### What you get

A data-cleaning summary with a before/after table (rows, columns, missing values, duplicates), a record of
what was done and why under four headings (missing values, duplicates, outliers, inconsistent formats), items
the data owner needs to confirm, and a short note on what the cleaned data is ready for.

### Scope and limitations

- **Never deletes outliers automatically**; their source is checked first, and genuine extreme values are kept and flagged
- **No guesswork fills**; every fill or deletion is backed by a statistical or business reason
- Uncertain items are set aside for the data owner to confirm; always keep your original file

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/data-cleaning-playbook.zip`](../../../dist/data-cleaning-playbook.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
