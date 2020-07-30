# 文件名：01_SQLAlchemy_Create_Connect.py
# 功能说明：通过SQLAlchemy（MySQL+PyMySQL）创建与MySQL数据库的连接

#-------------------------------------------------------------------------
# 一、导入SQLAlchemy模块中相关的函数
#-------------------------------------------------------------------------
from sqlalchemy import create_engine

#-------------------------------------------------------------------------
# 二、建立初步连接（此时尚未真正连接MySQL数据库）
#-------------------------------------------------------------------------
# 1. 定义数据库连接路径DB_URL相关变量
DIALECT = 'mysql'           # 定义dialect，如：mysql、postgresql、sqlite等
DRIVER = 'pymysql'          # 定义驱动名，如：mysqldb、pymysql、mysqlconnector等
USERNAME = 'myuser'         # 定义数据库用户名
PASSWORD = 'mypasswd'       # 定义数据库密码
HOSTNAME = '127.0.0.1'      # 定义数据库主机IP地址
PORT = '3306'               # 定义数据库主机端口号
DB_NAME = 'mydb'            # 定义数据库名
# 2. 定义数据库连接路径DB_URL 
DB_URL = "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4".\
    format( dialect=DIALECT, driver=DRIVER, \
            username=USERNAME, password=PASSWORD, \
            host=HOSTNAME, port=PORT, database=DB_NAME)
#-------------------------------------------------------------------------
# 3. 基于数据库连接路径创建引擎实例对象myengine
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