# 文件名：02_SQLAlchemy_Create_Database.py
# 功能说明：通过SQLAlchemy（MySQL+PyMySQL）创建一个新的MySQL数据库

#-------------------------------------------------------------------------
# 一、导入SQLAlchemy模块中相关的函数
#-------------------------------------------------------------------------
from sqlalchemy import create_engine

#-------------------------------------------------------------------------
# 二、建立初步连接（此时尚未真正连接MySQL数据库）
#-------------------------------------------------------------------------
# 1. 定义数据库连接路径DB_URL (数据库名myolddb)
DB_URL = 'mysql+pymysql://myuser:mypasswd@127.0.0.1:3306/myolddb?charset=utf8mb4'
#-------------------------------------------------------------------------
# 2. 基于数据库连接路径创建引擎实例对象myengine
try:
    myengine = create_engine(DB_URL, max_overflow=10, echo=False)
    print('创建引擎成功！')
except:
    print('创建引擎失败！')

#-------------------------------------------------------------------------
# 三、建立真正连接（此时才真正连接MySQL数据库）
#-------------------------------------------------------------------------
try:    # 创建连接对象myconn
    myconn = myengine.connect()
    print('连接数据库成功！')
except: 
    print('连接数据库失败！')

#-------------------------------------------------------------------------
# 四、定义Raw SQL语句（创建数据库mydb）,如果数据库不存在则创建，存在则不创建; 
#-------------------------------------------------------------------------
sql_str = 'CREATE DATABASE IF NOT EXISTS mydb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'

#-------------------------------------------------------------------------
# 五、执行SQL语句（创建数据库）
#-------------------------------------------------------------------------
try:
    myconn.execute(object_=sql_str)
    print('创建数据库成功！')
except:
    print('创建数据库失败！')