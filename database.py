from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'sqlite:///a_m.sqlite3'
DB_URL = 'sqlite:///a_m.sqlite1'

# 데이터베이스에 연결하는 엔진을 생성하는 함수
engine = create_engine(DB_URL, connect_args={'check_same_thread': False})

# 데이터베이스와 상호 작용하는 세션을 생성하는 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy의 선언적 모델링을 위한 기본 클래스
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # 마지막에 무조건 닫음
        db.close()
