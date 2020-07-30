# 文件名：04_PyMySQL_Create_Table.py
# 功能说明：通过PyMySQL驱动接口创建数据库中的数据表

#-------------------------------------------------------------------------
# 一、导入PyMySQL模块中相关的部分
#-------------------------------------------------------------------------
import pymysql.cursors

#-------------------------------------------------------------------------
# 二、建立与PyMySQL数据库的连接
#-------------------------------------------------------------------------
# 定义数据库名和数据表名
DB_NAME = 'mydb'
TABLE_NAME = 'mytable'
try:
	# 创建连接对象myconn
    myconn = pymysql.connect(
		user="myuser",
	    passwd="mypasswd",
		host="127.0.0.1",
        database=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
		)
    print('连接数据库{}成功！'.format(DB_NAME))
except pymysql.Error as err:
    # 如果连接失败，则给出连接失败相应提示
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