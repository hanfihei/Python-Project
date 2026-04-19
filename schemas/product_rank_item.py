from pydantic import BaseModel

class ProductRankItem(BaseModel):
    rank: int
    name: str
    price: int
    reason: str

