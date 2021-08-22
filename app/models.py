from app import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model): # Question 모델 생성, 기본 클래스 db.Model 상속
    # db.Column() 사용, 첫 번째 인수 데이터 타입, 나머지는 옵션 설정
    id = db.Column(db.Integer, primary_key=True) # 고유 번호, 기본키 설정
    subject = db.Column(db.String(200), nullable=False) # 제목 db.String() 글자 수 제한
    content = db.Column(db.Text(), nullable=False) # 내용 db.Text() 글자 수 제한 x
    create_date = db.Column(db.DateTime(), nullable=False) # 작성 일시
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))
    # nullable=False Null 값 허용 x

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Answer(db.Model): # Answer 모델 생성, 기본 클래스 db.Model 상속
    # db.Column() 사용, 첫 번째 인수 데이터 타입, 나머지는 옵션 설정
    id = db.Column(db.Integer, primary_key=True) # 고유 번호, 기본 키 설정
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) # db.ForeignKey 사용하여 Question 모델과 연결, ondelete='CASCADE' 삭제 연동 설정, 질문 삭제 시 질문에 달린 답변도 함께 삭제
    question = db.relationship('Question', backref=db.backref('answer_set')) # db.relationship으로 관계 설정, 첫 번째 값 참조할 모델명, 두 번째는 역참조 설정, 질문에서 답변을 거꾸로 참조하는 것을 의미
    content = db.Column(db.Text(), nullable=False) # 내용 db.Text() 글자 수 제한 x
    create_date = db.Column(db.DateTime(), nullable=False) # 작성 일시
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))

