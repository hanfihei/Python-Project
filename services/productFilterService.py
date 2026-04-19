from data.products import products
# 상품리스트를 보면서 조건에 안 맞는건 탈락시키고 끝까지 살아남는 상품만 모으기
# ex) "무게가 1키로가 안 넘고 가격이 50만원이 넘지않는 휴대성 좋은 노트북 추천해줘"

#지피티가 준 json 예시
# 필터 조건이 없다면 기본 값 반환함 -> int = 0, float = 0.0, str = ""
# {
#   "category": "노트북",
#   "max_price": 500000,
#   "max_weight": 1.0,
#   "tags": ["휴대성"] //이거 뺌
# } 우선 가격이나 무게가 ~이상 일때는 제외함

# products는 더미데이터, filter는 ai가 넘겨준 json자료
def filter_products(products, filters): 
    result = []

    for product in products:
        # 딕셔너리는 .으로 접근 불가능
        # if(product["category"] == filters["category"]
        #     and product["weight"] <= filters["weight"]
        #     and product["price"] <= filters["price"]):
        if(filters["category"] != ""):
            if (product["category"] != filters["category"]):
                continue
            
        if(filters["weight"] != 0.0):
            if (product["weight"] > filters["weight"]):
                continue
            
        if(filters["price"] != 0):
            if (product["price"] > filters["price"]):
                continue

        result.append(product)
        
    return result
        



