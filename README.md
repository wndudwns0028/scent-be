# 향수 추천 서비스 백엔드 API

사용자가 좋아하는 향을 기준으로 제품을 분류하는 서비스의 백엔드 API 서버입니다.

## ✨ 주요 기능

- 제품별 향 정보 조회, 필터링
- Naver 쇼핑 API를 연동한 정보 제공

## 🛠️ 기술 스택

- **Framework**: FastAPI
- **Database**: MongoDB
- **Server**: Uvicorn
- **Environment Management**: python-dotenv
- **Linting/Formatting**: flake8, black

## 🚀 프로젝트 설정 및 실행

### 1. 저장소 복제

```bash
git clone https://github.com/your-username/fragrance-be.git
cd fragrance-be
```

### 2. 가상 환경 생성 및 활성화

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env.template` 파일을 복사하여 `.env` 파일을 생성하고, 아래와 같이 환경에 맞는 값을 입력합니다.

```bash
cp .env.template .env
```

**`.env` 파일 내용:**

```
MONGODB_URI=mongodb://your_mongodb_uri
NAVER_CLIENT_ID=your_naver_client_id
NAVER_CLIENT_SECRET=your_naver_client_secret
```

### 5. 서버 실행

```bash
uvicorn main:app --reload
```

서버가 정상적으로 실행되면 `http://127.0.0.1:8000` 주소로 접속할 수 있습니다.
API 문서는 `http://127.0.0.1:8000/docs` 에서 확인 가능합니다.

## 📁 프로젝트 구조

```
.
├── app/            # FastAPI 애플리케이션 설정
├── crud/           # 데이터베이스 CRUD(생성, 읽기, 수정, 삭제) 로직
├── database/       # 데이터베이스 연결 및 설정
├── models/         # 데이터 모델 및 스키마 (Pydantic)
├── routes/         # API 라우터 및 엔드포인트 정의
├── services/       # 외부 서비스(e.g., Naver API) 클라이언트
├── main.py         # 애플리케이션 진입점
├── requirements.txt # Python 의존성 목록
└── README.md       # 프로젝트 설명 파일
```

## 📝 주요 API 엔드포인트

- `GET /fragrances`: 모든 제품 리스트를 조회합니다.
- `GET /search/naver?query={keyword}`: Naver 쇼핑에서 키워드로 상품을 검색합니다.

> 전체 API 명세는 서버 실행 후 `/docs` 경로에서 확인해주세요.