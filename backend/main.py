from fastapi import FastAPI, status
from database import get_all_categories, get_all_category_products

app = FastAPI()


@app.get("/categories")
async def get_categories_data():
    categories = await get_all_categories()
    for category in categories:
        del category['_id']
    if categories:
        status_code = status.HTTP_200_OK
        return {"categories": categories}
    status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Categories not found."}


@app.get("/products/{category}")
async def get_products_data(category: str):
    products = await get_all_category_products(category)
    for product in products:
        del product['_id']
    if products:
        status_code = status.HTTP_200_OK
        return {"products": products}
    status_code = status.HTTP_404_NOT_FOUND
    return {"message": "Products not found."}
