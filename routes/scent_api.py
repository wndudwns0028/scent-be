# scent_api.py (fragrances + products 통합)

from fastapi import APIRouter, HTTPException
from typing import List
from models.fragrance_schema import FragranceCategory
from database.mongodb import db, scent_collection

router = APIRouter()

# --------------------------
# GET /fragrances
# 향기 카테고리 전체 조회
# --------------------------
@router.get("/fragrances", response_model=List[FragranceCategory])
def get_all_categories():
    docs = list(scent_collection.find({}, {"_id": 0}))
    return docs

# ------------------------------------
# GET /fragrances/{product}
# 특정 제품의 향기 카테고리 조회
# ------------------------------------
@router.get("/fragrances/{product}", response_model=List[FragranceCategory])
def get_category_by_product(product: str):
    docs = list(scent_collection.find({"product": product}, {"_id": 0}))
    if not docs:
        raise HTTPException(status_code=404, detail="No data for this product")
    return docs

# ---------------------------------------------------------
# GET /products/{product_name}
# 제품의 향기 카테고리 목록 (MongoDB Collection에서 조회)
# ---------------------------------------------------------
@router.get("/products/{product_name}")
def get_product_categories(product_name: str):
    collection_name = f"{product_name}_scents"
    if collection_name not in db.list_collection_names():
        raise HTTPException(status_code=404, detail="제품 카테고리 없음")

    collection = db[collection_name]
    return list(collection.find({}, {"_id": 0}))

# ----------------------------------------------------------------------
# GET /products/{product_name}/{scent}
# 특정 제품의 특정 scent에 대한 fragrance 세부 목록
# ----------------------------------------------------------------------
@router.get("/products/{product_name}/{scent}")
def get_product_scent_detail(product_name: str, scent: str):
    collection_name = f"{product_name}_scents"
    if collection_name not in db.list_collection_names():
        raise HTTPException(status_code=404, detail="제품 카테고리 없음")

    collection = db[collection_name]
    result = collection.find_one({"scent": scent}, {"_id": 0})
    if result:
        return result

    raise HTTPException(status_code=404, detail="향기 카테고리 없음")

# ----------------------------------
# POST /fragrances
# 향기 카테고리 추가
# ----------------------------------
@router.post("/fragrances", response_model=dict)
def add_category(item: FragranceCategory):
    scent_collection.insert_one(item.dict())
    return {"message": "향기 카테고리가 추가되었습니다."}
