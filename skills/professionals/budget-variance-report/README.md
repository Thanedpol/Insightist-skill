# Budget Variance Report

**ผู้ช่วยทีมการเงินเทียบงบประมาณกับยอดจริง วิเคราะห์สาเหตุ และสรุปข้อเสนอแนะให้ผู้บริหาร**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `budget-variance-report` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักวิเคราะห์การเงิน (financial analyst) นักวิเคราะห์งบประมาณ นักบัญชีบริหาร และผู้ควบคุมการเงิน (financial controller)
ที่ต้องปิดงบและรายงานผลประจำเดือน/ไตรมาส/ปี รวมถึงเจ้าของธุรกิจและหัวหน้าแผนกที่ต้องชี้แจงผลใช้งบต่อผู้บริหารหรือบอร์ด

### ทำอะไรได้บ้าง

- คำนวณ **variance ทั้งจำนวนเงินและเปอร์เซ็นต์** ของทุกหมวดรายการ
- ระบุสถานะ **Favorable / Unfavorable** ให้ถูกต้องตามประเภทรายการ (รายได้กับค่าใช้จ่ายตีความกลับกัน)
- ตั้ง **เกณฑ์นัยสำคัญ (materiality threshold)** ค่าเริ่มต้น ±10% แล้วแยกรายการที่ต้องวิเคราะห์เชิงลึก
- วิเคราะห์ **สาเหตุของ variance** เช่น ราคา/อัตรา ปริมาณ timing รายการครั้งเดียว หรือการตั้งงบผิดตั้งแต่แรก
- **จัดลำดับรายการที่ต้องจับตา** ตามผลกระทบเป็นจำนวนเงิน และแยกความเสี่ยงต่อเนื่องออกจากเหตุการณ์ครั้งเดียว
- สรุป **ข้อเสนอแนะเชิงบริหาร** ที่ลงมือได้จริง เช่น ปรับงบงวดถัดไป ขออนุมัติเพิ่ม หรือตั้งมาตรการคุมต้นทุน
- เปรียบเทียบผลงบระหว่างหลายแผนก หลายโครงการ หรือหลายสาขา

### ตัวอย่างคำสั่ง

- "ช่วยทำ budget vs actual ของแผนกการตลาดเดือนสิงหาคม"
- "ทำไมค่าใช้จ่ายไตรมาสนี้เกินงบ วิเคราะห์ผลต่างงบประมาณให้หน่อย"
- "สรุปรายงานเปรียบเทียบงบประมาณประจำเดือนจากไฟล์นี้ให้ผู้บริหาร"

### สิ่งที่จะได้รับ

รายงาน variance ที่ระบุหน่วยงาน งวด และเกณฑ์นัยสำคัญที่ใช้ ตามด้วยสรุปภาพรวม (งบรวม ยอดจริงรวม ผลต่างรวม)
ตารางรายละเอียดทุกหมวดพร้อมสถานะ F/U รายการที่ต้องจับตาพร้อมสาเหตุที่เป็นไปได้และผลกระทบ
และปิดท้ายด้วยข้อเสนอแนะเชิงบริหาร

### ขอบเขตและข้อควรระวัง

- ถ้าข้อมูลไม่พอยืนยันสาเหตุ จะเสนอเป็น **สมมติฐาน** พร้อมบอกว่าควรถามใครหรือดูข้อมูลอะไรเพิ่ม
- ต้องให้ **หน่วยเงินและช่วงเวลาตรงกัน** ก่อนเทียบ เช่น ไม่เอางบรายปีไปเทียบกับยอดจริงสะสม 3 เดือนโดยไม่ปรับสัดส่วน
- ความแม่นยำขึ้นกับข้อมูลที่ให้มา ควรตรวจตัวเลขกับระบบบัญชีก่อนนำเสนอ

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Financial analysts, budget analysts, management accountants and financial controllers who close the books
and report monthly, quarterly or annual results, plus business owners and department heads who have to
explain budget performance to management or the board.

### What it can do

- Calculate **variance in both amount and percentage** for every line item
- Label each line **Favorable or Unfavorable** correctly by type, since revenue and expenses read in opposite directions
- Apply a **materiality threshold** (±10% by default) and pull out the items that need a deeper look
- Analyse **causes of variance**: price/rate, volume, timing, one-off items or a planning error
- **Rank watch-list items** by money impact and separate recurring risks from one-time events
- Write **actionable management recommendations**, such as adjusting next period's budget, seeking extra approval or tightening cost controls
- Compare budget results across departments, projects or branches

### Example prompts

- "Do a budget vs actual for the marketing department for August."
- "Why are we over budget this quarter? Analyse the variance."
- "Summarise this month's budget comparison file into a report for management."

### What you get

A variance report stating the unit, period and threshold used, followed by an overview (total budget,
total actual, total variance), a detailed table of every line with F/U status, a watch list with likely
causes and impact, and a closing set of management recommendations.

### Scope and limitations

- When the data can't confirm a cause, it's presented as a **hypothesis**, with suggestions on who to ask or what to check
- **Currency units and time periods must match** before comparing; an annual budget isn't compared with three months of actuals without pro-rating
- Results are only as accurate as the input data; check figures against your accounting system before presenting

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/budget-variance-report.zip`](../../../dist/budget-variance-report.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
