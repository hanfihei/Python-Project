import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 불러오기
load_dotenv()

# 클라이언트 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_test(query: str):
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=[
            {
                "role": "system",  # system -> ai 성격, 규칙 설정
                "content": """
                [역할]
                너는 사용자의 응답을 json형태로 filter에 맞게 전달하는 도구다.

                [출력형식]
                {
                    "category": "",
                    "weight": 0.0,
                    "price": 0,
                    "tags": []
                }

                [규칙]
                1. 반드시 json 객체만 출력한다.
                2. 필터 항목(category, weight, price, tags) 외의 값은 절대 포함하지 않는다.
                3. 값이 없다면 기본값을 사용한다. int는 0, float는 0.0, str은 "", list는 []를 사용한다.
                4. price는 int만, weight는 float만, category는 str만 반환해야 한다. tags는 문자열 배열(list[str])만 반환해야 한다.
                5. 카테고리는 데스크탑, 컴퓨터, 노트북, 모니터, 마우스, 키보드, 헤드셋 중 하나만 올 수 있다.
                6. 사용자 응답에서 저렴하거나 싼 제품을 찾는다면 tags에 "가성비"를 추가한다.
                7. 가볍거나 휴대성이 좋은 제품을 찾는다면 tags에 "휴대성"을 추가한다.
                8. 비싸거나 프리미엄 제품을 찾는다면 tags에 "프리미엄"을 추가한다.
                9. 성능 좋은 제품을 찾는다면 tags에 "고성능"을 추가한다.
                10. 게임용 제품을 찾는다면 tags에 "게이밍", "고성능"을 추가한다.
                11. tags에 같은 값은 중복해서 넣지 않는다.
                12. 일치하는 키워드가 없다면 tags는 빈 배열 []로 반환한다.


                [예시]
                입력: 1kg 이하 노트북
                출력:
                {
                    "category": "노트북",
                    "weight": 1.0,
                    "price": 0,
                    "tags": ["휴대성"]
                }
                """
            },
            {
                "role": "user",  # user -> 사용자 입력
                "content": query
            }
        ]
    )
    # 결과 출력
    print(response.output_text)
    return response.output_text


def get_recommendation(result: list[dict], query: str):
    response = client.responses.create(
    model="gpt-5.4-mini",
    input=[
        {
            "role": "system",  # system -> ai 성격, 규칙 설정
            "content": """
            [역할]
            너는 result에 있는 상품들과 사용자의 응답을 비교해서 최적의 제품을 소개해주는 역할이야.
            [출력형식]
            {
            "recommendations": [
                {
                "rank": 1,
                "name": "삼성 갤럭시 노트북",
                "price": 500000,
                "reason": "가격이 저렴하고 무게가 가벼워 휴대성이 뛰어나며, 일상 작업에 적합합니다."
                },
                {
                "rank": 2,
                "name": "LG 그램",
                "price": 900000,
                "reason": "초경량 노트북으로 휴대성이 매우 뛰어나며 배터리 성능도 우수합니다."
                },
                {
                "rank": 3,
                "name": "Lenovo IdeaPad",
                "price": 450000,
                "reason": "가성비가 좋고 기본적인 작업을 수행하기에 충분한 성능을 제공합니다."
                }
            ],
            }

            [규칙]
            1. 순위를 매기는데 맞는 제품이 없다면 결과가 꼭 3개가 아니여도 된다.
            2. 이유를 설명할 때는 사용자의 응답과 상품의 태그, 설명이 일치하는 순서에 따라 순위를 매긴다.
            3. 사용자의 요청(query)과 가장 관련성이 높은 상품을 우선 선택한다.
            4. 가격, 무게, 카테고리 등 필터 조건을 우선적으로 만족하는 상품을 선택한다.
            5. 같은 상품을 중복해서 추천하지 않는다.
            6. 최대 3개의 상품만 추천한다.
            7. 반드시 json형식으로 출력해라.
            8. 반드시 제공된 상품 목록(result)에 있는 상품만 사용한다.


            [예시]
            입력: 가벼운 노트북 추천해줘
            출력:
            {
            "recommendations": [
                {
                "rank": 1,
                "name": "LG 그램",
                "price": 900000,
                "reason": "가벼운 무게와 휴대성이 뛰어나 사용자 요청과 가장 잘 맞습니다."
                },
                {
                "rank": 2,
                "name": "삼성 갤럭시 노트북",
                "price": 800000,
                "reason": "가격과 성능이 균형 잡혀 있으며 휴대성이 좋습니다."
                }
            ]
            }
            """
        },
        {
            "role": "user",  # user -> 사용자 입력
            "content": f"""
            사용자 요청:
            {query}

            상품 목록:
            {result}
            """
        }
     ]
)
    # 결과 출력
    print(response.output_text)
    return response.output_text
    
