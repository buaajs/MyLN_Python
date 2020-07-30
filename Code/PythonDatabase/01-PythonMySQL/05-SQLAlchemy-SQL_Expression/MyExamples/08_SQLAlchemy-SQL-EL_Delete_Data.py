# 文件名：08_SQLAlchemy-SQL_ExpressionDelete_Data.py
# 功能说明：通过SQLAlchemy-SQL_Expression（MySQL+PyMySQL）删除数据表中的数据记录

# 文件名：06_SQLAlchemy-SQL_Expression_Insert_Data.py
# 功能说明：通过SQLAlchemy-SQL_Expression（MySQL+PyMySQL）向数据表中插入数据记录

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
# 四、构造删除数据SQL Expression （若不加where过滤则删除表中所有数据）
#----------------------------------------------------------------------------
sql_delete = mytable.delete().where(mytable.c.name == 'MySQL')

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
# 六、执行SQL语句（删除数据记录）
#----------------------------------------------------------------------------
try:    # 执行SQL语句
    myresult = myconn.execute(sql_delete)
    # 删除数据记录成功给出提示
    print('从数据表中成功删除', myresult.rowcount, '条数据记录！')
except: # 如果插入数据记录失败，则给出失败提示
    print('从数据表中删除数据记录失败！')
finally:# 关闭ResultProxy对象
    myresult.close()    