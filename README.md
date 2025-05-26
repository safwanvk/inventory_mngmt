# 🧾 Inventory Management API

This is a simple RESTful API for managing products using **Django** and **Django Rest Framework**. The API allows you to **create**, **read**, **update**, **delete**, and **manage product stock**.

---

## 🚀 Setup & Run the Project

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
| Method | Endpoint                    | Description               |
|--------|-----------------------------|---------------------------|
| GET    | `/api/v1/products/`         | List all products         |
| GET    | `/api/v1/products/{id}/`    | Retrieve a product        |
| POST   | `/api/v1/products/`         | Create a new product      |
| PUT    | `/api/v1/products/{id}/`    | Update an existing product|
| DELETE | `/api/v1/products/{id}/`    | Delete a product          |

### 📉 Stock Management
| Method | Endpoint                              | Description                         |
|--------|---------------------------------------|-------------------------------------|
| POST   | `/api/v1/products/{id}/sell/` | Sell/reduce stock from a product    |

---

## 🛠️ Usage

### ➕ Create a Product
```bash
curl -X POST http://localhost:5000/api/v1/products/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Product 1",
  "description": "Description of Product 1",
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
curl -X POST http://localhost:5000/api/v1/products/1/manage-stock/ \
-H "Content-Type: application/json" \
-d '{"quantity_to_sell": 10}'
```

---

## 🧪 Running Tests

To run the test suite:

```bash
python manage.py test
```

---

## 📌 Filters & Ordering

The product listing endpoint supports filtering and ordering:
- `?name=phone` → filter by product name
- `?minimum_quantity_in_stock=10` → filter by minimum stock
- `?ordering=name` or `?ordering=-price` → order by name or descending price

---