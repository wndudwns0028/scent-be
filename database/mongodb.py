from pymongo import MongoClient
from dotenv import load_dotenv
import os  # ⬅ 이거 빠졌으면 꼭 추가하세요

load_dotenv()

# ✅ 환경변수에서 실제 URI를 가져오기
MONGODB_URL = os.getenv("MONGODB_URL")

if not MONGODB_URL:
    raise ValueError("❌ MONGODB_URL 환경변수를 찾을 수 없습니다!")

# ✅ pymongo로 MongoDB에 연결
client = MongoClient(MONGODB_URL)

# ✅ 사용할 데이터베이스 및 컬렉션
db = client["scent_db"]
scent_collection = db["fragrances"]
