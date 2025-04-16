from fastapi import APIRouter, HTTPException
from database.mongodb import db

router = APIRouter()

# 특정 제품의 향기 카테고리 목록 가져오기
@router.get("/{product_name}")
def get_product_categories(product_name: str):
    collection_name = f"{product_name}_scents"
    if collection_name not in db.list_collection_names():
        raise HTTPException(status_code=404, detail="제품 카테고리 없음")

    collection = db[collection_name]
    return list(collection.find({}, {"_id": 0}))

# 특정 scent의 세부 fragrance 목록 가져오기
@router.get("/{product_name}/{scent}")
def get_product_scent_detail(product_name: str, scent: str):
    collection_name = f"{product_name}_scents"
    if collection_name not in db.list_collection_names():
        raise HTTPException(status_code=404, detail="제품 카테고리 없음")

    collection = db[collection_name]
    result = collection.find_one({"scent": scent}, {"_id": 0})
    if result:
        return result

    raise HTTPException(status_code=404, detail="향기 카테고리 없음")
