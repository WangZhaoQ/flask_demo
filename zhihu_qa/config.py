import os

# —配置文件。一般数据库配置还有DEBUG的配置之类的卸载这个py文件中


DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '903132103'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhihuqa_demo'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME
                                             ,PASSWORD,HOST,PORT,DATABASE)

# SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False