from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model
class Book(BaseModel):
    title: str
    price: float
    description: str | None = None


# Use the Pydantic model in a FastAPI route
@app.post("/books/")
async def create_book(book: Book) -> Book:
    return book


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # Test the API with the following  data:
    # {
    #     "title": "Python for Dummies",
    #     "price": 10,
    #     "description": "A book for beginners"
    # }
    