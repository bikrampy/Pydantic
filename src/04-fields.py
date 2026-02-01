from pydantic import BaseModel, Field;
from typing import List;

class Product(BaseModel):
    pId: int = Field(
        ...
    )
    pName: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Provide a valid product name (3-50)',
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
    pImgs: List[str] | None = Field(
        default=None,
    )

sampleData = {
    'pId': 1,
    'pName': 'Iphone 17',
    'pPrice': 67000,
    'pQuantity': 15
}

product1 = Product(**sampleData);
print(product1);
