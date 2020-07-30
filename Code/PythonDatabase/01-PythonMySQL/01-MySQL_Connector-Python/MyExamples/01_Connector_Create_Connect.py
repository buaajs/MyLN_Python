# 文件名：01_Connector_Create_Connect.py
# 功能说明：通过MySQL Connector/Python驱动接口创建与MySQL Server的连接

#-------------------------------------------------------------------------
# 一、导入MySQL Connector/Python模块中相关的部分
#-------------------------------------------------------------------------
import mysql.connector
from mysql.connector import errorcode

#-------------------------------------------------------------------------
# 二、建立与MySQL的连接
#-------------------------------------------------------------------------
try:
	# 创建连接对象myconn
    myconn = mysql.connector.connect(
		user="myuser",
	    passwd="mypasswd",
		host="127.0.0.1"
		)
    print("连接MySQL Server成功！")
except mysql.connector.Error as err:
    # 如果连接失败，则给出连接失败相应提示
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("连接MySQL Server失败!————用户名或密码有误")
    else:
        print('连接MySQL Server失败!————{}'.format(err))
finally:    # 关闭连接myconn
    myconn.close()