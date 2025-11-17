from pydantic import BaseModel

class Class(BaseModel):
    id: int
    code: str
    title: str
    description: str
