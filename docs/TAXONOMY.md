# Taxonomy & Roadmap

> 🗺️ อยากดูแบบลากโหนดเล่น/ขยายหมวดย่อยได้จริง เปิด **[Insightist Skill Map](https://claude.ai/code/artifact/df4a05d9-4ba8-4ae8-8c89-0e2bf51677af)**
> — มีมุมมองตารางสลับดูได้ในหน้าเดียวกัน

เอกสารนี้อธิบายกรอบการจัดหมวดหมู่ (taxonomy) ของ Insightist Skills Library ที่ใช้อยู่ตอนนี้
และแนวทางขยายต่อในระดับที่ละเอียดขึ้น

## แนวคิด: ยึดมาตรฐานสากล ไม่ตั้งหมวดเอง

รอบแรกของโปรเจกต์นี้ตั้งหมวดหมู่เอง 8 หมวด (กลยุทธ์ การเงิน การตลาด ฯลฯ) ซึ่งครอบคลุมแค่งานออฟฟิศ/knowledge
work เป็นหลัก ยังไม่ครอบคลุม "ทุกสายอาชีพ" ตามเป้าหมายเดิม

รอบนี้เปลี่ยนมาใช้ **ISCO-08 (International Standard Classification of Occupations)** ซึ่งเป็นมาตรฐาน
การจัดประเภทอาชีพขององค์การแรงงานระหว่างประเทศ (ILO) ที่สำนักงานสถิติแห่งชาติของไทยก็ใช้อ้างอิงเช่นกัน
เหตุผลที่เปลี่ยน:

1. **ครอบคลุมจริง** — ISCO-08 แบ่งอาชีพทั้งหมดเป็น 10 หมวดใหญ่ (Major groups) และ 43 หมวดย่อย
   (Sub-major groups) ซึ่งครอบคลุมกำลังแรงงานได้ครบทุกอุตสาหกรรม ตั้งแต่ผู้บริหารระดับสูงไปจนถึงงานพื้นฐาน
2. **มีข้อมูลจริงรองรับ** — เทียบกับข้อมูลผู้มีงานทำจริงในไทยจากสำนักงานสถิติแห่งชาติ (สสช.) ไตรมาส 3/2568
   (39,852,121 คน) ทำให้รู้ว่าแต่ละหมวดมีคนทำงานอยู่จริงกี่คน ไม่ใช่หมวดที่นั่งเทียนตั้งเอง
3. **เทียบข้ามแพลตฟอร์ม/ประเทศได้** — เพราะเป็นมาตรฐานสากล ไม่ใช่หมวดเฉพาะของ Insightist™

## โครงสร้าง 4 ระดับของ ISCO-08

ISCO-08 ซ้อนกัน 4 ระดับ: **หมวดใหญ่ (10)** → **หมวดย่อย/Sub-major groups (43)** → **หมู่/Minor groups (130)**
→ **หน่วยอาชีพ/Unit groups (436)** — คลังนี้สร้าง 1 skill ต่อ 1 หมวดย่อย (sub-major group) ก่อน
เพื่อให้ครอบคลุมกว้างครบทุกสายอาชีพในรอบเดียว ส่วนการเจาะลึกลงหมู่/หน่วยอาชีพ (130/436) เป็นเฟสขยายต่อ

## หมวดใหญ่ทั้ง 10 (พร้อมข้อมูลผู้มีงานทำจริงในไทย)

| # | หมวดใหญ่ | โฟลเดอร์ | หมวดย่อย | ผู้มีงานทำในไทย | % |
|---|---|---|---|---|---|
| 1 | ผู้จัดการ · Managers | `skills/managers/` | 4 | 1,365,359 | 3.43% |
| 2 | ผู้ประกอบวิชาชีพด้านต่างๆ · Professionals | `skills/professionals/` | 6 | 2,200,878 | 5.52% |
| 3 | เจ้าหน้าที่เทคนิคและผู้ประกอบวิชาชีพที่เกี่ยวข้อง · Technicians and Associate Professionals | `skills/technicians-associate-professionals/` | 5 | 1,847,079 | 4.63% |
| 4 | เสมียน/งานธุรการสนับสนุน · Clerical Support Workers | `skills/clerical-support-workers/` | 4 | 1,797,391 | 4.51% |
| 5 | พนักงานบริการและผู้จำหน่ายสินค้า · Service and Sales Workers | `skills/service-sales-workers/` | 4 | 8,509,785 | 21.35% |
| 6 | ผู้ปฏิบัติงานมีฝีมือด้านเกษตร ป่าไม้ ประมง · Skilled Agricultural, Forestry and Fishery Workers | `skills/skilled-agricultural-forestry-fishery-workers/` | 3 | 10,919,064 | 27.40% |
| 7 | ช่างฝีมือและผู้ปฏิบัติงานที่เกี่ยวข้อง · Craft and Related Trades Workers | `skills/craft-related-trades-workers/` | 5 | 4,010,828 | 10.06% |
| 8 | ผู้ควบคุมเครื่องจักรและผู้ประกอบชิ้นงาน · Plant and Machine Operators, and Assemblers | `skills/plant-machine-operators-assemblers/` | 3 | 4,375,624 | 10.98% |
| 9 | ผู้ประกอบอาชีพงานพื้นฐาน · Elementary Occupations | `skills/elementary-occupations/` | 6 | 4,697,589 | 11.79% |
| 0 | ทหาร · Armed Forces Occupations | `skills/armed-forces-occupations/` | 3 | สสช. ไม่รายงานแยกเป็นหมวด | — |
| — | คนงานซึ่งมิได้จำแนกไว้ในหมวดอื่น (ตาม สสช.) | — | — | 128,524 | 0.32% |
| — | รวม | | **43** | 39,852,121 | 100% |

หมวด 6 (เกษตร/ป่าไม้/ประมง) ใหญ่ที่สุดในไทยที่ 27.40% ตามด้วยหมวด 5 (บริการ/ขาย) 21.35% — สองหมวดนี้
รวมกันเกินครึ่งของกำลังแรงงานไทยทั้งหมด ขณะที่หมวด "ผู้ประกอบวิชาชีพ" ซึ่งมีหน่วยอาชีพย่อยเยอะที่สุดในมาตรฐาน (92
หน่วย) กลับมีคนทำงานจริงแค่ 5.52% — ภาพนี้เป็นเหตุผลที่คลังนี้ตั้งใจสร้าง skill ให้ครบทุกหมวดใหญ่ ไม่ใช่เอียงไปทาง
งานออฟฟิศอย่างเดียวเหมือนรอบแรก

## 43 หมวดย่อย — ครบทุกตัว (พร้อม skill ที่สร้างแล้ว)

แต่ละหมวดย่อยมี 1 skill หลักที่ช่วยงานเอกสาร/กระบวนการที่คนกลุ่มนั้นทำจริง ยกตัวอย่างอาชีพจริงในหมวดนั้น
ต่อท้ายชื่อ skill ในวงเล็บ

**1 · Managers** — `11-executive-strategic-memo-writer` (CEO, ผู้บริหารระดับสูง, ข้าราชการอาวุโส) ·
`12-department-management-report-builder` (ผจก.การเงิน/HR/การตลาด) ·
`13-operations-manager-sop-and-kpi-builder` (ผจก.โรงงาน/รพ./ร.ร.) ·
`14-hospitality-retail-shift-and-service-planner` (ผจก.โรงแรม/ร้านอาหาร/ค้าปลีก)

**2 · Professionals** — `21-engineering-technical-report-writer` (วิศวกร, สถาปนิก) ·
`22-patient-education-material-writer` (แพทย์, พยาบาลวิชาชีพ, เภสัชกร) ·
`23-lesson-and-curriculum-designer` (อาจารย์, ครู) ·
`24-business-analysis-memo-writer` (นักบัญชี, นักวิเคราะห์การลงทุน, นักการตลาด) ·
`25-technical-documentation-and-code-review-assistant` (นักพัฒนาซอฟต์แวร์, ผู้เชี่ยวชาญไซเบอร์) ·
`26-legal-social-cultural-brief-writer` (ทนายความ, นักสังคมสงเคราะห์, นักข่าว, ศิลปิน)

**3 · Technicians and Associate Professionals** — `31-field-technician-inspection-report-writer`
(ช่างเทคนิคโยธา/ไฟฟ้า, นักบิน) · `32-clinical-support-documentation-assistant` (นักเทคนิคการแพทย์,
พยาบาลเทคนิค) · `33-insurance-and-brokerage-proposal-writer` (ตัวแทนประกัน, เจ้าหน้าที่สินเชื่อ) ·
`34-paralegal-and-social-work-case-note-writer` (ผู้ช่วยทนายความ, เชฟ, โค้ช) ·
`35-it-support-ticket-and-troubleshooting-log-writer` (IT Support, ช่างเทคนิคเครือข่าย)

**4 · Clerical Support Workers** — `41-office-correspondence-and-data-entry-assistant`
(เลขานุการ, พนักงานคีย์ข้อมูล) · `42-customer-service-call-script-and-response-writer`
(พนักงานคอลเซ็นเตอร์, พนักงานเคาน์เตอร์ธนาคาร) · `43-inventory-and-accounting-clerk-report-builder`
(เสมียนบัญชี, พนักงานคลังสินค้า) · `44-mailroom-and-records-management-assistant` (พนักงานคัดแยก/นำจ่ายไปรษณีย์,
เสมียนแฟ้มเอกสาร)

**5 · Service and Sales Workers** — `51-hospitality-personal-service-standard-writer`
(พนักงานเสิร์ฟ, มัคคุเทศก์, ช่างเสริมสวย) · `52-retail-sales-script-and-upsell-planner`
(พนักงานขายหน้าร้าน, เทเลเซลส์) · `53-caregiving-daily-care-plan-writer` (พี่เลี้ยงเด็ก,
ผู้ดูแลผู้สูงอายุ) · `54-security-incident-report-writer` (ตำรวจ, รปภ., พนักงานดับเพลิง)

**6 · Skilled Agricultural, Forestry and Fishery Workers** — `61-crop-and-livestock-farm-plan-writer`
(ชาวนา, ชาวสวนยาง, ผู้เลี้ยงไก่/สุกร) · `62-fishery-and-forestry-operation-log-writer`
(ชาวประมง, ผู้เพาะเลี้ยงกุ้ง/ปลา) · `63-subsistence-farming-household-planning-assistant`
(เกษตรกรรายย่อยยังชีพ, ผู้เก็บของป่า)

**7 · Craft and Related Trades Workers** — `71-construction-trade-job-quote-and-checklist-writer`
(ช่างก่ออิฐ, ช่างปูน, ช่างไม้) · `72-machine-repair-service-report-writer` (ช่างเชื่อม, ช่างซ่อมรถยนต์) ·
`73-handicraft-and-print-shop-order-spec-writer` (ช่างทอผ้า, ช่างทำเครื่องประดับ) ·
`74-electrical-installation-job-checklist-writer` (ช่างไฟฟ้าอาคาร, ช่างติดตั้งไฟเบอร์) ·
`75-craft-production-batch-and-quality-log-writer` (คนทำขนมปัง, ผู้ตัดเย็บเสื้อผ้า)

**8 · Plant and Machine Operators, and Assemblers** — `81-plant-operator-shift-log-and-maintenance-writer`
(ผู้ควบคุมเครื่องจักรโรงงาน) · `82-assembly-line-quality-checklist-writer` (พนักงานประกอบชิ้นส่วนยานยนต์) ·
`83-driver-trip-log-and-safety-checklist-writer` (คนขับรถบรรทุก/แท็กซี่, ไรเดอร์ส่งของ)

**9 · Elementary Occupations** — `91-cleaning-service-schedule-and-checklist-writer` (แม่บ้าน,
พนักงานทำความสะอาด) · `92-farm-labour-daily-task-assignment-writer` (คนงานรับจ้างเกษตร) ·
`93-labour-crew-daily-safety-briefing-writer` (กรรมกรก่อสร้าง, คนงานโรงงาน) ·
`94-kitchen-prep-and-food-safety-checklist-writer` (ผู้ช่วยในครัว) · `95-street-vendor-daily-sales-log-writer`
(คนขายของริมถนนที่ไม่ใช่อาหาร — ถ้าขายอาหารข้างทาง ISCO-08 จัดไว้ที่ 5212 ในหมวด 52) · `96-waste-collection-route-and-log-writer` (พนักงานเก็บขยะ, ซาเล้ง)

**0 · Armed Forces Occupations** — `01-military-officer-operations-briefing-writer` (นายทหารสัญญาบัตร) ·
`02-nco-unit-training-schedule-writer` (นายสิบ, จ่า) · `03-enlisted-personnel-daily-duty-roster-writer`
(พลทหาร) — 3 skill นี้จำกัดเฉพาะงานเอกสารธุรการ/บริหารกำลังพลทั่วไปเท่านั้น ไม่แตะเนื้อหาเชิงยุทธวิธีหรือข้อมูลลับ

## หมวดที่มาจากเวอร์ชันแรก (ยังใช้ได้ ย้ายเข้าโครงสร้างใหม่แล้ว)

24 skills จากเวอร์ชันแรก (business-model-canvas-builder, financial-ratio-analyzer, contract-clause-reviewer
ฯลฯ) ยังอยู่ครบ แค่ย้ายเข้าไปอยู่ใต้หมวดใหญ่ ISCO ที่ตรงกับลักษณะงานที่สุด:

- งานที่เป็นการบริหาร/วางกลยุทธ์/ปฏิบัติการ (business-strategy, operations-supply-chain เดิม) → `skills/managers/`
- งานวิชาชีพเฉพาะทาง (finance-accounting, marketing-sales, hr-people-ops, legal-compliance,
  technology-data, education-training เดิม) → `skills/professionals/`

ทั้ง 24 ตัวนี้เป็น skill เฉพาะงาน (task-specific) ในขณะที่ 43 skill ใหม่เป็น skill ระดับกลุ่มอาชีพ
(occupation-cluster) ที่กว้างกว่า — ใช้เสริมกันได้ในหมวดเดียวกัน

## ระดับถัดไปสำหรับขยายต่อ (Roadmap)

ตอนนี้ครอบคลุมครบ 43/43 หมวดย่อยแล้ว ระดับที่ยังเจาะลึกได้อีกคือ:

1. **หมู่ (Minor groups) — 130 หมู่** เช่น จากหมวดย่อย 22 "สุขภาพ" แตกเป็น 221 แพทย์, 222 พยาบาล,
   223 แพทย์แผนโบราณ ฯลฯ — ทำ skill เฉพาะอาชีพย่อยลงไปอีกสำหรับหมวดที่มีคนทำงานเยอะ/มีความต้องการเฉพาะสูง
2. **หน่วยอาชีพ (Unit groups) — 436 หน่วย** คือระดับละเอียดที่สุดของ ISCO-08 (เช่น "นักกายภาพบำบัด"
   แยกจาก "แพทย์" ชัดเจน) เหมาะกับการทำ skill เฉพาะทางสุดๆ ในเฟสยาว
3. **อาชีพยุคใหม่ที่ ISCO-08 ยังไม่มีรหัสแยก** เช่น Data Scientist, ML Engineer, Prompt Engineer —
   ตอนนี้ถูกจัดรวมในหมวดใกล้เคียงที่สุด (เช่น 25 ICT) ส่วนไรเดอร์ส่งของมีรหัสอยู่แล้วคือ 8321 Motorcycle Drivers
   (ISCO-08 ระบุ "dispatch rider" ไว้ในหน่วยนี้) แต่ ISCO จัดตามลักษณะงาน จึงไม่แยกว่าเป็นงานผ่านแพลตฟอร์ม (gig) หรือไม่
   ฉบับปรับปรุงของ ISCO ที่ ILO มีกำหนดนำเสนอในที่ประชุม ICLS ครั้งที่ 22 ปี 2571 (2028)

## วิธีขยายต่อ (สำหรับทีมหรือ contributor ใหม่)

1. เลือกหมวดย่อย/หมู่/หน่วยอาชีพที่ต้องการเจาะลึกเพิ่ม จากตาราง ISCO-08 ทางการ (ดูแหล่งอ้างอิงด้านล่าง)
2. ใช้ skill ที่มีอยู่แล้วในหมวดใหญ่เดียวกันเป็นต้นแบบโครงสร้าง (ดู "กติกาการเขียน SKILL.md" ใน README
   และ [`docs/CROSS_PLATFORM.md`](CROSS_PLATFORM.md) สำหรับกติกาข้ามแพลตฟอร์ม)
3. ถ้ามี skill สร้าง skill ในระบบ — ใช้ช่วยร่าง + ทำ eval คุณภาพก่อน merge
4. สร้างโฟลเดอร์ `skills/<major-group-slug>/<code>-<skill-slug>/SKILL.md` ตามรูปแบบเดิม
5. รัน `python3 scripts/validate.py` ให้ผ่านก่อน แล้วรัน `python3 scripts/build.py` เพื่ออัปเดต
   `catalog.json`, `.claude-plugin/marketplace.json` และ `dist/*.zip` อัตโนมัติ
6. ส่ง Pull Request พร้อมอธิบายว่า skill ใหม่ครอบคลุมอาชีพ/งานอะไร และอ้างอิงรหัส ISCO-08 ที่เกี่ยวข้อง

## แหล่งอ้างอิง

1. International Labour Organization (ILO) — [The International Standard Classification of Occupations
   (ISCO-08)](https://ilostat.ilo.org/methods/concepts-and-definitions/classification-occupation/) —
   โครงสร้าง 10/43/130/436 และระดับทักษะรายหมวดใหญ่
2. สำนักงานสถิติแห่งชาติ — [ตารางสถิติ โครงการสำรวจภาวะการทำงานของประชากร ไตรมาส 3 พ.ศ. 2568](https://www.nso.go.th/nsoweb/storage/survey_detail/2025/20251030091822_77870.pdf)
   (ตาราง 3) — ผู้มีงานทำ 39,852,121 คน จำแนกตามอาชีพ 9 หมวด + คนงานซึ่งมิได้จำแนกไว้ในหมวดอื่น 128,524 คน
3. กรมการจัดหางาน — การจัดประเภทมาตรฐานอาชีพไทย (TSCO) ฉบับปี 2544 — อิง ISCO-88 หนึ่งรุ่นก่อนหน้า
4. ILO Department of Statistics — [Progress of work on the ISCO-08 revision](https://unstats.un.org/unsd/classifications/Meetings/UNCEISC2024_2nd/Session_3_Progress%20of%20work%20ISCO_08.pdf) (นำเสนอในที่ประชุม UN Expert Group on International Statistical Classifications, ต.ค. 2024) — ไทม์ไลน์เสนอฉบับใหม่ที่ ICLS ครั้งที่ 22 ปี 2571 (2028)

ข้อมูลสถิติและโครงสร้างหมวดในเอกสารนี้อ้างอิงจากรายงาน "ISCO-08 ครบทั้ง 43 หมวดย่อย พร้อมตัวอย่างอาชีพจริง
และการนับในบริบทไทย" (จัดทำ 13 กันยายน 2569) ซึ่งตรวจสอบยอดรวมผู้มีงานทำ 39,852,121 คน ตรงกับยอดรวมของ สสช.
