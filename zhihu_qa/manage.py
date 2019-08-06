from flask_script import Manager
#终端操作
from flask_migrate import Migrate,MigrateCommand
from exts import db
from app import app
#用户模型映射到数据库的表中
from models import User,Question,Answer


manager = Manager(app)
#使用Migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令道manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()