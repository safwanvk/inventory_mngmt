# 📟 Inventory Management API

A simple RESTful API built using **Django** and **Django Rest Framework** to manage products and stock operations.

---

## 🚀 Local Setup (without Docker)

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔌 API Endpoints

### 📦 Product Management

| Method | Endpoint                 | Description                |
| ------ | ------------------------ | -------------------------- |
| GET    | `/api/v1/products/`      | List all products          |
| GET    | `/api/v1/products/{id}/` | Retrieve a product         |
| POST   | `/api/v1/products/`      | Create a new product       |
| PUT    | `/api/v1/products/{id}/` | Update an existing product |
| DELETE | `/api/v1/products/{id}/` | Delete a product           |

### 📉 Stock Management

| Method | Endpoint                              | Description               |
| ------ | ------------------------------------- | ------------------------- |
| POST   | `/api/v1/products/{id}/sell/` | Sell/reduce product stock |

---

## 🔔 Low Stock Notification Feature

When a product is sold (via `/sell/`) or update, if the quantity falls below a set threshold (e.g., 10 units), a **notification task** is triggered asynchronously using **Celery**.

📬 This helps warehouse managers keep track of items that are about to run out.

---

## ⚙️ Celery & Redis Setup

1. **Start Redis** (used as the message broker):

   ```bash
   docker-compose up -d redis_broker
   ```

2. **Run Celery Worker**:

   ```bash
   docker-compose up -d celery_worker
   ```

   Or manually (if not using Docker Compose):

   ```bash
   celery -A inventory_mngmt worker -l info
   ```

---

## 🐻 Docker Setup

### 🧱 Build & Run with Docker Compose

```bash
# Build images
docker-compose build

# Run containers (Django app, Redis, Celery)
docker-compose up
```

📦 Services included:

* `inventory_app`: Django + Gunicorn
* `redis_broker`: Message broker for Celery
* `celery_worker`: Handles background tasks

---

## 📃 Example API Requests

### ➕ Create a Product

```bash
curl -X POST http://localhost:8000/api/v1/products/ \
-H "Content-Type: application/json" \
-H "Authorization: ApiKey <your-api-key>" \
-d '{
  "name": "Product 1",
  "description": "Description",
  "price": 10.99,
  "quantity_in_stock": 100
}'
```

### 📃 Get All Products
```bash
curl -X GET http://localhost:5000/api/v1/products/
```

### 🔍 Get Product by ID
```bash
curl -X GET http://localhost:5000/api/v1/products/1/
```

### ✏️ Update a Product
```bash
curl -X PUT http://localhost:5000/api/v1/products/1/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Updated Product 1",
  "description": "Updated description",
  "price": 12.99,
  "quantity_in_stock": 150
}'
```

### ❌ Delete a Product
```bash
curl -X DELETE http://localhost:5000/api/v1/products/1/
```

### 📉 Manage Product Stock (Sell)
```bash
curl -X POST http://localhost:5000/api/v1/products/1/sell/ \
-H "Content-Type: application/json" \
-d '{"quantity_to_sell": 10}'
```

---

## 🗪 Running Tests

```bash
python manage.py test
```

---

## 📌 Filters & Ordering

Supports query params:

* `?name=phone`
* `?minimum_quantity_in_stock=10`
* `?ordering=name`
* `?ordering=-price`
