---
name: api-doc-writer
description: เขียนเอกสาร API (API documentation) จากโค้ดหรือ spec ที่ผู้ใช้ให้มา ครอบคลุม endpoint, parameters, response schema, error codes และตัวอย่าง request/response ที่ใช้งานได้จริง ใช้ทุกครั้งที่ผู้ใช้พูดว่า "ช่วยเขียน API doc หน่อย", "document this API", "เขียนเอกสาร endpoint นี้", "สรุป API spec", "ทำ API reference", "อธิบาย endpoint ให้ทีม frontend", "generate API documentation", หรือแปะโค้ด route/controller/OpenAPI spec มาแล้วขอให้แปลงเป็นเอกสารอ่านง่าย แม้ไม่ได้พูดคำว่า "documentation" ตรงๆ ก็ให้ trigger skill นี้เสมอเมื่อบริบทคือการอธิบาย API ให้คนอื่นเข้าใจและเรียกใช้ได้
---

# API Doc Writer

Skill นี้ช่วยแปลงโค้ด API (เช่น route handler, controller function) หรือ spec ดิบ (เช่น OpenAPI/Swagger, Postman collection, คำอธิบายปากเปล่า) ให้กลายเป็นเอกสาร API ที่อ่านง่าย ใช้งานได้จริง และครบทุกส่วนที่นักพัฒนาฝั่งที่เรียกใช้ (consumer) ต้องการรู้ เหมาะสำหรับทีม backend ที่ต้องส่งมอบเอกสารให้ทีม frontend/mobile หรือทีมภายนอก (partner integration)

จุดสำคัญคือเอกสารต้อง "เรียกใช้ได้จริงทันทีที่อ่านจบ" — มีตัวอย่าง request/response ที่ copy ไปทดสอบได้เลย ไม่ใช่แค่บรรยาย parameter เป็นคำพูดลอยๆ

## เมื่อไหร่ควรใช้ skill นี้

- เมื่อพัฒนา API endpoint เสร็จแล้วต้องส่งมอบให้ทีม frontend/mobile เรียกใช้
- เมื่อต้องทำ API reference สำหรับ partner หรือ third-party ที่จะ integrate ระบบ
- เมื่อมีโค้ด backend (Express, FastAPI, Flask, Spring, ฯลฯ) แต่ยังไม่มีเอกสารประกอบ
- เมื่อมี OpenAPI/Swagger spec หรือ Postman collection แล้วอยากได้เอกสารที่อ่านง่ายกว่า raw spec
- เมื่อต้องอัปเดตเอกสารเดิมให้ตรงกับโค้ดที่เปลี่ยนแปลงไป (API versioning)
- เมื่อทีม support ต้องการเอกสาร error code เพื่อ debug ปัญหาจากลูกค้า

## ขั้นตอนการทำงาน

1. **สำรวจ input ที่มี** — อ่านโค้ด/spec ที่ได้รับมาให้ครบก่อน ระบุว่ามีกี่ endpoint แต่ละอันใช้ HTTP method อะไร (GET/POST/PUT/PATCH/DELETE) และ path เป็นอย่างไร ถ้าข้อมูลไม่ครบ (เช่น ไม่รู้ error response) ให้ระบุไว้ในเอกสารว่า "ต้องยืนยันเพิ่มเติม" แทนการเดาเอง
2. **สกัดข้อมูล endpoint แต่ละตัว** ให้ครบองค์ประกอบนี้:
   - **Method + Path** เช่น `POST /api/v1/orders`
   - **คำอธิบายสั้นๆ** ว่า endpoint นี้ทำอะไร ใช้เมื่อไหร่
   - **Authentication** ต้องใช้ token/API key ไหม ใส่ตรงไหน (header, query param)
3. **สกัด Parameters** แยกตามประเภทให้ชัดเจน:
   - Path parameters (เช่น `/orders/{order_id}`)
   - Query parameters (เช่น `?page=1&limit=20`)
   - Request body / payload (สำหรับ POST/PUT/PATCH)
   - สำหรับแต่ละ parameter ต้องระบุ: ชื่อ, ชนิดข้อมูล, จำเป็นหรือไม่ (required/optional), ค่า default (ถ้ามี), คำอธิบายสั้นๆ, และ constraint (เช่น ความยาวสูงสุด, ค่าที่ยอมรับได้)
4. **สกัด Response Schema** สำหรับกรณีสำเร็จ (2xx):
   - HTTP status code ที่จะได้ (เช่น 200, 201, 204)
   - โครงสร้าง response body พร้อมชนิดข้อมูลของแต่ละ field
   - ถ้ามีการแบ่งหน้า (pagination) ให้ระบุ field ที่เกี่ยวข้อง (เช่น `total`, `page`, `next_cursor`)
5. **สกัด Error Codes** ให้ครบทุกกรณีที่เป็นไปได้:
   - HTTP status code (400, 401, 403, 404, 409, 422, 429, 500 ฯลฯ)
   - เงื่อนไขที่ทำให้เกิด error นั้น (เช่น 404 เมื่อ order_id ไม่มีอยู่จริง)
   - โครงสร้าง error response (เช่น `{ "error": "...", "code": "..." }`)
   - ถ้าโค้ดต้นทางไม่ได้ระบุ error case ไว้ครบ ให้เดาเฉพาะกรณีมาตรฐานที่เป็นไปได้จริงจาก logic (เช่น validation error) และทำเครื่องหมายว่าควรให้ทีม backend ยืนยัน ห้ามสร้าง error code ที่ไม่มีอยู่จริงขึ้นมาลอยๆ
