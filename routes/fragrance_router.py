from fastapi import APIRouter, HTTPException
from typing import List
from models.fragrance_schema import FragranceCategory
from database.mongodb import scent_collection

router = APIRouter()

@router.get("/", response_model=List[FragranceCategory])
def get_all_categories():
    docs = list(scent_collection.find({}, {"_id": 0}))
    return docs

@router.get("/{product}", response_model=List[FragranceCategory])
def get_category_by_product(product: str):
    """
    /fragrances/shampoo
    → product='shampoo'
    DB에서 { product:'shampoo' }인 문서 목록
    """
    docs = list(scent_collection.find({"product": product}, {"_id": 0}))
    if not docs:
        raise HTTPException(status_code=404, detail="No data for this product")
    return docs

@router.post("/", response_model=dict)
def add_category(item: FragranceCategory):
    scent_collection.insert_one(item.dict())
    return {"message": "향기 카테고리가 추가되었습니다."}

