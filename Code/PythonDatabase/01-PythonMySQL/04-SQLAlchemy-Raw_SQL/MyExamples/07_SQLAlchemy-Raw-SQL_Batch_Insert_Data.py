# 文件名：07_SQLAlchemy-Raw-SQL_Batch_Insert_Data.py
# 功能说明：通过SQLAlchemy-Raw-SQL（MySQL+PyMySQL）向数据库的数据表中批量插入数据记录

#-------------------------------------------------------------------------
# 一、导入SQLAlchemy模块中相关的函数
#-------------------------------------------------------------------------
from sqlalchemy import create_engine

#-------------------------------------------------------------------------
# 二、建立初步连接（此时尚未真正连接MySQL数据库）
#-------------------------------------------------------------------------
# 定义数据库名
DB_NAME = 'mydb'         
# 定义数据库连接路径DB_URL 
DB_URL = "mysql+pymysql://myuser:mypasswd@127.0.0.1:3306/{}?charset=utf8mb4".format(DB_NAME)
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
    print('连接数据库{}成功！'.format(DB_NAME))
except: # 如果连接失败，则给出失败提示
    print('连接数据库{}失败！'.format(DB_NAME))
    
#----------------------------------------------------------------------------
# 四、定义Raw SQL语句（插入数据记录）
#----------------------------------------------------------------------------
TABLE_NAME = 'mytable'
# 定义SQL语句（ 批量插入数据记录）
sql_str = 'INSERT INTO {} (name, url) VALUES(%s, %s)'.format(TABLE_NAME)
# 定义多条记录变量
var_data = [('Google', 'https://www.google.com'),
            ('GitHub', 'https://www.github.com'),
            ('Baidu', 'https://www.baidu.com')]

#----------------------------------------------------------------------------
# 五、执行SQL语句（插入多条数据记录）
#----------------------------------------------------------------------------
try:
    res_obj = myconn.execute(sql_str, var_data)
    print('从数据表{}中成功插入'.format(TABLE_NAME), res_obj.rowcount, '条数据记录！')
except: # 如果插入数据记录失败，则给出失败提示
    print('从数据表{}中批量插入数据记录失败！'.format(TABLE_NAME))