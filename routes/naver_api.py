from fastapi import APIRouter, Query
from services.naver_client import search_naver_shopping
import urllib.parse

router = APIRouter()

@router.get("/search")
def search_from_naver(query: str = Query(..., description="검색할 키워드")):
    """
    네이버 쇼핑 API를 통해 키워드 검색 결과를 반환합니다.
    """
    print(f"🧪 [네이버 검색 요청] 받은 쿼리: {query}")

    # 한 번 디코딩해보기 (예: %ED... → 한글)
    decoded_query = urllib.parse.unquote(query)
    print(f"✅ 디코딩된 쿼리: {decoded_query}")

    return search_naver_shopping(decoded_query)