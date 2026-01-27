from pydantic import BaseModel;
class User(BaseModel):
    uID: int
    isActive: bool
    marks: float

user = User(uID='1', isActive=1, marks='99.99');
# 1 -> true, 0 -> false
print(user);

from pydantic import StrictBool, StrictInt, StrictStr
class User2(BaseModel):
    name: StrictStr
    age: StrictInt
    is_admin: StrictBool

user2 = User2(name='Bikram', age='100', is_admin='True')
print(user2)