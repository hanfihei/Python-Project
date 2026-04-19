from pydantic import BaseModel
from schemas.product_rank_item import ProductRankItem
from typing import List

class ProductRankResponse(BaseModel):
    recommendations: List[ProductRankItem]
