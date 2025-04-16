# setup_env.py
import os
import shutil
from dotenv import load_dotenv

TEMPLATE_FILE = ".env.template"
ENV_FILE = ".env"

# .env 파일 없으면 생성
if not os.path.exists(ENV_FILE):
    print("📄 .env 파일이 없습니다. 템플릿에서 복사 중...")
    shutil.copyfile(TEMPLATE_FILE, ENV_FILE)
    print("✅ .env 파일이 생성되었습니다! 값을 입력해주세요.")
else:
    print("✅ .env 파일이 이미 존재합니다.")

# .env 로드해서 값 확인
load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")

if not client_id or not client_secret:
    print("⚠️  환경변수가 누락되었습니다. .env 파일을 열어 값을 채워주세요.")
else:
    print("🔐 환경변수 로딩 성공. 네이버 API 설정 완료!")
