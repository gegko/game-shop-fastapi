import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_URL = (
    os.getenv("MONGO_URL")
    .replace('<username>', MONGO_USER)
    .replace('<password>', MONGO_PASSWORD)
)
client = AsyncIOMotorClient(MONGO_URL)
db = client.gameshop
category_schema = db.category
product_schema = db.product

async def get_all_categories():
    categories = await category_schema.find().to_list(10)
    return categories

async def get_all_category_products(category_name: str):
    category = await category_schema.find_one({"name": category_name})
    products = (
        await product_schema
        .find({"category.name": category["name"]})
        .to_list(100)
    )
    return products
