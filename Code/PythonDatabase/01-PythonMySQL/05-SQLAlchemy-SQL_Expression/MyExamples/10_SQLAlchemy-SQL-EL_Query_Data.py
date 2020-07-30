# 文件名：10_SQLAlchemy-SQL_Expression_Query_Data.py
# 功能说明：通过SQLAlchemy-SQL_Expression（MySQL+PyMySQL）查询数据表的数据记录

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
# 四、构造查询数据SQL Expression
#----------------------------------------------------------------------------
sql_select = mytable.select().where(mytable.c.id > 0)

#----------------------------------------------------------------------------
# 五、建立真正连接（此时才真正连接MySQL数据库）
#----------------------------------------------------------------------------
try:    # 创建连接对象myconn
    myconn = myengine.connect()
    # 连接成功给出成功提示
    print('连接数据库成功！')
except: # 如果连接失败，则给出失败提示
    print('连接数据库失败！')
    
#----------------------------------------------------------------------------
# 六、执行SQL语句（查询数据记录）
#----------------------------------------------------------------------------
try:    # 执行SQL语句（查询数据记录）
    myresult = myconn.execute(sql_select)
    # 查询数据记录成功给出提示
    print('从数据表中成功查询', myresult.rowcount, '条数据记录！')
    # 获取所有行 
    resultset = myresult.fetchall()  
    # 遍历结果，并打印满足查询条件的数据记录
    for row in resultset:            
        print(row)    
except: # 如果查询数据记录失败，则给出失败提示
    print('从数据表中查询数据记录失败！')    
finally:# 关闭ResultProxy对象
    myresult.close()