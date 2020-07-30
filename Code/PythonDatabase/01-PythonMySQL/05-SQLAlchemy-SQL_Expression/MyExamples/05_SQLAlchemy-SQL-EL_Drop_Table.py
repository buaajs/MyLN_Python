# 文件名：05_SQLAlchemy-SQL_Expression_Drop_Table.py
# 功能说明：通过SQLAlchemy-SQL_Expression（MySQL+PyMySQL）删除MySQL数据库中的数据表

#-------------------------------------------------------------------------
# 一、导入SQLAlchemy模块中相关的函数
#-------------------------------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String

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
# 三、定义数据表
#----------------------------------------------------------------------------
# 创建一个MetaData对象（通过MetaData类构造函数）
metadata = MetaData()
# 定义数据表（通过Table类构造函数）
mytable = Table('mytable', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(40)),
                Column('url', String(80)),
                )

#----------------------------------------------------------------------------
# 四、删除数据表
#----------------------------------------------------------------------------
try:    # 删除所有定义的数据表
    metadata.drop_all(myengine)
    print('删除数据表成功！')
except:
    print('删除数据表失败！')