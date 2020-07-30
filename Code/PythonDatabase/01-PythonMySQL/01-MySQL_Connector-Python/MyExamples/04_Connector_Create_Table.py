# 文件名：04_Connector_Create_Table.py
# 功能说明：通过MySQL Connector/Python驱动接口创建数据库中的数据表

#-------------------------------------------------------------------------
# 一、导入MySQL Connector/Python模块中相关的部分
#-------------------------------------------------------------------------
import mysql.connector
from mysql.connector import errorcode

#-------------------------------------------------------------------------
# 二、建立与MySQL的连接
#-------------------------------------------------------------------------
# 定义数据库名和数据表名
DB_NAME = 'mydb'
TABLE_NAME = 'mytable'
try:
	# 创建连接对象myconn
    myconn = mysql.connector.connect(
		user="myuser",
	    passwd="mypasswd",
        database=DB_NAME,
		host="127.0.0.1",
        charset='utf8mb4'
		)
    print('连接数据库{}成功！'.format(DB_NAME))
except mysql.connector.Error as err:
    # 如果连接失败，则给出连接失败相应提示
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('连接数据库{}失败!————用户名或密码有误'.format(DB_NAME))
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('连接数据库{}失败!————数据库不存在'.format(DB_NAME))
    else:
        print('连接数据库{}失败!————{}'.format(DB_NAME, err))

#-------------------------------------------------------------------------
# 三、创建游标对象
#-------------------------------------------------------------------------
mycursor = myconn.cursor()

#-------------------------------------------------------------------------
# 四、定义SQL语句（创建数据表）
#-------------------------------------------------------------------------
sql_str = "CREATE TABLE IF NOT EXISTS {} (name VARCHAR(255), url VARCHAR(255))".format(TABLE_NAME)

#-------------------------------------------------------------------------
# 五、执行SQL语句
#-------------------------------------------------------------------------
try:
    mycursor.execute(sql_str)  
    # 提交数据库执行SQL语句
    myconn.commit()             
    print('创建数据表{}成功！'.format(TABLE_NAME))
except:	# 如果发生错误则回滚
    myconn.rollback()           
    print('创建数据表{}失败！'.format(TABLE_NAME))
finally:    # 关闭游标mycursor和连接myconn
    mycursor.close()
    myconn.close()