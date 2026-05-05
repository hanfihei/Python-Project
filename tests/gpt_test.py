import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 불러오기
load_dotenv()

# 클라이언트 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# GPT 호출
response = client.responses.create(
    model="gpt-5.4-mini",  # 일단 이걸로
    input="안녕이라고만 답해줘"
)

# 결과 출력
print(response.output_text)