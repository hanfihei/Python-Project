# FastAPI 기능을 쓰기 위해 가져오는 준비 코드
from fastapi import FastAPI
# DTO import
from schemas.user_schema import UserRequest
from schemas.filter import FilterRequest
from data.products import products
from services.productFilterService import filter_products


# app 객체 생성(시작점)
app = FastAPI() 

# 전역변수로 저장 (DB 안 써서 재식작 시 초기화)
users = []

# 파이썬 기본 주소 http://127.0.0.1:8000/
# GET요청이 들어오면 json응답을 돌려주는 api
@app.get("/")
def root(): 
    return {"message": "hello fastapi"} #딕셔너리로 -> json


@app.get("/users/{id}")
def get_name(id: int, name: str):
    return {"result": f"{id}{name}"} # f-string -> 자료형 맞춰줌


@app.post("/users")
def create_user(request: UserRequest):
    # 딕셔너리 생성
    user = { 
        "name": request.name,
        "age": request.age
    }

    users.append(user)

    return {
        "name": request.name,
        "age": request.age,
        "message": "유저 생성" # 단순 메세지 반환
    }





#===============상품 추천 API====================

@app.get("/products")
def get_products():
    return products

@app.post("/search")
def product_search(filter: FilterRequest):
        filters = filter.model_dump()
        result = filter_products(products, filters)
        return result



