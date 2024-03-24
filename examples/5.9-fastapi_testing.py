from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = Field(
        None, title="The description of the item", max_length=300)
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")
    tax: float = Field(..., ge=13,
                       description="The tax must be greater than or equal to 13")

    def validate_name(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    def validate_price(cls, v):
        if v < 0:
            raise ValueError('must be non-negative')
        return v

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "description": item.description, "price": item.price, "tax": item.tax}

def test_create_item():
    with TestClient(app) as client:
        # Valid item data
        valid_item_data = {
            "name": "Test Item",
            "description": "This is a test item",
            "price": 10.0,
            "tax": 15.0
        }

        # Test valid item data
        response = client.post("/items/", json=valid_item_data)
        assert response.status_code == 200
        assert response.json() == valid_item_data

        # Invalid item data (price is negative)
        invalid_item_data = {
            "name": "Invalid Item",
            "description": "This item has a negative price",
            "price": -5.0,
            "tax": 13.5
        }

        # Test invalid item data
        response = client.post("/items/", json=invalid_item_data)
        
        if response.status_code == 422:
            print("Test passed: Negative price validation")
        else:
            raise AssertionError("Unexpected response status code")

if __name__ == "__main__":
    test_create_item()
