import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'code.db')) # 데이터 베이스 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy 이벤트 처리 옵션
SECRET_KEY = "dev"
