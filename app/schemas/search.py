# 검색 흐름에서 쓰이는 DTO 정의
from pydantic import BaseModel
from app.schemas.product import Product

# 검색 요청
class SearchRequest(BaseModel):
    query: str

