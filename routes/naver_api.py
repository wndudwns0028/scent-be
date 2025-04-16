# routes/naver.py
from fastapi import APIRouter, Query
from services.naver_client import search_naver_shopping

router = APIRouter()

@router.get("/search")
def search_from_naver(query: str = Query(..., description="검색할 키워드")):
    """
    네이버 쇼핑 API를 통해 키워드 검색 결과를 반환합니다.
    """
    return search_naver_shopping(query)
