# 베이스 이미지 (Python 3.11 slim 버전 사용)
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY ./app ./app

# 포트 설정 (Streamlit 기본 포트는 8501)
EXPOSE 8786

# 실행 명령
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]

