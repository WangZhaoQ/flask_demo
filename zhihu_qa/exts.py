# db
# 因为数据库的操作中再项目名.py和model.py中会形成循环引用，所以我们通多exts.py消除循环引用
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

