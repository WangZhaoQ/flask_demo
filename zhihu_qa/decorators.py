from functools import wraps
from flask import session,redirect,url_for
#登录限制的装饰器
def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs) #如果没有一个变量来接受func的返回值，那么必须在前面加上return
        else:
            return redirect(url_for('login'))
    return wrapper