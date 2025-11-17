from pydantic import BaseModel

class ProductRequest(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: str
