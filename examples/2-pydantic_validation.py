from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []

# without pydantic
# class User:
#     def __init__(self, id: int, name: str, signup_ts: datetime | None = None, friends: list[int] = []):
#       self.id = id
#       self.name = name
#       self.signup_ts = signup_ts
#       self.friends = friends
    
external_data = {
    'id': '123',
    'name': 'John Doe',
    'signup_ts': '2017-06-01 12:22',
    'friends': [1, 2, '3']
}

if __name__ == "__main__":
    user = User(**external_data)
    print(user.id)
    print(user.signup_ts)
    print(user.friends)