6. **สร้างตัวอย่าง Request/Response ที่ใช้งานได้จริง** — เขียนตัวอย่างเป็น curl หรือ JSON ที่มีค่าสมมติสมจริง (ไม่ใช้ค่าที่ดูปลอมเกินไปแบบ "string", "foo") ให้ครบทั้งกรณีสำเร็จอย่างน้อย 1 ตัวอย่าง และกรณี error อย่างน้อย 1 ตัวอย่าง
7. **จัดกลุ่มและเรียงลำดับ** — ถ้ามีหลาย endpoint ให้จัดกลุ่มตาม resource (เช่น Orders, Users, Payments) และเรียงตาม CRUD (Create → Read → Update → Delete) เพื่อให้ผู้อ่านตามง่าย
8. **ตรวจทานความสอดคล้อง** — เช็คว่าชื่อ field ในตัวอย่าง JSON ตรงกับที่ระบุใน schema ทุกจุด ไม่มีจุดที่ขัดแย้งกันเอง

## โครงสร้าง Output

```
# API Documentation: [ชื่อ Service/Module]

## ภาพรวม
[บอกว่า API ชุดนี้ใช้ทำอะไร Base URL คืออะไร ต้อง authenticate อย่างไร]

**Base URL:** `https://api.example.com/v1`
**Authentication:** [วิธี auth เช่น Bearer token ใน header Authorization]

---

## [ชื่อกลุ่ม เช่น Orders]

### [Method] [Path]
[คำอธิบายสั้นๆ ว่า endpoint นี้ทำอะไร]

**Parameters**

| ชื่อ | ตำแหน่ง | ชนิด | จำเป็น | คำอธิบาย |
|---|---|---|---|---|
| ... | path/query/body | string/int/... | ใช่/ไม่ | ... |

**Response สำเร็จ (200/201)**
```json
{
  "field": "ตัวอย่างค่า"
}
```

**Error Codes**

| Status | เงื่อนไข | Response |
|---|---|---|
| 400 | ... | `{ "error": "..." }` |
| 404 | ... | `{ "error": "..." }` |

**ตัวอย่าง Request**
```bash
curl -X POST https://api.example.com/v1/... \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{ "field": "ค่า" }'
```

**ตัวอย่าง Response**
```json
{
  "field": "ค่าที่ได้กลับมา"
}
```

---
[ทำซ้ำรูปแบบเดียวกันสำหรับ endpoint ถัดไป]

## หมายเหตุ/จุดที่ต้องยืนยันเพิ่มเติม
- [รายการที่ข้อมูลต้นทางไม่ครบ ต้องเช็คกับทีม backend]
```

## ตัวอย่าง

**Input** (ฟังก์ชัน route แบบง่ายที่ผู้ใช้แปะมา):

```python
@app.post("/api/v1/orders")
def create_order(payload: OrderCreate):
    if payload.quantity <= 0:
        raise HTTPException(400, detail="quantity must be positive")
    if not product_exists(payload.product_id):
        raise HTTPException(404, detail="product not found")
    order = Order.create(product_id=payload.product_id, quantity=payload.quantity)
    return {"order_id": order.id, "status": "created", "total_price": order.total_price}
```

**Output คร่าวๆ ที่ควรได้:**

```
## Orders

### POST /api/v1/orders
สร้างคำสั่งซื้อใหม่สำหรับสินค้าหนึ่งรายการ

**Parameters (request body)**

| ชื่อ | ตำแหน่ง | ชนิด | จำเป็น | คำอธิบาย |
|---|---|---|---|---|
| product_id | body | string | ใช่ | รหัสสินค้าที่ต้องการสั่งซื้อ |
| quantity | body | integer | ใช่ | จำนวนที่สั่งซื้อ ต้องมากกว่า 0 |

**Response สำเร็จ (200)**
```json
{
  "order_id": "ord_8f21a",
  "status": "created",
  "total_price": 590.00
}
```

**Error Codes**

| Status | เงื่อนไข | Response |
|---|---|---|
| 400 | quantity น้อยกว่าหรือเท่ากับ 0 | `{ "detail": "quantity must be positive" }` |
| 404 | product_id ไม่มีอยู่จริงในระบบ | `{ "detail": "product not found" }` |

**ตัวอย่าง Request**
```bash
curl -X POST https://api.example.com/v1/orders \
  -H "Content-Type: application/json" \
  -d '{ "product_id": "prod_123", "quantity": 2 }'
```

## หมายเหตุ
- โค้ดไม่ได้ระบุวิธี authentication ไว้ชัดเจน ควรยืนยันกับทีม backend ว่า endpoint นี้ต้องใช้ token หรือไม่
```

## เกณฑ์คุณภาพ

- [ ] ทุก endpoint มีครบ 5 ส่วน: path/method, parameters, response schema, error codes, ตัวอย่าง request/response
- [ ] ตัวอย่าง JSON ใช้ค่าสมมติที่สมจริง ไม่ใช้ placeholder ลอยๆ อย่าง "string"/"foo"
- [ ] ชื่อ field ในตัวอย่างตรงกับที่ระบุใน schema ทุกจุด ไม่ขัดแย้งกันเอง
- [ ] error code ที่ระบุมาจาก logic จริงในโค้ด/spec ไม่ใช่การเดาแบบไม่มีที่มา
- [ ] จุดที่ข้อมูลต้นทางไม่ครบ ถูกระบุแยกไว้ชัดเจนว่าต้องยืนยันเพิ่ม ไม่ปนกับข้อมูลที่ยืนยันแล้ว
- [ ] จัดกลุ่ม endpoint ตาม resource และเรียงลำดับอ่านง่ายเมื่อมีหลาย endpoint

---

*ส่วนหนึ่งของ [Insightist™ Skills Library](https://github.com/Thanedpol/Insightist-skill) — เขียนโดยทีม Insightist™*
