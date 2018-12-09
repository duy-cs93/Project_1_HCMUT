import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM customer "       
			row = cursor.execute(sql)
			print ("select all")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def select(customer_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM customer WHERE customer_code = %s"       
			row = cursor.execute(sql,(customer_code))
			print ("select")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


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

def update(customer_code,customer_name,customer_address,customer_phone,customer_sex,customer_DOB,customer_DOP,old_customer_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE customer SET customer_code = %s, customer_name = %s, customer_address = %s, customer_phone = %s, customer_sex = %s, customer_DOB = %s, customer_DOP = %s WHERE customer_code = %s"       
			cursor.execute(sql,(customer_code,customer_name,customer_address,customer_phone,customer_sex,customer_DOB,customer_DOP,old_customer_code))
			connection.commit()
			print('update')                 
	finally:     
		connection.close()


def delete(customer_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM customer where customer_code = %s"
			cursor.execute(sql,(customer_code))
			connection.commit()
			print('delete')
	finally:
		connection.close()