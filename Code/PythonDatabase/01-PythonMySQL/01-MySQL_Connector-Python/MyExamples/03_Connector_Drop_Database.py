# 文件名：03_Connector_Drop_Database.py
# 功能说明：通过MySQL Connector/Python驱动接口删除MySQL数据库

#-------------------------------------------------------------------------
# 一、导入MySQL Connector/Python模块中相关的部分
#-------------------------------------------------------------------------
import mysql.connector
from mysql.connector import errorcode

#-------------------------------------------------------------------------
# 二、建立与MySQL的连接
#-------------------------------------------------------------------------
# 数据库名
DB_NAME = 'mydb'
try:
	# 创建连接对象myconn
    myconn = mysql.connector.connect(
		user="myuser",
	    passwd="mypasswd",
		host="127.0.0.1",
        charset='utf8mb4'
		)
    print("连接MySQL Server成功！")
except mysql.connector.Error as err:
    # 如果连接失败，则给出连接失败相应提示
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("连接MySQL Server失败!————用户名或密码有误")
    else:
        print('连接MySQL Server失败!————{}'.format(err))

#-------------------------------------------------------------------------
# 三、创建游标对象
#-------------------------------------------------------------------------
mycursor = myconn.cursor()

#-------------------------------------------------------------------------
# 四、定义SQL语句（删除数据库）
#-------------------------------------------------------------------------
sql_str = "DROP DATABASE {};".format(DB_NAME)

#-------------------------------------------------------------------------
# 五、执行SQL语句
#-------------------------------------------------------------------------
try:
    mycursor.execute(sql_str)  
    # 提交数据库执行SQL语句
    myconn.commit()             
    print('删除数据库{}成功！'.format(DB_NAME))
except:	# 如果发生错误则回滚
    myconn.rollback()           
    print('删除数据库{}失败！'.format(DB_NAME))
finally:    # 关闭游标mycursor和连接myconn
    mycursor.close()
    myconn.close()