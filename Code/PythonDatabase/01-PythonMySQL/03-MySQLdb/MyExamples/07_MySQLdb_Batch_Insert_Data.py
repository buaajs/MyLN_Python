# 文件名：07_MySQLdb_Batch_Insert_Data.py
# 功能说明：通过MySQLdb驱动接口批量插入数据库中的数据表的数据记录

#-------------------------------------------------------------------------
# 一、导入MySQLdb模块中相关的部分
#-------------------------------------------------------------------------
import MySQLdb.cursors

#-------------------------------------------------------------------------
# 二、建立与MySQL数据库的连接
#-------------------------------------------------------------------------
# 定义数据库名 和 数据表名
DB_NAME = 'mydb'
TABLE_NAME = 'mytable'
try:
	# 创建连接对象myconn
    myconn = MySQLdb.connect(
		user="myuser",
	    passwd="mypasswd",
		host="127.0.0.1",
        database=DB_NAME,
        charset='utf8mb4',
        cursorclass=MySQLdb.cursors.DictCursor
		)
    print('连接数据库{}成功！'.format(DB_NAME))
except MySQLdb.Error as err:
    # 如果连接失败，则给出连接失败相应提示
    print('连接数据库{}失败!————{}'.format(DB_NAME, err))


#-------------------------------------------------------------------------
# 三、创建游标对象
#-------------------------------------------------------------------------
mycursor = myconn.cursor()

#-------------------------------------------------------------------------
# 四、定义SQL语句（插入数据记录）
#-------------------------------------------------------------------------
sql_str = "INSERT INTO {} (name, url) VALUES (%s, %s)".format(TABLE_NAME)
# 多条记录变量
myval = [('Google', 'https://www.google.com'),
         ('GitHub', 'https://www.github.com'),
         ('Baidu', 'https://www.baidu.com')]

#-------------------------------------------------------------------------
# 五、执行SQL语句
#-------------------------------------------------------------------------
try:
    mycursor.executemany(sql_str, myval)  
    # 提交数据库执行SQL语句
    myconn.commit()             
    print('向数据表{}中成功插入'.format(TABLE_NAME), mycursor.rowcount, '条数据记录！')
except:	# 如果发生错误则回滚
    myconn.rollback()           
    print('向数据表{}中插入数据记录失败！'.format(TABLE_NAME))
finally:    # 关闭游标mycursor和连接myconn
    mycursor.close()
    myconn.close()