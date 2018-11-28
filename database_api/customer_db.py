import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM customer "       
			cursor.execute(sql)
			cursor_2 = cursor
			print ("select")
	finally:      
		connection.close()
	return cursor_2


def insert(customer_code,customer_name,customer_address,customer_phone,customer_sex,customer_DOB,customer_DOP):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s);"       
			cursor.execute(sql,(customer_code,customer_name,customer_address,customer_phone,customer_sex,customer_DOB,customer_DOP))
			connection.commit()
			print('insert')                 
	finally:     
		connection.close()
