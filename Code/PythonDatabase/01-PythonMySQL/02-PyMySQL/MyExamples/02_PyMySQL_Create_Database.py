# 文件名：02_PyMySQL_Create_Database.py
# 功能说明：通过PyMySQL驱动接口创建MySQL数据库

#-------------------------------------------------------------------------
# 一、导入PyMySQL模块中相关的部分
#-------------------------------------------------------------------------
import pymysql.cursors

#-------------------------------------------------------------------------
# 二、建立与MySQL的连接
#-------------------------------------------------------------------------
# 定义数据库名
DB_NAME = 'mydb'
try:
	# 创建连接对象myconn
    myconn = pymysql.connect(
		user="myuser",
	    passwd="mypasswd",
		host="127.0.0.1",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
		)
    print("连接MySQL Server成功！")
except pymysql.Error as err:
    # 如果连接失败，则给出连接失败相应提示
    print('连接MySQL Server失败!————{}'.format(err))

#-------------------------------------------------------------------------
# 三、创建游标对象
#-------------------------------------------------------------------------
mycursor = myconn.cursor()

#-------------------------------------------------------------------------
# 四、定义SQL语句（创建数据库）
#-------------------------------------------------------------------------
# SQL语句（创建数据库）：如果数据库不存在则创建，存在则不创建; 
sql_str = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARSET utf8 COLLATE utf8_general_ci;".format(DB_NAME)

#-------------------------------------------------------------------------
# 五、执行SQL语句
#-------------------------------------------------------------------------
try:
    mycursor.execute(sql_str)  
    # 提交数据库执行SQL语句
    myconn.commit()             
    print('创建数据库{}成功！'.format(DB_NAME))
except:	# 如果发生错误则回滚
    myconn.rollback()           
    print('创建数据库{}失败！'.format(DB_NAME))
finally:    # 关闭游标mycursor和连接myconn
    mycursor.close()
    myconn.close()