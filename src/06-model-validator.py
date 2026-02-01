from pydantic import BaseModel, Field, model_validator;
class User(BaseModel):
    userId: int = Field(...)
    password: str
    confirmPassword: str
    @model_validator(mode='after')
    def validatePassword(cls):
        if cls.password != cls.confirmPassword:
            raise ValueError('Password do not match')
        return cls

u1 = User(userId=1, password='12345', confirmPassword='12345')
print(u1)
