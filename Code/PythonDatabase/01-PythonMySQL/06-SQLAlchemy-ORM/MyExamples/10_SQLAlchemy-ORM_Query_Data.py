# 文件名：10_SQLAlchemy-ORM_Query_Data.py
# 功能说明：通过SQLAlchemy-ORM（MySQL+PyMySQL）查询数据表的数据记录

#-------------------------------------------------------------------------
# 一、导入SQLAlchemy模块中相关的函数
#-------------------------------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
# 四、创建会话（建立起与数据库的真正连接）
#-------------------------------------------------------------------------
# 1. 基于引擎对象myengine创建一个Session类 
Session = sessionmaker(myengine)
# 2. 创建一个Session类实例对象mysession，真正建立起跟当前数据库的连接，
mysession = Session()

#-------------------------------------------------------------------------
# 五、查询数据记录
#-------------------------------------------------------------------------
try:
    # 查询所有id大于2的数据记录，结果按id升序排列
    query_obj = mysession.query(Mytable).filter(Mytable.id>2).order_by(Mytable.id).all()
    # 遍历查询结果，打印符合条件的数据记录
    for rowdata in query_obj:
        print(rowdata.id, rowdata.name, rowdata.url)
except: # 如果更新数据记录失败，则给出失败提示
    print('查询数据记录失败！')
finally:# 关闭会话对象
    mysession.close()        