#模型
# 一般在这里面存储建立数据库的类。
from exts import db
from datetime import datetime
class User(db.Model):
    __tablename__= 'user'#表明
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Question(db.Model):
    __tablename__= 'question'#表明
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    #now()获取的是服务器第一次运行的时间，所以所有数据时间都是一样的
    #now就是每次创建一个模型的时候，都获取当前的实际
    create_time = db.Column(db.DateTime,default=datetime.now())
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref = db.backref('questions'))


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime,default=datetime.now)
    question = db.relationship('Question',backref=db.backref('answers',order_by = id.desc()))
    author = db.relationship('User',backref = db.backref('answers'))
