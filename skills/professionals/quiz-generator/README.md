# Quiz Generator

**ผู้ช่วยออกแบบทดสอบจากเนื้อหาหรือหัวข้อวิชา พร้อมเฉลยและคำอธิบายทุกข้อ สำหรับครู วิทยากร และผู้ทำ e-learning**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `quiz-generator` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

ครูระดับประถมและมัธยม อาจารย์ วิทยากรฝึกอบรม (Trainer) เจ้าหน้าที่ฝ่ายพัฒนาบุคลากร (L&D)
และนักพัฒนาสื่อ e-learning หรือ Instructional Designer ที่ต้องทำแบบทดสอบก่อนเรียน หลังเรียน หรือ assessment ประกอบบทเรียนออนไลน์

### ทำอะไรได้บ้าง

- สร้าง **แบบทดสอบจากเนื้อหาที่ให้มา** เช่น บทความ เอกสาร สไลด์ transcript หรือจากหัวข้อวิชาที่ระบุ
- รองรับ **หลายรูปแบบคำถาม** ได้แก่ ปรนัย 4 ตัวเลือก ถูก/ผิด เติมคำ และอัตนัยสั้น
- **ผสมระดับความคิดตาม Bloom's Taxonomy** (จำ/เข้าใจ ประยุกต์ใช้ วิเคราะห์) และกระจายคำถามให้ครอบคลุมทั้งเนื้อหา
- ออกแบบ **ตัวลวงที่สมเหตุสมผล** มาจากความเข้าใจผิดที่พบได้จริง
- เขียน **เฉลยพร้อมคำอธิบายเหตุผล** ทุกข้อ รวมถึงเหตุผลที่ตัวเลือกอื่นผิด
- ทำ **pre-test หรือ post-test** และตรวจเฉลยของคำถามที่ผู้ใช้เขียนไว้แล้ว

### ตัวอย่างคำสั่ง

- "ทำ quiz 5 ข้อ ปรนัย จากบทความเรื่องวงจรน้ำนี้ สำหรับนักเรียนมัธยมต้น"
- "ช่วยออกคำถามจากเอกสารอบรมนี้หน่อย เอาแบบผสม 10 ข้อ พร้อมเฉลย"
- "สร้างแบบทดสอบก่อนเรียนเรื่อง Excel พื้นฐานสำหรับพนักงานใหม่"

### สิ่งที่จะได้รับ

แบบทดสอบที่ระบุจำนวนข้อ รูปแบบ ระดับความยาก และแหล่งเนื้อหาที่อ้างอิง ตามด้วยชุดคำถาม ส่วนเฉลยและคำอธิบายแยกต่างหาก
และสรุปการกระจายคำถามตามระดับความคิด (ถ้าต้องการ)

### ขอบเขตและข้อควรระวัง

- **ทุกข้อและเฉลยจะถูกตรวจทานกับเนื้อหาต้นฉบับ** เพื่อไม่ให้เฉลยขัดแย้งกับต้นฉบับ
- ถ้าเนื้อหาสั้นเกินจำนวนข้อที่ขอ จะแจ้งตรงๆ แทนการแต่งเนื้อหาที่ไม่มีในต้นฉบับ
- ถ้าเป็นหัวข้อกว้างที่ไม่มีเนื้อหาอ้างอิง จะใช้ความรู้ทั่วไปที่เชื่อถือได้ และ **ควรให้ผู้เชี่ยวชาญตรวจทานอีกครั้ง**
- หลีกเลี่ยงการออกคำถามจากจุดที่คลุมเครือ หรือคำถามที่ตอบได้ด้วยสามัญสำนึกโดยไม่ต้องอ่านเนื้อหา

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Primary and secondary school teachers, lecturers, corporate trainers, L&D staff, and e-learning developers or
instructional designers who need pre-tests, post-tests or assessments for online course modules.

### What it can do

- Create **quizzes from your own material** (articles, documents, slides, transcripts) or from a named subject
- Support **several question types**: four-option multiple choice, true/false, fill in the blank and short answer
- **Mix thinking levels using Bloom's Taxonomy** (recall, application, analysis) and spread questions across the whole source
- Write **plausible distractors** based on real misconceptions
- Provide **an answer key with reasoning** for every question, including why the other options are wrong
- Build **pre-tests or post-tests**, or check the answer key for questions you've already written

### Example prompts

- "Make a 5-question multiple-choice quiz from this water cycle article for lower-secondary students."
- "Generate 10 mixed-format questions with answers from this training document."
- "Create a pre-test on basic Excel for new employees."

### What you get

A quiz header showing the number of questions, format, difficulty and source, followed by the question set,
a separate answer key with explanations, and an optional breakdown of questions by thinking level.

### Scope and limitations

- **Every question and answer is checked against the source material** so the key never contradicts it
- If the source is too short for the number of questions requested, it says so rather than inventing content
- For broad topics with no source text, it relies on reliable general knowledge, and **a subject expert should review the result**
- Avoids questions on ambiguous passages, or ones that can be answered by common sense without reading the material

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/quiz-generator.zip`](../../../dist/quiz-generator.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
