import psycopg2 # PostgreSQL 연결 라이브러리
from app.core.config import DATABASE_URL

def get_connection():
    return psycopg2.connect(DATABASE_URL) # DB연결