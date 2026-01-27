from pydantic import BaseModel, Field;
class User1(BaseModel):
    uid: int
    uname: str
# user1 = User1(uid= 1); # this will throw an error.
user1 = User1(uid= 1, uname='Bikram Saha');
print(user1);

from typing import Optional;
class User2(BaseModel):
    uId: int
    uName: Optional[str] = None
user2 = User2(uId= 1);
print(user2);
