from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Define a Pydantic model
class User(BaseModel):
    id: int 
    name : str
    signup_ts: datetime | None = None
    friends: list[int] = []

# Use the Pydantic model in a FastAPI route
@app.post("/user/")
def create_user(user: User):
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # Test the API with the following  data:
    # {
    #     "id": 123,
    #     "name": "John Doe",
    #     "signup_ts": "2017-06-01 12:22",
    #     "friends": [1, 2, "3"]
    # }