from pydantic import BaseModel

class Product(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: str
