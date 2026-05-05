# FastAPI 기능을 쓰기 위해 가져오는 준비 코드
from fastapi import FastAPI
import json
from schemas.user_schema import UserRequest
from schemas.product_rank import ProductRankResponse
from schemas.filter import FilterRequest
from data.products import products
from services.ai_service import get_test
from services.ai_service import get_recommendation
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

# ai 없는 필터 테스트
@app.post("/search")
def product_search(filter: FilterRequest):
        filters = filter.model_dump()
        result = filter_products(products, filters)
        return result

# ai 동작 확인
@app.get("/getTest")
def gpt_test():
    print("gpt확인")
    result = get_test()
    print("ai반환완료")
    return {"result": result}

# ai를 적용한 필터 테스트
@app.get("/ai-search")
def ai_search_test(query: str):
    print("도착 확인")
    ai_result = get_test(query)
    filters = json.loads(ai_result) 


    print("AI 원본 결과:", ai_result)

    print("파싱된 필터:", filters)

    result = filter_products(products, filters)
    print("최종 결과:", result)

    if len(result) == 0:
         return "조건에 맞는 상품이 없습니다."
    
    final = get_recommendation(result, query)

    data = json.loads(final) 
    dto = ProductRankResponse(**data) 

    return dto








