# Financial Ratio Analyzer

**ผู้ช่วยวิเคราะห์งบการเงินด้วยอัตราส่วนหลัก 4 กลุ่ม แล้วแปลผลให้คนที่ไม่ใช่นักบัญชีเข้าใจได้ทันที**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `financial-ratio-analyzer` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักวิเคราะห์การเงิน (financial analyst) นักบัญชี และนักวิเคราะห์สินเชื่อ (credit analyst)
ที่ต้องสรุปสุขภาพการเงินของกิจการให้ผู้บริหาร บอร์ด หรือนักลงทุนที่ไม่ใช่สายบัญชีอ่าน
รวมถึงเจ้าของกิจการและผู้บริหารที่ต้องใช้ข้อมูลประกอบการตัดสินใจ เช่น ก่อนขอสินเชื่อหรือระดมทุน

### ทำอะไรได้บ้าง

- ดึงตัวเลขสำคัญจาก **งบดุล งบกำไรขาดทุน และงบกระแสเงินสด** (PDF, Excel หรือพิมพ์มาตรงๆ)
- คำนวณ **สภาพคล่อง (liquidity)**: Current Ratio, Quick Ratio, Cash Ratio
- คำนวณ **ความสามารถทำกำไร (profitability)**: Gross/Operating/Net Margin, ROA, ROE
- คำนวณ **โครงสร้างหนี้ (leverage)**: D/E Ratio, Debt Ratio, Interest Coverage
- คำนวณ **ประสิทธิภาพ (efficiency)**: Inventory/Receivables Turnover, DIO, DSO, DPO, Cash Conversion Cycle, Asset Turnover
- ทำ **ตาราง trend** เมื่อมีงบหลายปีหรือหลายไตรมาส พร้อมทิศทางดีขึ้น/แย่ลง
- **แปลผลเป็นภาษาธุรกิจ** และสรุปจุดแข็ง จุดที่ต้องระวัง และประเด็นที่ควรติดตาม

### ตัวอย่างคำสั่ง

- "ช่วยวิเคราะห์งบการเงินปี 2568 ของบริษัทนี้ให้หน่อย"
- "บริษัทนี้การเงินแข็งแรงไหม สภาพคล่องเป็นยังไง หนี้สินเยอะไปไหม"
- "คำนวณ ROE ROA จากงบดุลและงบกำไรขาดทุน 3 ปีย้อนหลังนี้"

### สิ่งที่จะได้รับ

รายงานวิเคราะห์อัตราส่วนทางการเงิน 6 ส่วน — (1) สภาพคล่อง (2) ความสามารถทำกำไร
(3) โครงสร้างหนี้ (4) ประสิทธิภาพ (5) แนวโน้มย้อนหลังถ้ามีข้อมูลหลายงวด
(6) สรุปผู้บริหาร — ทุกอัตราส่วนแสดงค่าพร้อมคำแปลผลสั้นๆ

### ขอบเขตและข้อควรระวัง

- **ไม่ให้คำแนะนำการลงทุนส่วนบุคคล** เช่น ควรซื้อหุ้นนี้ไหม เน้นสรุปสุขภาพการเงินเท่านั้น
- ถ้าข้อมูลไม่ครบ จะ **ระบุว่าอัตราส่วนใดคำนวณไม่ได้** แทนการเดาตัวเลข
- แสดงสูตรและตัวเลขที่ใช้ให้ตรวจสอบย้อนกลับได้ เกณฑ์ที่ใช้เป็นเกณฑ์ทั่วไปและขึ้นกับอุตสาหกรรม

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Financial analysts, accountants and credit analysts who need to summarise a company's financial health for
executives, boards or investors without an accounting background, plus business owners and managers using
the numbers to make decisions, such as before taking on a loan or raising capital.

### What it can do

- Pull key figures from the **balance sheet, income statement and cash flow statement** (PDF, spreadsheet or typed in)
- Calculate **liquidity**: current ratio, quick ratio, cash ratio
- Calculate **profitability**: gross, operating and net margin, ROA, ROE
- Calculate **leverage**: debt-to-equity, debt ratio, interest coverage
- Calculate **efficiency**: inventory and receivables turnover, DIO, DSO, DPO, cash conversion cycle, asset turnover
- Build a **trend table** when several years or quarters are available, showing whether each area is improving or declining
- **Explain results in plain business language** and summarise strengths, concerns and points to monitor

### Example prompts

- "Analyse this company's 2025 financial statements."
- "Is this company financially healthy? How's its liquidity? Is it carrying too much debt?"
- "Calculate ROE and ROA from these three years of balance sheets and income statements."

### What you get

A financial ratio report in six parts: (1) liquidity, (2) profitability, (3) leverage, (4) efficiency,
(5) historical trend when multiple periods are provided, and (6) an executive summary. Every ratio comes
with its value and a short plain-language reading.

### Scope and limitations

- **No personal investment advice**, such as whether to buy a stock; the focus is on financial health only
- When inputs are missing, it **states which ratios can't be calculated** rather than guessing figures
- Formulas and inputs are shown so results can be traced; benchmarks are general rules of thumb and vary by industry

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/financial-ratio-analyzer.zip`](../../../dist/financial-ratio-analyzer.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
