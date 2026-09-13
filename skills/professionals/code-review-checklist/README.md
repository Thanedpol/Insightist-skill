# Code Review Checklist

**ผู้ช่วยนักพัฒนาและ tech lead รีวิวโค้ดตาม checklist 4 ด้าน แล้วสรุปเป็น review comment ที่สร้างสรรค์**

| | |
|---|---|
| **หมวดใหญ่ / Major group** | 2 · ผู้ประกอบวิชาชีพด้านต่างๆ (Professionals) |
| **Skill ID** | `code-review-checklist` |

[🇹🇭 ภาษาไทย](#th) · [🇬🇧 English](#en)

---

<a id="th"></a>

## 🇹🇭 ภาษาไทย

### Skill นี้สำหรับอาชีพไหน

นักพัฒนาซอฟต์แวร์ วิศวกรซอฟต์แวร์ และ tech lead ที่ต้องรีวิว pull request ก่อน merge
รวมถึงนักพัฒนาที่รับช่วงโค้ดต่อจากคนอื่น และผู้ดูแลความปลอดภัยของแอปพลิเคชันที่อยากเช็คจุดเสี่ยงในโค้ดอย่างเป็นระบบ

### ทำอะไรได้บ้าง

- ตรวจ **readability** เช่น การตั้งชื่อ ความยาวฟังก์ชัน magic number การ nest และโค้ดซ้ำซ้อน
- ตรวจ **security** เช่น การ validate input, SQL/command injection, hardcoded credentials, การ leak ข้อมูลใน error และการเช็คสิทธิ์
- ตรวจ **performance** เช่น loop ซ้อนที่ไม่จำเป็น, N+1 query, การใช้ cache และการปิด resource
- ประเมิน **test coverage** ทั้ง happy path, edge case, logic เสี่ยงสูง และ assertion ที่หลวมเกินไป
- จัดลำดับข้อค้นพบเป็น **🔴 Critical / 🟡 Suggested / 🟢 Nitpick**
- เขียน **review comment แบบสร้างสรรค์** บอกทั้งปัญหา เหตุผล และวิธีแก้ พร้อมชมจุดที่ทำดี
- ให้ **คำแนะนำสุดท้ายว่า merge ได้หรือไม่** พร้อมเหตุผลสั้นๆ

### ตัวอย่างคำสั่ง

- "ช่วยรีวิวโค้ด PR นี้หน่อย ก่อน merge ช่วยเช็คให้ที"
- "ฟังก์ชันนี้ปลอดภัยไหม มีปัญหาอะไรบ้าง"
- "ตรวจ diff นี้ให้หน่อยว่ามีจุดไหนจะทำให้ระบบช้า"

### สิ่งที่จะได้รับ

รายงาน code review ที่มีสรุปภาพรวม จุดที่ทำได้ดี ข้อค้นพบแบ่งตามระดับความสำคัญ
(แต่ละข้อระบุบรรทัด/ไฟล์ ปัญหา เหตุผล และข้อเสนอแนะ) ส่วนประเมิน test coverage
และคำแนะนำสุดท้ายว่าพร้อม merge, merge ได้แต่ตามแก้ทีหลัง หรือควรแก้ก่อน merge

### ขอบเขตและข้อควรระวัง

- ครอบคลุมทั้ง 4 มุมทุกครั้ง แต่ **ไม่แทนการทดสอบจริงหรือการทำ security audit เต็มรูปแบบ**
- ตัวอย่างช่องโหว่ใช้เพื่ออธิบายปัญหาเชิงการศึกษาเท่านั้น **ไม่มีโค้ด exploit ที่เป็นอันตรายจริง**
- ควรอ่านโค้ดประกอบ PR description หรือ ticket เพื่อให้รีวิวตรงกับเจตนาของงาน

---

<a id="en"></a>

## 🇬🇧 English

### Who is this skill for

Software developers, software engineers and tech leads who review pull requests before merging, as well as
developers taking over someone else's code and application security engineers who want a systematic pass
over risky spots.

### What it can do

- Check **readability**: naming, function length, magic numbers, nesting depth and duplicated code
- Check **security**: input validation, SQL/command injection, hardcoded credentials, leaky error messages and authorization checks
- Check **performance**: unnecessary nested loops, N+1 queries, caching opportunities and resource cleanup
- Assess **test coverage**: happy paths, edge cases, high-risk logic and assertions too loose to catch regressions
- Rank findings as **🔴 Critical, 🟡 Suggested or 🟢 Nitpick**
- Write **constructive review comments** covering the problem, why it matters and how to fix it, plus what was done well
- Give a **final merge recommendation** with a short reason

### Example prompts

- "Review this PR before I merge it."
- "Is this function safe? What's wrong with it?"
- "Check this diff for anything that could slow the system down."

### What you get

A code review with an overall summary, strengths, findings grouped by severity (each with file/line, problem,
impact and suggested fix), a test-coverage assessment, and a final verdict: ready to merge, merge with
follow-ups, or fix before merging.

### Scope and limitations

- Always covers all four areas, but **doesn't replace real testing or a full security audit**
- Vulnerability examples are for explanation only; **no working exploit code** is produced
- Share the PR description or ticket where possible so the review reflects the intent of the change

---

## 📦 ติดตั้ง / Installation

- **ไฟล์คำสั่งหลัก / Skill instructions:** [`SKILL.md`](SKILL.md)
- **แพ็กเกจพร้อมติดตั้ง / Installable package:** [`dist/code-review-checklist.zip`](../../../dist/code-review-checklist.zip)
- **วิธีติดตั้งทุกแพลตฟอร์ม / Setup for every platform:** [README หลัก / Main README](../../../README.md)

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*

*Part of the [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill), written by the Insightist™ team.*
