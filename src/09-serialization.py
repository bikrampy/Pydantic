from pydantic import BaseModel, ConfigDict
from datetime import datetime

class User(BaseModel):
    uid: int
    name: str
    email: str | None = None
    password: str
    createdAt: datetime
    model_config = ConfigDict(
        json_encoders= {
            datetime: lambda v: v.strftime("%Y-%m-%d"),
        }
    )

user = User(
    uid=1,
    name='Bikram Saha',
    password='12345',
    createdAt=datetime.now(),
)

print(user.model_dump()) # dictionary
print(user.model_dump(exclude={'password'}))
print(user.model_dump(include={'name'}))
print(user.model_dump_json(exclude={'password'})) # json