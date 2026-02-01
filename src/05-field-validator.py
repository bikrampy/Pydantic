from pydantic import BaseModel, field_validator;
class User(BaseModel):
    userName: str
    @field_validator('userName')
    def cleanUName(cls, v: str):
        strippedUname = v.strip()
        finalUname = strippedUname.lower()
        return finalUname
    @field_validator('userName')
    def checkUName(cls, v: str):
        if 'admin' in v.lower():
            raise ValueError('This Username is not allowed')
        return v
    
user1 = User(userName='bikram ')
print(user1.userName + '!')