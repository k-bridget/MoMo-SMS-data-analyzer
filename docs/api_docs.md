# MoMo SMS REST API Documentation

## Authentication
All endpoints require **Basic Authentication**.

- **Username:** admin
- **Password:** secret
- If credentials are missing or invalid → `401 Unauthorized`

Example request with credentials:
```bash
curl -u admin:secret http://localhost:8000/transactions
```

---

## Endpoints

### 1. GET /transactions
Retrieve **all transactions**.

**Request Example**
```bash
curl -u admin:secret http://localhost:8000/transactions
```

**Response Example**
```json
[
  {
    "id": 1,
    "body": "You have received 2000 RWF from Jane Smith...",
    "date": "10 May 2024",
    "address": "M-Money"
  },
  {
    "id": 2,
    "body": "Your payment of 1,000 RWF to Samuel Carter...",
    "date": "10 May 2024",
    "address": "M-Money"
  }
]
```

**Error Codes**
- `401 Unauthorized` – Invalid/missing credentials
- `404 Not Found` – Wrong endpoint

---

### 2. GET /transactions/{id}
Retrieve a **single transaction** by its ID.

**Request Example**
```bash
curl -u admin:secret http://localhost:8000/transactions/1
```

**Response Example**
```json
{
  "id": 1,
  "body": "You have received 2000 RWF from Jane Smith...",
  "date": "10 May 2024",
  "address": "M-Money"
}
```

**Error Codes**
- `401 Unauthorized`
- `404 Transaction not found`

---

### 3. POST /transactions
Add a **new transaction**.

**Request Example**
```bash
curl -u admin:secret -X POST -H "Content-Type: application/json" \
-d '{"id": 2000, "body": "Deposit 1000 RWF", "date": "12 Jan 2025", "address": "M-Money"}' \
http://localhost:8000/transactions
```

**Response Example**
```json
{ "message": "Transaction added" }
```

**Error Codes**
- `401 Unauthorized`
- `400 Bad Request` – Invalid JSON body
- `404 Not Found` – Wrong endpoint

---

### 4. PUT /transactions/{id}
Update an existing transaction by ID.

**Request Example**
```bash
curl -u admin:secret -X PUT -H "Content-Type: application/json" \
-d '{"body": "Updated transaction text"}' \
http://localhost:8000/transactions/2000
```

**Response Example**
```json
{ "message": "Transaction updated" }
```

**Error Codes**
- `401 Unauthorized`
- `400 Bad Request` – Invalid JSON body
- `404 Transaction not found`

---

### 5. DELETE /transactions/{id}
Delete a transaction by ID.

**Request Example**
```bash
curl -u admin:secret -X DELETE http://localhost:8000/transactions/2000
```

**Response Example**
```json
{ "message": "Transaction deleted" }
```

**Error Codes**
- `401 Unauthorized`
- `404 Transaction not found`
