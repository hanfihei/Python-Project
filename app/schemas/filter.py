from pydantic import BaseModel
from typing import List

class FilterRequest(BaseModel):
    weight: float = 0.0
    price: int = 0
    category: str = ""
    tags: list[str] = []
