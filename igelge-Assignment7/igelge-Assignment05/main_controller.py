from fastapi import FastAPI, status
from typing import List
from models.product import Product
from models.product_request import ProductRequest
import services.product_service as product_service
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Module 7 - Products API",
    version="1.0",
    contact={"name": "Isabella Elge", "email": "igelge@mail.mccneb.edu"},
    description="Assignment 7 - Products API with SQLite and Services"
)

@app.get("/", summary="Root Endpoint", responses={
    200: {"description": "Welcome message"},
})
def root():
    return {"message": "Welcome to the Products API! Go to /docs for Swagger UI."}


@app.get(
    "/products",
    response_model=List[Product],
    responses={
        200: {"description": "List of all products returned"},
        400: {
            "description": "No products found in the database",
            "content": {"application/json": {"example": {"message": "No products available"}}},
        },
    },
    summary="Get All Products",
    tags=["Products"],
)
def get_products():
    products = product_service.get_all_products()
    if not products:
        content = {"message": "No products available"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)
    return products


@app.get(
    "/product",
    response_model=Product,
    responses={
        200: {"description": "Product found and returned"},
        400: {
            "description": "Product ID not found",
            "content": {"application/json": {"example": {"message": "Product not found"}}},
        },
    },
    summary="Get Single Product by ID",
    tags=["Products"],
)
def get_product(product_id: int):
    product = product_service.get_product_by_id(product_id)
    if not product:
        content = {"message": "Product not found"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)
    return product


@app.post(
    "/products/mod",
    responses={
        200: {"description": "Product added or updated successfully", "content": {"application/json": {"example": {"message": "Added New Product"}}}},
        400: {
            "description": "Request object invalid or missing required fields",
            "content": {"application/json": {"example": {"message": "Request object missing required fields or invalid"}}},
        },
    },
    summary="Add or Update Product",
    tags=["Products"],
)
def update_product(product: ProductRequest):
    # Validate required fields - assuming Name, Type must be non-empty strings
    if not product.Name or product.Name.strip() == "" or not product.Type or product.Type.strip() == "":
        content = {"message": "Request object missing required fields or invalid"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)

    message = product_service.add_or_update_product(product)
    return {"message": message}
