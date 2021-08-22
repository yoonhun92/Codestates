from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from app.models import Question

bp = Blueprint('main', __name__, url_prefix='/') # blueprint 선언, 이름, 모듈명, URL 프리픽스 값 


@bp.route('/hello') # 
def hello_pybo():
        return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list')) # url_for 기능으로 리다이렉트
        #question_list = Question.query.order_by(Question.create_date.desc()) # 조회 결과 정렬 함수
        #return render_template('question/question_list.html', question_list=question_list) #

#@bp.route('/detail/<int:question_id>/')
#def detail(question_id):
#        question = Question.query.get_or_404(question_id)
#        return render_template('question/question_detail.html', question=question)
