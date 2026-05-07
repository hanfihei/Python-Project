import os # 환경변수 사용을 위한 os 모듈
from dotenv import load_dotenv

load_dotenv()

# .env 파일에서 환경변수 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")