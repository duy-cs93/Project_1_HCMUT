import pymysql.cursors  

# Hàm trả về một connection.
def get_connection():
    #connect to database
	connection = pymysql.connect(host='127.0.0.1',
                             	user='root',
                             	password='admin',                             
                             	db='sale_management',
                             	cursorclass=pymysql.cursors.DictCursor)
	return connection
