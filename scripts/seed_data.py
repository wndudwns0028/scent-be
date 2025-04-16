# scripts/seed_data.py

from pymongo import MongoClient

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017")
db = client["scent_db"]
fragrance_collection = db["fragrances"]

# slug 기반 시드 데이터
seed_data = [
    {
        "product": "shampoo",
        "scent": "과일향",
        "scent_slug": "fruity",
        "fragrances": [
            {"name": "복숭아향", "slug": "peach"},
            {"name": "레몬향", "slug": "lemon"},
            {"name": "망고향", "slug": "mango"}
        ]
    },
    {
        "product": "shampoo",
        "scent": "플로럴 향",
        "scent_slug": "floral",
        "fragrances": [
            {"name": "로즈향", "slug": "rose"},
            {"name": "라벤더향", "slug": "lavender"}
        ]
    },
    {
        "product": "bodywash",
        "scent": "우디 향",
        "scent_slug": "woody",
        "fragrances": [
            {"name": "샌달우드향", "slug": "sandalwood"},
            {"name": "시더우드향", "slug": "cedarwood"}
        ]
    },
    {
        "product": "bodywash",
        "scent": "시트러스 향",
        "scent_slug": "citrus",
        "fragrances": [
            {"name": "오렌지향", "slug": "orange"},
            {"name": "자몽향", "slug": "grapefruit"}
        ]
    }
]

# 기존 데이터 삭제 후 삽입
fragrance_collection.delete_many({})
fragrance_collection.insert_many(seed_data)

print("✅ 슬러그 기반 seed 데이터가 삽입되었습니다!")
