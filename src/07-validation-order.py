from pydantic import BaseModel, Field, field_validator, model_validator

class User(BaseModel):
    age: int = Field(ge=18)

    @field_validator("age", mode="before")
    def before_age(cls, value):
        print("before validator")
        print(type(value), value)
        return value

    @field_validator("age")
    def after_age(cls, value):
        print("after validator")
        print(type(value), value)
        return value

    @model_validator(mode="after")
    def final_check(self):
        print("model validator")
        return self


user = User(age='19')
