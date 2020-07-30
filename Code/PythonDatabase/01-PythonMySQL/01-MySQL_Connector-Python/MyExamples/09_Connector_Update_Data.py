# 文件名：09_Connector_Update_Table.py
# 功能说明：通过MySQL Connector/Python驱动接口修改数据库中的数据表的数据记录

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
# 四、定义SQL语句（删除数据记录）
#-------------------------------------------------------------------------
sql_str = "UPDATE {} set name = %s, url = %s WHERE name = %s".format(TABLE_NAME)
# SQL语句变量
myval = ("Python", "https://www.python.org", "GitHub")

#-------------------------------------------------------------------------
# 五、执行SQL语句
#-------------------------------------------------------------------------
try:
    mycursor.execute(sql_str, myval)  
    # 提交数据库执行SQL语句
    myconn.commit()             
    print('向数据表{}中成功修改'.format(TABLE_NAME), mycursor.rowcount, '条数据记录！')
except:	# 如果发生错误则回滚
    myconn.rollback()           
    print('向数据表{}中修改数据记录失败！'.format(TABLE_NAME))
finally:    # 关闭游标mycursor和连接myconn
    mycursor.close()
    myconn.close()