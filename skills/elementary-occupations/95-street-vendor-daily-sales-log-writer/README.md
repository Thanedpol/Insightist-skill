# Street Vendor Daily Sales Log Writer

**ผู้ช่วยจดบันทึกยอดขาย เงินเข้า-เงินออก และของที่ต้องซื้อเพิ่มแบบง่ายๆ สำหรับพ่อค้าแม่ค้าริมถนน**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 9 · ผู้ประกอบอาชีพงานพื้นฐาน (Elementary Occupations) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 95 · ผู้ขายสินค้าและให้บริการตามถนนและที่เกี่ยวข้อง (Street and Related Sales and Service Workers) |
| **Skill ID** | `95-street-vendor-daily-sales-log-writer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

คนขายของริมถนน คนขายอาหารข้างทางและรถเข็น คนขัดรองเท้า คนล้างกระจกรถตามสี่แยก และคนวิ่งงานตามถนน
รวมถึงพ่อค้าแม่ค้ารายย่อยที่ไม่ถนัดบัญชีแต่อยากเริ่มจดรายรับ-รายจ่ายประจำวันให้เป็นนิสัย
(หมายเหตุ: ISCO-08 จัดคนขายอาหารข้างทางไว้ที่ 5212 ในหมวด 52 แต่สมุดบันทึกนี้ใช้ได้เหมือนกัน)

### ทำอะไรได้บ้าง

- จด **ของหรือบริการที่ขายได้วันนี้** พร้อมจำนวนและราคาต่อหน่วย
- คำนวณ **ยอดขายต่อรายการและยอดขายรวมของวัน** โดยแสดงวิธีคูณ/บวกให้เห็นชัด
- จด **เงินที่จ่ายออกระหว่างวัน** เช่น ซื้อของเพิ่ม ค่าน้ำแข็ง ค่าน้ำมัน ค่าที่จอด
- สรุป **เงินเหลือปลายวัน** ด้วยการเอายอดขายลบยอดจ่าย อธิบายเป็นคำพูดง่ายๆ
- ทำ **รายการเตือนของที่ใกล้หมด** ที่ต้องซื้อเพิ่มพรุ่งนี้
- จัดเป็น **สมุดบันทึก 1 หน้าต่อวัน** ใช้คำง่าย ไม่มีศัพท์บัญชี เขียนตามด้วยมือได้

### ตัวอย่างคำสั่ง

- "ช่วยจดบันทึกยอดขายวันนี้ ขายส้มตำ 15 ถุง ถุงละ 40 บาท ไก่ย่าง 5 ตัว ตัวละ 100 บาท จ่ายค่าวัตถุดิบ 300 ค่ารถเข็น 50"
- "ทำสมุดรายรับรายจ่ายพ่อค้าแม่ค้าแบบง่ายๆ ให้หน่อย"
- "จดเงินเข้าเงินออกรถเข็นน้ำแข็งใสวันนี้"

### สิ่งที่จะได้รับ

บันทึกยอดขายประจำวันแผ่นเดียว 4 ส่วน — (1) ขายอะไรได้บ้างพร้อมยอดรวม (2) จ่ายอะไรไปบ้างพร้อมยอดรวม
(3) เงินเหลือวันนี้ (ยอดขาย − ยอดจ่าย) (4) ของที่ต้องซื้อเพิ่มพรุ่งนี้

### ขอบเขตและข้อควรระวัง

- เน้น **บันทึกยอดขายและรายจ่ายเท่านั้น ไม่แนะนำการลงทุนหรือการกู้ยืมเงินใดๆ**
- ตัวเลขทุกบรรทัดต้องคำนวณถูกและแสดงวิธีคิด ควรตรวจกับเงินจริงในมืออีกครั้ง
- ถ้าผู้ใช้ไม่ได้บอกว่าของอะไรใกล้หมด จะถามก่อน ไม่เดาเอง
- ใช้ตัวเลขกลมๆ ไม่ละเอียดถึงสตางค์

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Street vendors, roadside food and cart sellers, shoe shiners, windscreen washers at intersections
and street errand runners, plus any small trader who is not comfortable with bookkeeping but wants
to start a simple daily habit of recording money in and out. (Note: ISCO-08 classifies street food
sellers under 5212 in group 52, but the log works just as well for them.)

### What it can do

- Record **the goods or services sold today** with quantities and unit prices
- Calculate **sales per item and the day's total**, showing the multiplication and addition clearly
- Record **money spent during the day**, such as restocking, ice, fuel or parking fees
- Work out **cash left at the end of the day** as total sales minus total spending, in plain words
- List **items running low** that need buying tomorrow
- Lay it out as a **one-page-per-day log** in plain words with no accounting jargon, easy to copy by hand

### Example prompts

- "Log today's sales: 15 bags of papaya salad at 40 baht, 5 grilled chickens at 100 baht. I spent 300 on ingredients and 50 on cart rental."
- "Make me a simple income and expense notebook for a market trader."
- "Record money in and out for my shaved-ice cart today."

### What you get

A one-page daily sales log in four sections: (1) what was sold, with a total, (2) what was spent,
with a total, (3) money left today (sales minus spending), and (4) items to buy tomorrow.

### Scope and limitations

- **Records sales and expenses only; gives no investment or borrowing advice**
- Every figure must be calculated correctly with the working shown; check it against the cash in hand
- If you don't say which items are running low, it asks rather than guessing
- Uses round numbers, not satang-level detail

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/95-street-vendor-daily-sales-log-writer.zip`](../../../dist/95-street-vendor-daily-sales-log-writer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
