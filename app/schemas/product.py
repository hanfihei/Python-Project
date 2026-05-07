# 상품 정보 DTO
from pydantic import BaseModel
from typing import List

class ProductResponse(BaseModel):
    name: str
    price: int
    weight: float
    category: str  # 빠른 구현을 위해 enum 대신 문자열 사용
    tags: list[str]
    description: str
