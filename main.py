"""
메인 실행 파일 (FastAPI)
- 서버를 구동하고, 라우터(fragrances.py)를 등록
- CORS 설정
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

# ✅ .env 파일 로드 (모든 서비스에서 환경변수 사용 가능)
load_dotenv()

# routes 폴더의 라우터들 임포트
from routes import fragrance_router
from routes import products
from routes import naver_api
app = FastAPI()

# CORS 설정 (프론트엔드(Next.js)에서 접근 가능하도록)
# 여기서는 http://localhost:3000만 허용
# 만약 여러 도메인을 허용하거나 테스트용이라면 ["*"]로 변경 가능
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(fragrance_router.router, prefix="/fragrances")
app.include_router(naver_api.router, prefix="/naver", tags=["Naver"])
app.include_router(products.router, prefix="/products", tags=["Products"])

# FastAPI 실행 스크립트
# python main.py로 실행할 경우 아래 조건문이 동작
if __name__ == "__main__":
    # reload=True는 코드 변경 시 자동 재시작 (개발용)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
