"""
메인 실행 파일 (FastAPI)
- 서버를 구동하고, 라우터(scent_api.py, naver_api.py)를 등록
- CORS 설정
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

# ✅ .env 파일 로드
load_dotenv()

# 라우터 임포트 (하나로 합쳐진 scent_api)
from routes import scent_api
from routes import naver_api

app = FastAPI()

# ✅ CORS 설정 (Next.js 또는 정적 프론트에서 접근 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:5500", "https://scent-fe.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 통합된 scent_api 라우터 등록
app.include_router(scent_api.router, tags=["Fragrances & Products"])
app.include_router(naver_api.router, prefix="/naver", tags=["Naver"])

# ✅ FastAPI 서버 실행 (개발 환경에서 reload 사용)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
