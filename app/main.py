from fastapi import FastAPI

from app.routers import category, products
from app.models.category import Category
from app.routers import auth, reviews

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "My e-commerce app"
    }

app.include_router(category.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(reviews.router)