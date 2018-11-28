import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM warehouse "       
			cursor.execute(sql)
			cursor_2 = cursor
			print ("select")
	finally:      
		connection.close()
	return cursor_2


def insert(product_code,inventory_number):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO warehouse VALUES (%s,%s);"       
			cursor.execute(sql,(product_code,inventory_number))
			connection.commit()
			print('insert')                 
	finally:     
		connection.close()
