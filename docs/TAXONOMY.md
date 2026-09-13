# Taxonomy & Roadmap

> 🗺️ อยากดูแบบลากโหนดเล่น/ขยายหมวดย่อยได้จริง เปิด **[Insightist Skill Map](https://claude.ai/code/artifact/df4a05d9-4ba8-4ae8-8c89-0e2bf51677af)**
> — มีมุมมองตารางสลับดูได้ในหน้าเดียวกัน

เอกสารนี้อธิบายกรอบการจัดหมวดหมู่ (taxonomy) ของ Insightist Skills Library
และหมวด/สายอาชีพที่ยังไม่ได้ทำ (roadmap) สำหรับขยายต่อในเฟสถัดไป

## แนวคิด

"ทุกสายอาชีพ" ครอบคลุมได้กว้างมาก — U.S. Standard Occupational Classification (SOC)
ซึ่งเป็นมาตรฐานที่หลายแพลตฟอร์ม skill marketplace ใช้จัดหมวด (เช่น SkillsMP) แบ่งอาชีพย่อยไว้
ประมาณ **867 อาชีพ** ภายใต้ **23 กลุ่มใหญ่** การพยายามสร้าง skill ให้ครบทุกอาชีพย่อยตั้งแต่รอบแรก
จะทำให้คุณภาพต่อชิ้นตกและดูแลรักษายาก

แนวทางของโปรเจกต์นี้คือ **Framework + Taxonomy + Pilot**:
1. ออกแบบหมวดหมู่ระดับบนที่ครอบคลุมงานความรู้ (knowledge work) ที่ใช้ข้ามอุตสาหกรรมได้ก่อน
2. ทำ skill ตัวอย่างคุณภาพสูงในแต่ละหมวด (pilot) ให้เห็นรูปแบบและมาตรฐาน
3. ขยายทีละหมวด/ทีละอาชีพ โดยใช้ skill ที่มีอยู่เป็นต้นแบบ + skill-creator ช่วยร่างและทดสอบ

## หมวดที่ทำแล้ว (Pilot — 24 skills)

| หมวด | โฟลเดอร์ | จำนวน skill |
|---|---|---|
| กลยุทธ์ / บริหารธุรกิจ | `skills/business-strategy/` | 3 |
| การเงิน / บัญชี | `skills/finance-accounting/` | 3 |
| การตลาด / งานขาย | `skills/marketing-sales/` | 3 |
| งานบุคคล / HR | `skills/hr-people-ops/` | 3 |
| กฎหมาย / การปฏิบัติตามกฎระเบียบ | `skills/legal-compliance/` | 3 |
| เทคโนโลยี / ข้อมูล | `skills/technology-data/` | 3 |
| ปฏิบัติการ / โลจิสติกส์ | `skills/operations-supply-chain/` | 3 |
| การศึกษา / ฝึกอบรม | `skills/education-training/` | 3 |

## หมวดที่ยังไม่ได้ทำ (Roadmap สำหรับเฟสถัดไป — 10 หมวด ~30 sub-professions)

จัดตามกลุ่ม SOC ที่ยังไม่ครอบคลุม เรียงตามลำดับความสำคัญที่แนะนำ พร้อม sub-professions
และตัวอย่างชื่อ skill ที่ควรสร้างจริง (3-4 ตัวต่อหมวด) เพื่อให้เวลาสร้างจริงทำได้ตรงเป้าและไม่ซ้ำกับที่มีอยู่

### 9. 🏥 สุขภาพ / การแพทย์ (`healthcare-wellness`)
**Sub-professions:** แพทย์/พยาบาล, เภสัชกร, นักกำหนดอาหาร, ผู้ดูแลผู้สูงอายุ, เทรนเนอร์/ฟิตเนส
**ตัวอย่าง skill:** `patient-education-handout-writer` · `clinic-visit-sop-builder` · `nutrition-plan-outline` · `health-campaign-content-writer`
**ข้อควรระวัง:** ต้องมี disclaimer ทุกไฟล์ว่าไม่ใช่คำแนะนำทางการแพทย์ ให้ปรึกษาผู้เชี่ยวชาญเสมอ (เหมือนหมวดกฎหมาย)

### 10. 🏗️ วิศวกรรม / การผลิต (`engineering-manufacturing`)
**Sub-professions:** วิศวกรโยธา, วิศวกรเครื่องกล/ไฟฟ้า, ควบคุมคุณภาพ (QC/QA), หัวหน้าไลน์ผลิต
**ตัวอย่าง skill:** `qc-inspection-checklist` · `preventive-maintenance-scheduler` · `engineering-change-request-writer` · `safety-incident-report-writer`
**ข้อควรระวัง:** เน้นเอกสาร/checklist/กระบวนการ มากกว่าการคำนวณเชิงลึกที่ต้องใช้ซอฟต์แวร์วิศวกรรมเฉพาะทาง

### 11. 🎨 ครีเอทีฟ / งานออกแบบ (`creative-design`)
**Sub-professions:** กราฟิกดีไซน์, ถ่ายภาพ/วิดีโอ, งานเขียน/บรรณาธิการ, ดนตรี/เสียง
**ตัวอย่าง skill:** `brand-moodboard-brief` · `shot-list-planner` · `editorial-style-guide-checker` · `portfolio-case-study-writer`
**หมายเหตุ:** ต่อยอดกับ skill ที่มีอยู่แล้วในระบบ (`dataviz`, `canvas-design`, `algorithmic-art`) แทนที่จะสร้างซ้ำ

### 12. 🌾 เกษตร / อาหาร (`agriculture-food`)
**Sub-professions:** เกษตรกร/ปศุสัตว์, ผู้แปรรูปอาหาร, ร้านอาหาร/F&B, ผู้ตรวจสอบความปลอดภัยอาหาร
**ตัวอย่าง skill:** `crop-yield-planner` · `haccp-food-safety-checklist` · `menu-costing-calculator` · `restaurant-shift-scheduler`

### 13. 🏘️ อสังหาริมทรัพย์ / ก่อสร้าง (`real-estate-construction`)
**Sub-professions:** นายหน้าอสังหา, ผู้จัดการโครงการก่อสร้าง, สถาปนิก, ผู้รับเหมา
**ตัวอย่าง skill:** `property-listing-writer` · `construction-project-timeline-builder` · `site-safety-checklist` · `lease-comparison-matrix`

### 14. 🛎️ บริการลูกค้า / การท่องเที่ยว (`customer-service-hospitality`)
**Sub-professions:** คอลเซ็นเตอร์, โรงแรม, ท่องเที่ยว/ทัวร์, งานอีเวนต์
**ตัวอย่าง skill:** `customer-complaint-response-writer` · `hotel-guest-experience-sop` · `tour-itinerary-planner` · `event-run-of-show-builder`

### 15. 🏛️ รัฐ / นโยบายสาธารณะ / NGO (`public-nonprofit`)
**Sub-professions:** งานราชการ, องค์กรไม่แสวงหากำไร, นักวิเคราะห์นโยบาย
**ตัวอย่าง skill:** `grant-proposal-writer` · `public-consultation-summary` · `ngo-impact-report-builder`

### 16. 🔬 วิทยาศาสตร์ / วิจัย (`science-research`)
**Sub-professions:** นักวิจัย, งานห้องปฏิบัติการ, งานวิชาการ/อาจารย์มหาวิทยาลัย
**ตัวอย่าง skill:** `research-proposal-outline` · `literature-review-summarizer` · `lab-sop-writer` · `academic-abstract-writer`

### 17. 🚚 ขนส่ง / โลจิสติกส์เฉพาะทาง (`transportation-logistics`)
**Sub-professions:** Fleet management, ขนส่งสินค้าระหว่างประเทศ, บริหารคลังสินค้า
**ตัวอย่าง skill:** `fleet-maintenance-log-tracker` · `customs-document-checklist` · `warehouse-layout-optimizer`
**หมายเหตุ:** แยกจาก `operations-supply-chain` เดิม เพราะเจาะจงงานขนส่ง/fleet มากกว่า operation ทั่วไป

### 18. 🔧 งานฝีมือ / ช่างเทคนิค (`skilled-trades`)
**Sub-professions:** ช่างไฟฟ้า, ช่างประปา, ช่างซ่อมบำรุงทั่วไป
**ตัวอย่าง skill:** `service-call-quote-writer` · `maintenance-job-checklist` · `warranty-claim-writer`

---

**สรุปภาพรวม:** 8 หมวดที่ทำแล้ว (24 skills) + 10 หมวดที่วางแผนไว้ (~30-35 skills เมื่อทำครบ)
= 18 หมวดใหญ่ ครอบคลุมสายอาชีพส่วนใหญ่ในตลาดแรงงาน ก่อนจะพิจารณาแตกย่อยลงไปอีกตาม
23 กลุ่ม SOC เต็มรูปแบบ (~867 อาชีพย่อย) ในระยะยาว

## วิธีขยายต่อ (สำหรับทีมหรือ contributor ใหม่)

1. เลือกหมวดจากตาราง roadmap ด้านบน (หรือหมวดใหม่ที่ยังไม่มีในลิสต์)
2. ใช้ skill ที่มีอยู่แล้วในหมวดใกล้เคียงเป็นต้นแบบโครงสร้าง (ดู "กติกาการเขียน SKILL.md" ใน README)
3. ถ้ามี Claude พร้อม skill `skill-creator` — ใช้ช่วยร่าง + ทำ eval คุณภาพก่อน merge
4. สร้างโฟลเดอร์ `skills/<category>/<skill-name>/SKILL.md` ตามรูปแบบเดิม
5. รัน `python3 scripts/validate.py` ให้ผ่านก่อน แล้วรัน `python3 scripts/build.py` เพื่ออัปเดต
   `catalog.json`, `.claude-plugin/marketplace.json` และ `dist/*.zip` อัตโนมัติ
6. ส่ง Pull Request พร้อมอธิบายว่า skill ใหม่ครอบคลุมอาชีพ/งานอะไร
