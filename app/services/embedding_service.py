from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


# 문자열을 받아서 임베딩 벡터로 변환하는 함수
def create_embedding(text: str) -> (list[float]): # 문자열 -> float 리스트로 반환
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input = text
)
    
    # 첫번째 결과의 임베딩 값
    return response.data[0].embedding


# 반환되는 임베딩 예시
# {
#   "object": "list",
#   "data": [
#     {
#       "object": "embedding",
#       "embedding": [0.123, -0.551, 0.992]
#     }
#   ],
#   "model": "text-embedding-3-small"
# }