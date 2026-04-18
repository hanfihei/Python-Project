# 데이터 검증 (스프링의 DTO느낌)
from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    age: int