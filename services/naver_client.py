# services/naver_client.py

import requests
import os

# ▶ 네이버 쇼핑 API 연동을 위한 클라이언트 모듈
# 이 파일은 FastAPI 라우터가 외부 네이버 쇼핑에 요청할 때 사용하는 유틸 역할입니다.

# ✅ 환경변수에서 보안 키 값을 불러옴
# (.env 또는 운영환경에 사전 설정된 값 사용)
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def search_naver_shopping(query: str, display: int = 100):
    """
    네이버 쇼핑 검색 API 호출 함수

    Parameters:
        - query (str): 검색 키워드 (예: 복숭아 샴푸)
        - display (int): 가져올 결과 개수 (기본 10개, 최대 100)

    Returns:
        - dict: 네이버 API의 JSON 응답 결과
    """
    url = "https://openapi.naver.com/v1/search/shop.json"

    # 요청 헤더에 Client ID/Secret 포함
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }

    # 검색 파라미터 구성
    params = {
        "query": query,
        "display": display
    }

    # GET 요청 실행
    res = requests.get(url, headers=headers, params=params)

    # 결과를 JSON 형식으로 반환
    return res.json()
