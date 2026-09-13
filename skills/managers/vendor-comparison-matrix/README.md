# Vendor Comparison Matrix

**ผู้ช่วยเปรียบเทียบซัพพลายเออร์หลายรายด้วยคะแนนถ่วงน้ำหนัก พร้อมคำแนะนำที่อธิบายเหตุผลได้สำหรับฝ่ายจัดซื้อ**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 1 · ผู้จัดการ (Managers) |
| **Skill ID** | `vendor-comparison-matrix` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

ผู้จัดการฝ่ายจัดซื้อและเจ้าหน้าที่จัดซื้อ ผู้จัดการซัพพลายเชน ผู้จัดการโรงงานหรือฝ่ายปฏิบัติการ
และเจ้าของธุรกิจ SME ที่ต้องเลือกผู้ขาย ผู้ผลิต หรือผู้จำหน่ายอย่างมีหลักเกณฑ์
และต้องทำเอกสารประกอบเพื่อขออนุมัติจากผู้บริหาร

### ทำอะไรได้บ้าง

- จัดข้อมูลจาก **ใบเสนอราคาและข้อเสนอของผู้ขายหลายราย** ให้อยู่ในตารางเดียวกัน
- กำหนด **เกณฑ์เปรียบเทียบและน้ำหนัก** จากฐาน 4 ด้าน (ราคา คุณภาพ เวลาส่งมอบ เงื่อนไขชำระเงิน) และเพิ่มเกณฑ์เสริมตามบริบท
- ให้ **คะแนน 1-5 แบบเทียบสัมพัทธ์** ระหว่างผู้ขาย พร้อมเหตุผลกำกับทุกช่อง
- คำนวณ **คะแนนถ่วงน้ำหนักรวม (weighted score)** แสดงสูตรพร้อมตัวเลขแทนค่า
- วิเคราะห์ **จุดแข็ง-จุดอ่อนและสถานการณ์ที่เหมาะ** ของแต่ละราย แยกจากคะแนนรวม
- สรุป **ผู้ขายหลัก ผู้ขายสำรอง และความเสี่ยงที่ควรเฝ้าระวัง** เช่น การพึ่งพาผู้ขายรายเดียว

### ตัวอย่างคำสั่ง

- "เปรียบเทียบซัพพลายเออร์กล่องบรรจุภัณฑ์ 2 ราย ราย A 8 บาท ส่ง 10 วัน เครดิต 30 วัน ราย B 9.5 บาท ส่ง 5 วัน เครดิต 15 วัน"
- "เทียบราคาจากหลายเจ้าในใบเสนอราคาที่แนบมา แล้วบอกว่าควรเลือกใครดี"
- "ทำตารางประเมินซัพพลายเออร์ประจำปี เพื่อพิจารณาต่อสัญญาหรือเปลี่ยนราย"

### สิ่งที่จะได้รับ

ตารางเปรียบเทียบซัพพลายเออร์ระบุหมวดที่จัดซื้อ วันที่วิเคราะห์ และน้ำหนักเกณฑ์ที่ใช้ ประกอบด้วยตารางคะแนน
พร้อมเหตุผลและคะแนนถ่วงน้ำหนักรวม จุดแข็ง-จุดอ่อนรายซัพพลายเออร์ คำแนะนำผู้ขายหลักและสำรองพร้อมความเสี่ยง
และรายการข้อมูลที่ยังขาดหรือควรตรวจสอบเพิ่มเติม

### ขอบเขตและข้อควรระวัง

- **ไม่สมมติตัวเลขขึ้นเอง** ข้อมูลที่ขาดจะระบุว่า "ไม่มีข้อมูล" อย่างตรงไปตรงมา
- ถ้าไม่ได้กำหนดน้ำหนัก จะใช้ค่าเริ่มต้น ราคา 30% คุณภาพ 30% เวลาส่งมอบ 25% เงื่อนไขชำระเงิน 15% ซึ่งควรปรับตามความสำคัญจริงของธุรกิจ
- ควรตรวจสอบข้อมูลที่ยังขาดตามรายการท้ายรายงานก่อนตัดสินใจจริง

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Purchasing managers and buyers, supply-chain managers, plant or operations managers, and SME owners
who need a fair, structured way to choose between suppliers, manufacturers or distributors, and to
justify the choice to management for approval.

### What it can do

- Put **quotations and offers from several vendors** into one comparison table
- Set **criteria and weights**, starting from four core factors (price, quality, lead time and payment terms) and adding others that fit the context
- Give **relative 1-to-5 scores** across vendors, with a short reason in every cell
- Calculate a **weighted total score**, showing the formula with real numbers plugged in
- Summarise each vendor's **strengths, weaknesses and best-fit situations**, separately from the total score
- Recommend a **primary vendor, a backup and the risks to watch**, such as over-reliance on a single supplier

### Example prompts

- "Compare two packaging box suppliers: A is 8 baht, 10-day delivery, 30-day credit; B is 9.5 baht, 5-day delivery, 15-day credit."
- "Compare prices from the attached quotations and tell me which vendor to choose."
- "Build an annual supplier review table so we can decide whether to renew or switch."

### What you get

A vendor comparison for the purchase category, with the analysis date and weights used. It includes
a scoring table with reasons and weighted totals, strengths and weaknesses for each vendor, a primary
and backup recommendation with risks, and a list of missing information to verify.

### Scope and limitations

- **Never makes up figures**; missing data is plainly marked as "no data"
- If you don't set weights, it uses defaults of price 30%, quality 30%, lead time 25% and payment terms 15%, which you should adjust to your real priorities
- Check the missing items listed at the end of the report before making the final decision

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/vendor-comparison-matrix.zip`](../../../dist/vendor-comparison-matrix.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
