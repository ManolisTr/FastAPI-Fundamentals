from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: float = Field(...,ge=13, description="The tax must be greater than or equal to 13")


# Use the Pydantic model in a FastAPI route
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "description": item.description, "price": item.price, "tax": item.tax}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # Test the API with the following  data:
    # {
    #     "name": "item name",
    #     "description": "item description",
    #     "price": 10,
    #     "tax": 13
    # }