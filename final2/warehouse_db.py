import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM warehouse "       
			row = cursor.execute(sql)
			print ("select all")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def select(product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM warehouse WHERE product_code = %s"       
			row = cursor.execute(sql,(product_code))
			print ("select")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


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


def update(product_code,inventory_number,old_product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE warehouse SET product_code = %s, inventory_number = %s WHERE product_code = %s"       
			cursor.execute(sql,(product_code,inventory_number,old_product_code))
			connection.commit()
			print('update')                 
	finally:     
		connection.close()


def delete(product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM warehouse where product_code = %s"
			cursor.execute(sql,(product_code))
			connection.commit()
			print('delete')
	finally:
		connection.close()