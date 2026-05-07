import json
from app.db.database import get_connection
from app.services.embedding_service import create_embedding

# 상품을 받아서 문자열로 만드는 함수
def make_product_text(product: dict) -> str:
    return f"""
상품명: {product["name"]}
카테고리: {product["category"]}
가격: {product["price"]}원
무게: {product["weight"]}kg
태그: {', '.join(product["tags"])}
설명: {product["description"]}
"""

# products.json에 있는 상품들을 읽어서 상품 설명을 임베딩으로 바꾼 후 product 테이블에 저장
def import_products():
    # products.json 파일 읽기
    with open("app/data/products.json", "r", encoding="utf-8") as file:
        products = json.load(file) # json -> 딕셔너리

    # DB 연결
    conn = get_connection() # 연결 통로
    cur = conn.cursor() # 연결 통로로 DB에 접근할 수 있는 객체

    for product in products:
        product_text = make_product_text(product) # 상품 설명 문자열로 변환

        # 임베딩 생성
        embedding = create_embedding(product_text) # 문자열 -> 벡터

        cur.execute(
            """
            INSERT INTO products (name, category, price, weight, tags, description, embedding)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                product["name"],
                product["category"],
                product["price"],
                product["weight"],
                product["tags"],
                product["description"],
                embedding 
            )
        )

    conn.commit() 
    cur.close()
    conn.close()

    print("상품 저장 완료")


       