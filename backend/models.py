from pydantic import BaseModel


class Category(BaseModel):
    name: str
    imape_path: str


class Product(BaseModel):
    name: str
    imape_path: str
    category: Category
