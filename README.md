# Inventory Management API
This is a simple RESTful API for managing products using Django and Django Rest Framework. The API allows you to create, read, update, and delete products.


Set up and run the project
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

```

API Endpoints
```
GET /api/v1/products
GET /api/v1/products/{id}
POST /api/v1/products
PUT /api/v1/products/{id}
DELETE /api/v1/products/{id}
```

USAGE
```
# Create a new product
curl -X POST http://localhost:5000/api/v1/products/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Product 1",
  "description": "Description of Product 1",
  "price": 10.99,
  "quantity": 100
}'

# Get all products
curl -X GET http://localhost:5000/api/v1/products/

# Get a product by ID
curl -X GET http://localhost:5000/api/v1/products/1/

# Update a product
curl -X PUT http://localhost:5000/api/v1/products/1/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Updated Product 1",
  "description": "Updated description of Product 1",
  "price": 12.99,
  "quantity": 150
}'

# Delete a product
curl -X DELETE http://localhost:5000/api/v1/products/1
```
