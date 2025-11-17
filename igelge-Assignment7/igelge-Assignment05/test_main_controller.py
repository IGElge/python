import pytest
from fastapi.testclient import TestClient
from main_controller import app
import services.product_service as product_service
from models.product import Product
from unittest.mock import patch

client = TestClient(app)

@patch("services.product_service.get_all_products")
def test_get_products_success(mock_get_products):
    mock_get_products.return_value = [
        Product(ID=1, Name="Apple", Price=4.99, Type="Fruit"),
        Product(ID=2, Name="Tomato", Price=3.99, Type="Fruit")
    ]
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2


@patch("services.product_service.get_all_products")
def test_get_products_empty(mock_get_products):
    mock_get_products.return_value = []
    response = client.get("/products")
    assert response.status_code == 400
    assert response.json() == {"message": "No products available"}


@patch("services.product_service.get_product_by_id")
def test_get_product_success(mock_get_product):
    mock_get_product.return_value = Product(ID=1, Name="Apple", Price=4.99, Type="Fruit")
    response = client.get("/product?product_id=1")
    assert response.status_code == 200
    data = response.json()
    assert data["Name"] == "Apple"
    assert data["Type"] == "Fruit"
    assert data["Price"] == 4.99


@patch("services.product_service.get_product_by_id")
def test_get_product_not_found(mock_get_product):
    mock_get_product.return_value = None
    response = client.get("/product?product_id=999")
    assert response.status_code == 400
    assert response.json() == {"message": "Product not found"}


@patch("services.product_service.add_or_update_product")
def test_update_product_success(mock_add_or_update):
    mock_add_or_update.return_value = "Added New Product"
    product_data = {
        "ID": 1,
        "Name": "Updated Apple",
        "Price": 5.49,
        "Type": "Fruit"
    }
    response = client.post("/products/mod", json=product_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Added New Product"}


def test_update_product_invalid_missing_name():
    product_data = {
        "ID": 1,
        "Name": "   ",
        "Price": 5.49,
        "Type": "Fruit"
    }
    response = client.post("/products/mod", json=product_data)
    assert response.status_code == 400
    assert response.json() == {"message": "Request object missing required fields or invalid"}

def test_update_product_invalid_missing_type():
    product_data = {
        "ID": 1,
        "Name": "Banana",
        "Price": 2.99,
        "Type": "   "  # invalid type
    }
    response = client.post("/products/mod", json=product_data)
    assert response.status_code == 400
    assert response.json() == {"message": "Request object missing required fields or invalid"}

