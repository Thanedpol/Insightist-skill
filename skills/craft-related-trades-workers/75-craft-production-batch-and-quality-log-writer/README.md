# Craft Production Batch and Quality Log Writer

**ผู้ช่วยเขียนบันทึกการผลิตแบบล็อตพร้อมจุดตรวจคุณภาพและความปลอดภัย สำหรับช่างแปรรูปอาหาร งานไม้ งานตัดเย็บ และงานฝีมืออื่นๆ**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 7 · ช่างฝีมือและผู้ปฏิบัติงานที่เกี่ยวข้อง (Craft and Related Trades Workers) |
| **หมวดย่อย ISCO-08 / Sub-major group** | 75 · ช่างแปรรูปอาหาร งานไม้ เครื่องนุ่งห่ม และช่างฝีมืออื่นๆ (Food Processing, Wood Working, Garment and Other Craft and Related Trades Workers) |
| **Skill ID** | `75-craft-production-batch-and-quality-log-writer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

คนทำขนมปัง ผู้ผลิตแฮม/ชีส คนชำแหละเนื้อ ผู้ตัดเย็บเสื้อผ้า ช่างฟอกหนัง ช่างทำรองเท้า และช่างเลื่อยไม้
ที่ผลิตงานเป็นล็อตในร้านเบเกอรี่ โรงงานแปรรูปอาหารขนาดเล็ก หรือเวิร์กช็อปงานฝีมือ

### ทำอะไรได้บ้าง

- บันทึก **ข้อมูลตั้งต้นของล็อต** ได้แก่ หมายเลขล็อต วันที่ผลิต กะ/ผู้รับผิดชอบ และประเภทผลิตภัณฑ์
- ลิสต์ **วัตถุดิบ/วัสดุที่ใช้จริง** พร้อมปริมาณ แหล่งที่มา เลขล็อตวัตถุดิบต้นทาง และวันหมดอายุ (สำหรับอาหาร)
- สรุป **ขั้นตอนการผลิตพร้อมค่าที่ควบคุม** เช่น อุณหภูมิและเวลาอบ/หมัก ขนาดตัดและระยะตะเข็บ ความชื้นไม้และขนาดเลื่อย
- กำหนด **จุดตรวจคุณภาพ 2-3 จุด** (ต้นทาง/กลางกระบวนการ/ก่อนบรรจุหรือส่งมอบ) พร้อมเกณฑ์และผลตรวจจริง
- ทำ **จุดตรวจเฉพาะประเภทงาน** เช่น อุณหภูมิเก็บรักษา ความสะอาด การปนเปื้อนข้าม สำหรับอาหาร หรือความแข็งแรงของตะเข็บ/รอยต่อและตำหนิผิวงาน สำหรับงานตัดเย็บและงานไม้
- สรุป **ผลผลิตเทียบเป้าหมาย ของเสียและสาเหตุ** พร้อมข้อเสนอปรับปรุงสำหรับล็อตถัดไป

### ตัวอย่างคำสั่ง

- "ทำบันทึกการผลิตล็อตขนมปังฝรั่งเศส ใช้แป้ง 20 กก. ตั้งเป้า 200 ก้อน"
- "ช่วยตรวจคุณภาพงานตัดเย็บเสื้อเชิ้ตรอบตัดนี้ 150 ตัว และบันทึกของเสีย"
- "ทำ log การเลื่อยไม้ บันทึกปริมาณไม้เข้า-ออกและอัตราการสูญเสียเนื้อไม้"

### สิ่งที่จะได้รับ

บันทึกการผลิตล็อตที่มีหมายเลขล็อต วันที่ผลิต ผู้รับผิดชอบ และผลิตภัณฑ์ แบ่งเป็น 6 ส่วน ได้แก่ (1) วัตถุดิบ/วัสดุที่ใช้
(2) ขั้นตอนการผลิตหลัก (3) จุดตรวจคุณภาพ (4) จุดตรวจความปลอดภัย/คุณภาพเฉพาะทาง (5) สรุปผลผลิตและของเสีย
และ (6) ข้อเสนอปรับปรุงล็อตถัดไป

### ขอบเขตและข้อควรระวัง

- **ไม่กุตัวเลขปริมาณวัตถุดิบ อุณหภูมิ หรือผลตรวจที่ไม่มีข้อมูลรองรับ** จะระบุว่าต้องบันทึกจากหน้างานจริง
- ผลตรวจคุณภาพต้องเป็นผลตรวจจริง ไม่ใช่แค่คำว่า "ผ่าน" ลอยๆ
- เกณฑ์ตรวจต้องเหมาะกับประเภทงานนั้นจริง ไม่ใช้เกณฑ์เดียวกันทุกงาน
- รายงานของเสียและปัญหาอย่างตรงไปตรงมา และข้อเสนอปรับปรุงต้องเชื่อมโยงกับปัญหาที่พบจริงในล็อตนั้น

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Bakers, ham and cheese makers, butchers, garment makers and tailors, tanners, shoemakers and sawmill workers
who produce in batches in bakeries, small food processing plants or craft workshops.

### What it can do

- Record **batch header details**: lot number, production date, shift or person in charge, and product
- List the **raw materials actually used** with quantities, sources, supplier lot numbers and expiry dates (for food)
- Summarise **production steps with controlled parameters**, such as proofing and baking temperature and time, cut sizes and seam allowances, or wood moisture and saw settings
- Set **two or three quality checkpoints** (incoming, mid-process, before packing or delivery) with criteria and actual results
- Add **job-specific checks**: storage temperature, hygiene and cross-contamination for food, or seam and joint strength and surface defects for garments and woodwork
- Summarise **output against target, rejects and their causes**, with improvements for the next batch

### Example prompts

- "Make a batch log for French bread using 20 kg of flour, targeting 200 loaves."
- "Help me log quality checks and rejects for this cutting run of 150 shirts."
- "Create a sawmill log tracking timber in and out and the wood loss rate."

### What you get

A batch production log with lot number, production date, person in charge and product, in six parts: (1) materials used,
(2) main production steps, (3) quality checkpoints, (4) job-specific safety or quality checks, (5) output and rejects,
and (6) improvements for the next batch.

### Scope and limitations

- **Never invents material quantities, temperatures or test results** without supporting data; these are marked to be recorded on site
- Quality checks must show actual results, not just "pass"
- Check criteria must fit the type of work rather than one standard for everything
- Rejects and problems are reported honestly, and improvement suggestions must tie back to issues found in that batch

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/75-craft-production-batch-and-quality-log-writer.zip`](../../../dist/75-craft-production-batch-and-quality-log-writer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
