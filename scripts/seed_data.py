# seed_data.py
from pymongo import MongoClient

# ✅ MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017")
db = client["scent_db"]  # 사용할 데이터베이스
collection = db["fragrances"]  # 사용할 컬렉션

# ✅ 시드 데이터 정의 (복숭아, 자몽, 레몬, 망고, 딸기 포함)
seed_data = [
    {
        "product": "shampoo",
        "scent": "과일향",
        "scent_slug": "fruity",
        "fragrances": [
            {"name": "복숭아향", "slug": "peach"},
            {"name": "자몽향", "slug": "grapefruit"},
            {"name": "레몬향", "slug": "lemon"},
            {"name": "망고향", "slug": "mango"},
            {"name": "딸기향", "slug": "strawberry"},
        ],
    },
    {
        "product": "shampoo",
        "scent": "플로럴 향",
        "scent_slug": "floral",
        "fragrances": [
            {"name": "로즈향", "slug": "rose"},
            {"name": "라벤더향", "slug": "lavender"},
        ],
    },
    {
        "product": "bodywash",
        "scent": "과일향",
        "scent_slug": "fruity",
        "fragrances": [
            {"name": "복숭아향", "slug": "peach"},
            {"name": "자몽향", "slug": "grapefruit"},
            {"name": "레몬향", "slug": "lemon"},
            {"name": "망고향", "slug": "mango"},
            {"name": "딸기향", "slug": "strawberry"},
        ],
    },
    {
        "product": "bodywash",
        "scent": "우디 향",
        "scent_slug": "woody",
        "fragrances": [
            {"name": "샌달우드향", "slug": "sandalwood"},
            {"name": "시더우드향", "slug": "cedarwood"},
        ],
    },
]

# ✅ 기존 데이터 삭제 및 삽입
collection.delete_many({})
collection.insert_many(seed_data)

print("✅ Seed data inserted successfully.")
