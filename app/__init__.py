# file name : index.py
# pwd : /project_name/app/main/index.py

#from flask import Flask
#from flask import Blueprint, request, render_template, flash, redirect, url_for
#from flask import current_app as app
# 추가할 모듈이 있다면 추가

#main= Blueprint('main', __name__, url_prefix='/')

#@main.route('/main', methods=['GET'])
#def index():
             # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
#             return render_template('/main/index.html')
#bp = Blueprint('main;, __name__, url_prefix='/'')

#@bp.route('/hello')
#def create_app():
#    app = Flask(__name__)

#    from .views import main_views
#    app.register_blueprint(main_views.bp)

#    return app

#@bp.route('/')
#def index():
#    return 'Pybo index'

#def create_app():
#    app = Flask(__name__)

#    @app.route('/')
#    def hello_pybo():
#        return 'Hello, Pybo!'
#    return app

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#from flaskext.markdown import Markdown

from sqlalchemy import MetaData

import config

naming_convention = {
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
        }
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention)) # 전역 변수로 DB 객체 생성
migrate = Migrate() # 전역 변수로 migrate 객체 생성

def create_app(): # 애플리케이션 팩토리
    app = Flask(__name__) # 플라스크 선언
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True) # init_app 메서드를 이용해서 초기화
    else:
        migrate.init_app(app, db) #init_app 메서드를 이용해 초기화
    from . import models # 모델 import

    #Blue print
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views # views 사용을 위해 import
    app.register_blueprint(main_views.bp) # main_views blue print 사용
    app.register_blueprint(question_views.bp) # question_views blue print 사용
    app.register_blueprint(answer_views.bp) # answer_views blue print 사용

    app.register_blueprint(auth_views.bp) # auth_views blue print 사용

    app.register_blueprint(comment_views.bp) # comment_views blue print 사용
    
    app.register_blueprint(vote_views.bp) # vote_views blue print 사용

    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    #Markdown(app, extensions=['nl2br', 'fenced_code'])
    return app

