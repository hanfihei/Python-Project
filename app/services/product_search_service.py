# 유저 질문 embedding → pgvector 유사 상품 TOP5 검색하는 서비스
from app.db.database import get_connection
from app.services.embedding_service import create_embedding

def search_similar_products(query: str, limit: int = 5):
    # 검색어 임베딩 생성
    query_embedding = create_embedding(query) 

    conn = get_connection()
    cur = conn.cursor()

    # <-> 연산자는 pgvector에서 벡터 간의 유사도를 계산하는 연산자, 값이 작을수록 유사도 높음
    cur.execute(
        """
        SELECT name, category, price, weight, tags, description
        FROM products

        -- 상품 embedding과 사용자 질문 embedding 사이의 거리 계산
        ORDER BY embedding <-> %s::vector
        LIMIT %s
        """,
        (query_embedding, limit)
    )

    # 조회된 상품 정보 가져오기
    product_data = cur.fetchall()

    # 상품들을 하나하나 꺼내서 리스트에 담기
    data = []
    for product in product_data:

        # product는 튜플 형태이므로 딕셔너리로 변환
        product = {
            "name": product[0],
            "category": product[1],
            "price": product[2],
            "weight": product[3],
            "tags": product[4],
            "description": product[5]
        }
        data.append(product)

    # result = dict(data) // 튜플이 2개가 넘으면 딕셔너리로 자동 변환이 불가함
    print(data)

    cur.close()
    conn.close()

    return data