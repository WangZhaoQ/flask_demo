from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import User,Question,Answer
from exts import db

from decorators import login_required
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

#登录限制的装饰器


@app.route('/')
def index():
    context = {
        # 'questions': Question.query.order_by('-create_time').all() #这方法不行啊
        'questions': Question.query.order_by(Question.create_time.desc()).all()
    }
    return render_template('index.html',**context)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone,User.password==password).first()
        if user:
            #设置cookie,登录的时候保存cookie
            session['user_id'] = user.id
            #如果想在31天内都不需要登录
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '手机号码或者密码错误，请确认后再登录'
@app.route('/regiest/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #手机号码验证，如果被注册了，就不能再注册了
        user = User.query.filter(User.telephone == telephone ).first()
        if user:
            return '该手机号码已经被注册，请更换手机号码'
        else:
            #password1要和password2相等
            if password1 != password2:
                return '两次密码不相等，请核对后再填写'
            else:
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                #如果注册成功，就让页面跳转到登录的页面
                return redirect(url_for('login'))

@app.context_processor
def my_context_processor():
    #判断当前用户是否登录
    # user_id = session['user_id']#如果没有则跑出异常，为了避免跑出异常，选择下一种方法
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}

    return {}#必须要返回字典，即使为空，不然会报错

@app.route('/logout/')
def logout():
    # 删除session_id
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model=Question.query.filter(Question.id == question_id).first()
                #关键字参数是question，则使用question模型中也使用question

    return render_template('detail.html',question=question_model)


@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')
    answer = Answer(content = content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id)
    answer.author = user
    question = Question.query.filter(Question.id==question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))

if __name__ == '__main__':
    app.run()
