# Invoice & Expense Tracker

**ผู้ช่วยจัดระเบียบใบแจ้งหนี้และใบเสร็จ ตรวจรายการซ้ำหรือผิดปกติ แล้วสรุปเป็นรายงานพร้อมส่งฝ่ายบัญชี**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `invoice-expense-tracker` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักบัญชี เจ้าหน้าที่บัญชีเจ้าหนี้ (accounts payable) และทีมบัญชีที่ต้องเคลียร์เอกสารค่าใช้จ่ายจำนวนมากให้เป็นระบบ
รวมถึงเจ้าของธุรกิจ SME และฟรีแลนซ์ที่ต้องเตรียมสรุปค่าใช้จ่ายส่งนักบัญชีหรือใช้ประกอบการยื่นภาษี

### ทำอะไรได้บ้าง

- รวมข้อมูลจาก **PDF รูปถ่ายใบเสร็จที่แปลงเป็นข้อความ statement หรือ Excel** ให้เป็นตารางเดียวที่ฟิลด์ครบ
- **จัดหมวดหมู่ค่าใช้จ่าย** ตามหมวดมาตรฐาน เช่น ต้นทุนขาย ค่าเช่า/สาธารณูปโภค เงินเดือน การตลาด ค่าเดินทาง ค่าที่ปรึกษา IT/ซอฟต์แวร์ ภาษี
- **ตรวจรายการซ้ำซ้อน** จากเลขที่เอกสารซ้ำ หรือผู้ขาย + ยอดเงิน + วันที่ใกล้กัน
- **ตรวจรายการผิดปกติ** เช่น ยอดสูงกว่าค่าเฉลี่ยของหมวดมาก ผู้ขายรายใหม่ยอดสูง ไม่มีใบกำกับภาษี หรือเอกสารผิดงวด
- สรุป **สถานะการจ่ายเงิน** แยกจ่ายแล้ว / ค้างจ่าย / เลยกำหนด เรียงรายการ overdue ตามความเร่งด่วน
- คำนวณ **ยอดเงินสดที่ต้องเตรียมจ่าย** ในงวดถัดไป
- จัดทำ **ตารางรายละเอียดพร้อมยื่นบัญชี** แยกยอดก่อน VAT, VAT และยอดรวม

### ตัวอย่างคำสั่ง

- "ช่วยจัดระเบียบใบเสร็จเดือนกรกฎาคมพวกนี้ แล้วสรุปค่าใช้จ่ายตามหมวด"
- "เช็คบิลซ้ำไหม และหารายการผิดปกติในค่าใช้จ่ายไตรมาสนี้ให้หน่อย"
- "เตรียมเอกสารสรุปรายจ่ายประจำเดือนส่งให้นักบัญชี"

### สิ่งที่จะได้รับ

รายงานสรุปใบแจ้งหนี้และค่าใช้จ่ายที่ระบุช่วงเวลา จำนวนรายการ และยอดรวม ตามด้วยตารางสรุปตามหมวดหมู่พร้อมสัดส่วน
สถานะการจ่ายเงิน รายการที่ต้องตรวจสอบเพิ่มเติม (สงสัยซ้ำ ผิดปกติ เอกสารไม่ครบ)
และตารางรายละเอียดทุกรายการที่พร้อมกรอกลงระบบบัญชีหรือแนบยื่นภาษี

### ขอบเขตและข้อควรระวัง

- **ไม่ฟันธงว่าซ้ำแน่นอน** รายการต้องสงสัยจะถูก flag พร้อมเหตุผล เพราะบางกรณีอาจเป็นการสั่งซื้อซ้ำจริง
- เอกสารที่อ่านไม่ชัดหรือข้อมูลไม่ครบจะ **ระบุให้ตรวจต้นฉบับ แทนการเดาตัวเลข**
- รายงานเป็นข้อมูลประกอบ ควรให้นักบัญชีตรวจทานก่อนบันทึกบัญชีหรือยื่นภาษีจริง

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Accountants, accounts payable clerks and bookkeeping teams who need to bring order to large piles of expense
documents, plus SME owners and freelancers preparing expense summaries for their accountant or for tax filing.

### What it can do

- Combine data from **PDFs, receipt photos converted to text, bank statements or spreadsheets** into one table with complete fields
- **Categorise expenses** into standard groups such as cost of goods sold, rent and utilities, payroll, marketing, travel, professional fees, IT and software, and taxes
- **Detect possible duplicates** by repeated document numbers, or the same vendor and amount on nearby dates
- **Spot anomalies** such as amounts far above the category average, new vendors with large bills, missing tax invoices or documents from the wrong period
- Summarise **payment status**: paid, outstanding, and overdue, with overdue items ranked by urgency
- Calculate the **cash needed for upcoming payments** next period
- Produce an **accounting-ready detail table** with pre-VAT amount, VAT and total

### Example prompts

- "Organise these July receipts and summarise spending by category."
- "Check for duplicate bills and flag anything unusual in this quarter's expenses."
- "Prepare this month's expense summary for my accountant."

### What you get

An invoice and expense report stating the period, item count and total spend, followed by a category summary
with percentages, payment status, a list of items needing review (suspected duplicates, anomalies, incomplete
documents), and a line-by-line table ready to enter into accounting software or attach to a tax filing.

### Scope and limitations

- **Never declares a duplicate with certainty**; suspects are flagged with reasons, since some may be genuine repeat orders
- Unclear or incomplete documents are **flagged for checking against the original rather than guessed**
- The report is supporting information; have an accountant review it before posting entries or filing taxes

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/invoice-expense-tracker.zip`](../../../dist/invoice-expense-tracker.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
