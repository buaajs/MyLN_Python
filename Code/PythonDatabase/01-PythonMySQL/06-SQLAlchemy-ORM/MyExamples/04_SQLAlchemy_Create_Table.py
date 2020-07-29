# 文件名：04_SQLAlchemy-ORM_Create_Table.py
# 功能说明：通过SQLAlchemy-ORM（MySQL+PyMySQL）创建MySQL数据库中的数据表

#-------------------------------------------------------------------------
# 一、导入SQLAlchemy模块中相关的函数
#-------------------------------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#-------------------------------------------------------------------------
# 二、建立初步连接（此时尚未真正连接MySQL数据库）
#-------------------------------------------------------------------------
# 1. 定义数据库连接路径DB_URL 
DB_URL = 'mysql+pymysql://myuser:mypasswd@127.0.0.1:3306/mydb?charset=utf8mb4'
#-------------------------------------------------------------------------
# 2. 基于数据库连接路径创建引擎实例对象myengine
try:
    myengine = create_engine(DB_URL, max_overflow=10, echo=False)
    print('创建引擎成功！')
except:
    print('创建引擎失败！')

#-------------------------------------------------------------------------
# 三、建立映射
#-------------------------------------------------------------------------
# 1. 根据引擎对象myengine构建一个基类Base
Base = declarative_base(myengine)
#-------------------------------------------------------------------------
# 2. 基于基类Base定义一个映射类Mytable，该类描述了要被映射的数据库表mytable的细节
class Mytable(Base):
    # 类属性__tablename__（对应MySQL中数据表名字mytable）
    __tablename__ = "mytable"

    # Column类实例对象id（对应MySQL数据表中的字段id）：整型类型、主键、自增长
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Column类实例对象name（对应MySQL数据表中的字段name）：长度为40的可变长字符串类型，不能为空
    name = Column(String(40), nullable=False)
    # Column类实例对象url（对应MySQL数据表中的字段url）：长度为40的可变长字符串类型，可以为空
    url = Column(String(80), nullable=True)  

#-------------------------------------------------------------------------
# 四、创建数据表
#-------------------------------------------------------------------------
# 1. 找到基类Base的所有子类（即已经定义的数据表映射类），然后在数据库中创建这些表
try:
    Base.metadata.create_all()
    print('创建数据表成功！')
except:
    print('创建数据表失败！')