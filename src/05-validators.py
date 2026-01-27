from pydantic import BaseModel, Field, field_validator, model_validator, computed_field;
class User(BaseModel):
    uName: str = Field(...)
    @field_validator('uName')
    def validateUName(cls, v):
        if len(v) < 3:
            raise ValueError('Provide a valid username')
        return v
    password: str
    confirmPassword: str
    @model_validator(mode='after')
    def validatePassword(cls, v):
        if v.password != v.confirmPassword:
            raise ValueError('Password do not match')
        return v

user1 = User(uName='beingbifrons', password='12345', confirmPassword='12345')
print(user1)

class Product(BaseModel):
    price: float
    quantity: int
    @computed_field(return_type=float)
    @property
    def totalPrice(s):
        return s.price * s.quantity
p1 = Product(price=99.99, quantity=2)
print(p1)