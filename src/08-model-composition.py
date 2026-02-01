from pydantic import BaseModel;
class Address(BaseModel):
    city: str
    pincode: int
class Cart(BaseModel):
    product: str
    price: float
class User(BaseModel):
    uid: int
    name: str
    address: Address
    cartItems: list[Cart] | None = None

cartItem1 = Cart(product='IPhone17', price=79999)
cartItem2 = Cart(product='Macbook Air M4', price=89999)
address1 = Address(city='Kolkata', pincode=700127)
user1 = User(uid=1, name='Bikram Saha', address=address1, cartItems=[cartItem1, cartItem2])
print(user1)