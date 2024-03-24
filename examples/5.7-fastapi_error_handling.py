from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Define a Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


# Use the Pydantic model in a FastAPI route
@app.post("/items/")
async def create_item(item: Item):
    if item.name == "Foo":
        raise HTTPException(status_code=418, detail="Item name cannot be Foo")
    return {"name": item.name, "description": item.description, "price": item.price, "tax": item.tax}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
