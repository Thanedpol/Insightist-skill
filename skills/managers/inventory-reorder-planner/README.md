# Inventory Reorder Planner

**ผู้ช่วยคำนวณจุดสั่งซื้อซ้ำ safety stock และปริมาณสั่งซื้อที่เหมาะสมสำหรับฝ่ายจัดซื้อ คลังสินค้า และเจ้าของ SME**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 1 · ผู้จัดการ (Managers) |
| **Skill ID** | `inventory-reorder-planner` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

ผู้จัดการฝ่ายจัดซื้อและเจ้าหน้าที่จัดซื้อ ผู้จัดการคลังสินค้า ผู้จัดการซัพพลายเชน ผู้จัดการร้านค้าปลีก
และเจ้าของธุรกิจ SME ที่ต้องตัดสินใจว่าจะสั่งสินค้าเข้าเมื่อไหร่และสั่งครั้งละเท่าไหร่
โดยไม่ให้สต็อกขาดหรือสต็อกจมทุน

### ทำอะไรได้บ้าง

- คำนวณ **ยอดขายเฉลี่ยต่อวัน (ADU)** จากข้อมูลยอดขายหรือการเบิกใช้ย้อนหลัง
- คำนวณ **safety stock** ตามระดับการบริการที่ต้องการ (ค่าเริ่มต้น 95%) หรือใช้สูตรประมาณเมื่อไม่มีค่า SD
- หา **จุดสั่งซื้อซ้ำ (Reorder Point)** ว่าสต็อกเหลือเท่าไหร่ต้องสั่งทันที
- คำนวณ **ปริมาณสั่งซื้อที่เหมาะสม** ด้วยสูตร EOQ เมื่อมีข้อมูลต้นทุน หรือตามรอบสั่งซื้อเมื่อไม่มี
- ประเมิน **ความเร่งด่วนรายสินค้า** ว่าต้องสั่งทันที ต้องจับตา หรือยังปลอดภัย และเหลืออีกกี่วันก่อนถึงจุดสั่งซื้อ
- จัดทำ **ตารางสรุปหลาย SKU** เรียงตามความเร่งด่วน พร้อม action ที่ทำได้ทันที

### ตัวอย่างคำสั่ง

- "น้ำยาล้างจานขายวันละ 12 ขวด เหลือ 150 ขวด lead time 7 วัน ควรสั่งของตอนไหน สั่งเท่าไหร่ดี"
- "ช่วยคำนวณ reorder point กับ safety stock ของสินค้า 10 SKU ในไฟล์นี้"
- "ของจะหมดเมื่อไหร่ สั่งตอนนี้ทันไหม ถ้าซัพพลายเออร์ส่งช้า 14 วัน"

### สิ่งที่จะได้รับ

แผนสั่งซื้อสต็อกที่มีสรุปสำหรับผู้บริหาร (จำนวน SKU ที่ต้องสั่งทันที ที่ต้องจับตาภายใน 7 วัน และสมมติฐานที่ใช้)
ตารางแผนสั่งซื้อรายสินค้าพร้อมสถานะ รายละเอียดการคำนวณแบบแทนค่าตัวเลขสำหรับ SKU ที่ต้องสั่งทันที
และคำแนะนำเชิงปฏิบัติ

### ขอบเขตและข้อควรระวัง

- เมื่อข้อมูลไม่ครบ จะ **ตั้งสมมติฐานและระบุไว้ชัดเจน** เช่น Z-score หรือรอบสั่งซื้อ ควรตรวจทานก่อนใช้จริง
- ผลลัพธ์แม่นยำเท่ากับข้อมูลที่ใส่ ควร **ทบทวนตัวเลขซ้ำ** เมื่อยอดขายผันผวนสูงหรือเป็นสินค้าตามฤดูกาล
- ควรยืนยัน lead time กับซัพพลายเออร์อีกครั้ง โดยเฉพาะช่วงเทศกาล

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Purchasing managers and buyers, warehouse managers, supply-chain managers, retail store managers and
SME owners who need to decide when to reorder stock and how much to order, without running out or
tying up cash in excess inventory.

### What it can do

- Work out **average daily usage (ADU)** from past sales or consumption data
- Calculate **safety stock** for a target service level (95% by default), or with a simple estimate when no standard deviation is available
- Find the **reorder point**: the stock level at which you must order right away
- Calculate the **right order quantity**, using EOQ when cost data is available or an order-cycle method when it isn't
- Rate **urgency per item** (order now, watch, or safe) and how many days remain before the reorder point
- Produce a **multi-SKU summary table** sorted by urgency, with clear next actions

### Example prompts

- "Dish soap sells 12 bottles a day, 150 in stock, 7-day lead time. When should I reorder and how many?"
- "Calculate the reorder point and safety stock for the 10 SKUs in this file."
- "When will we run out, and is it too late to order if the supplier takes 14 days?"

### What you get

A stock reorder plan with an executive summary (SKUs to order now, SKUs to watch within seven days,
and the assumptions used), a per-item reorder table with status, step-by-step worked calculations
for every item that needs ordering now, and practical recommendations.

### Scope and limitations

- Where data is missing, it **makes and clearly labels assumptions**, such as the Z-score or order cycle; review them before acting
- Results are only as good as the input data, so **recheck the numbers** for volatile or seasonal products
- Confirm lead times with suppliers, especially around holidays and festivals

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/inventory-reorder-planner.zip`](../../../dist/inventory-reorder-planner.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
