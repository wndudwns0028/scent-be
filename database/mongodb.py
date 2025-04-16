from pymongo import MongoClient

# MongoDB에 연결 (로컬 주소 사용)
client = MongoClient("mongodb://localhost:27017")

# 사용할 데이터베이스
db = client["scent_db"]

# 사용할 컬렉션 (없으면 자동 생성)
scent_collection = db["fragrances"]
