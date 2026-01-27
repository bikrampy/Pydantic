from pydantic import BaseModel, Field;

class Product(BaseModel):
    pId: int = Field(...)
    pName: str = Field(
        default='Sample Product',
        min_length=3,
        max_length=500,
        description='Provide a product name less than 3 and greater than 500',
        examples=['Iphone 15', 'Samsung Galaxy S23']
    )
    pPrice: int = Field(
        ...,
        gt= 0
    )
    pQuantity: int = Field(
        ...,
        ge= 1,
        le= 100
    )

# sampleData = {
#     'pId': 1,
#     'pName': 'Iphone 17',
#     'pPrice': 67000,
#     'pQuantity': 0 # this will throw an error
# }

# sampleData = {
#     'pId': 1,
#     'pName': 'I', # this will throw an error
#     'pPrice': 67000,
#     'pQuantity': 10
# }

sampleData = {
    'pId': 1,
    'pName': 'Iphone 17',
    'pPrice': 67000,
    'pQuantity': 12
}
product1 = Product(**sampleData);
print(product1);
