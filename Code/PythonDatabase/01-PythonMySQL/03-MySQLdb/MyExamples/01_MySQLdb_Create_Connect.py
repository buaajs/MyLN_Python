# 文件名：01_MySQLdb_Create_Connect.py
# 功能说明：通过MySQLdb驱动接口创建与MySQL Server的连接

#-------------------------------------------------------------------------
# 一、导入MySQLdb模块中相关的部分
#-------------------------------------------------------------------------
import MySQLdb.cursors

#-------------------------------------------------------------------------
# 二、建立与MySQL的连接
#-------------------------------------------------------------------------
try:
	# 创建连接对象myconn
    myconn = MySQLdb.connect(
		user="myuser",
	    passwd="mypasswd",
		host="127.0.0.1",
        charset='utf8mb4',
        cursorclass=MySQLdb.cursors.DictCursor
		)
    print("连接MySQL Server成功！")
except MySQLdb.Error as err:
    # 如果连接失败，则给出连接失败相应提示
    print('连接MySQL Server失败!————{}'.format(err))
finally:    # 关闭连接myconn
    myconn.close()    