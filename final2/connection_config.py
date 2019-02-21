import pymysql.cursors  


# HÃ m tráº£ vá»� má»™t connection.
def get_connection():
    # connect to database
	connection = pymysql.connect(host='127.0.0.1',
                             	 user='root',
                             	 password='nhthach95',
                             	 db='sale_management',
                             	 cursorclass=pymysql.cursors.DictCursor)
	return connection
