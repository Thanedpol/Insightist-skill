# Inventory and Accounting Clerk Report Builder

**ผู้ช่วยทำรายงานกระทบยอดสต๊อก สรุปบัญชีและเงินเดือนเบื้องต้น จากตัวเลขจริงที่ผู้ใช้ให้มา สำหรับเสมียนบัญชีและพนักงานคลังสินค้า**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 4 · เสมียน / งานธุรการสนับสนุน (Clerical Support Workers) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 43 · เสมียนบันทึกตัวเลขและวัสดุ (Numerical and Material Recording Clerks) |
| **Skill ID** | `43-inventory-and-accounting-clerk-report-builder` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

เสมียนบัญชี พนักงานการเงิน พนักงานเงินเดือน พนักงานคลังสินค้า/สต๊อก พนักงานสถิติ
พนักงานวางแผนการผลิต และพนักงานธุรการขนส่ง ที่ต้องจัดตัวเลขที่มีอยู่แล้วให้เป็นรายงานอ่านง่ายก่อนส่งต่อ

### ทำอะไรได้บ้าง

- ทำ **รายงานกระทบยอดสินค้าคงคลัง** เทียบยอดในระบบกับยอดนับจริงทีละรายการ คำนวณผลต่าง และจัดกลุ่มเป็นตรงกัน/ขาด/เกิน
- สรุป **รายการรับ-จ่ายประจำเดือน** ตามหมวดหมู่ที่ผู้ใช้กำหนด พร้อมยอดรวมแต่ละหมวดและยอดรวมทั้งหมด
- สรุป **ยอดเงินเดือนสุทธิ** จากชั่วโมงทำงาน อัตราจ้าง และรายการหัก ตามสูตรที่ผู้ใช้ให้มา
- จัดตัวเลข **การผลิต สต๊อก หรือการเดินรถ/จัดส่ง** ให้เป็นรายงานสรุปประจำงวด
- **ตรวจความสมเหตุสมผลของตัวเลข** เช่น ยอดย่อยรวมตรงกับยอดใหญ่หรือไม่ มีค่าติดลบในช่องที่ไม่ควรติดลบหรือไม่
- ระบุ **ประเด็นที่ต้องส่งต่อให้ฝ่ายบัญชี/หัวหน้างานตรวจสอบ** เช่น ผลต่างผิดปกติหรือข้อมูลไม่ครบ

### ตัวอย่างคำสั่ง

- "ช่วยกระทบยอดสต๊อก สินค้า A ยอดในระบบ 500 ชิ้น นับจริงได้ 480 ชิ้น สินค้า B ยอดในระบบ 200 ชิ้น นับจริงได้ 205 ชิ้น"
- "สรุปบัญชีเบื้องต้นรายการรับ-จ่ายเดือนนี้ให้เป็นตาราง ก่อนส่งฝ่ายบัญชีตรวจ"
- "ทำสรุปเงินเดือนพนักงาน 5 คน จากชั่วโมงทำงานและค่าล่วงเวลาที่แนบมา"

### สิ่งที่จะได้รับ

รายงานที่ระบุงวด/วันที่และแหล่งที่มาของตัวเลข พร้อมตารางสรุปรายการ ยอดตามระบบ ยอดจริง ผลต่าง และหมายเหตุ
ตามด้วยยอดรวมทั้งหมด และรายการประเด็นที่ต้องตรวจสอบเพิ่มเติม

### ขอบเขตและข้อควรระวัง

- **ใช้เฉพาะตัวเลขที่ผู้ใช้ให้มา** ไม่แต่งหรือประมาณยอดบัญชี ภาษี หรือยอดคงคลังขึ้นเอง
- ไม่ใช้อัตราภาษีหรือประกันสังคมที่ไม่ได้รับมา และไม่ใช่การคำนวณภาษีหรือปิดงบบัญชีที่ต้องใช้ดุลพินิจทางวิชาชีพบัญชี
- ข้อมูลที่ขาดหรือตัวเลขผิดปกติจะถูกแจ้งให้ผู้ใช้ตรวจสอบ แทนการแก้หรือปิดยอดเอง
- รายงานควรผ่านการตรวจของฝ่ายบัญชีหรือหัวหน้างานก่อนใช้เป็นทางการ

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Accounting clerks, finance and payroll staff, stock and warehouse clerks, statistical clerks,
production planning clerks and transport clerks who need to turn existing figures into clear reports.

### What it can do

- Build an **inventory reconciliation report** comparing book stock with the physical count item by item, calculating variances and grouping them as matched, short or over
- Summarise **monthly income and expenses** under the categories you set, with subtotals and a grand total
- Summarise **net pay per employee** from hours, pay rates and deductions, using only the formula you provide
- Turn **production, stock, trip or delivery figures** into a periodic summary report
- **Sanity-check the numbers**, for example whether subtotals add up to the total or a value is negative where it shouldn't be
- List **items to escalate to accounting or a supervisor**, such as unusual variances or missing data

### Example prompts

- "Reconcile stock: item A shows 500 in the system but we counted 480; item B shows 200, counted 205."
- "Summarise this month's income and expenses in a table before it goes to accounting."
- "Prepare a payroll summary for five staff from the attached hours and overtime."

### What you get

A report stating the period or date and the source of the figures, with a summary table of items, recorded amounts,
actual amounts, variances and notes, followed by a grand total and a list of issues that need further checking.

### Scope and limitations

- **Uses only the figures you provide**; never invents or estimates account balances, taxes or stock levels
- Does not apply tax or social security rates you haven't supplied, and is not a substitute for tax calculations or closing the books with professional accounting judgement
- Missing data and unusual figures are flagged for you to check rather than corrected or closed out
- Have reports reviewed by accounting or a supervisor before official use

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/43-inventory-and-accounting-clerk-report-builder.zip`](../../../dist/43-inventory-and-accounting-clerk-report-builder.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
