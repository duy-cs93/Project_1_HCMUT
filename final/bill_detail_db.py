import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM bill_detail "       
			row = cursor.execute(sql)
			print ("select all")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def select(bill_code,product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM bill_detail WHERE bill_code = %s AND product_code = %s"       
			row = cursor.execute(sql,(bill_code,product_code))
			print ("select")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def insert(bill_code,product_code,product_quantity,into_money):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO bill_detail VALUES (%s,%s,%s,%s);"       
			cursor.execute(sql,(bill_code,product_code,product_quantity,into_money))
			connection.commit()
			print('insert')                 
	finally:     
		connection.close()


def update(bill_code,product_code,product_quantity,into_money,old_bill_code,old_product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE bill_detail SET bill_code = %s, product_code = %s, product_quantity = %s, into_money = %s WHERE bill_code = %s AND product_code = %s"       
			cursor.execute(sql,(bill_code,product_code,product_quantity,into_money,old_bill_code,old_product_code))
			connection.commit()
			print('update')                 
	finally:     
		connection.close()		


def delete(bill_code,product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM bill_detail where bill_code = %s AND product_code = %s"
			cursor.execute(sql,(bill_code,product_code))
			connection.commit()
			print('delete')
	finally:
		connection.close()