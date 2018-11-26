import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM employee "       
			cursor.execute(sql)
			cursor_2 = cursor
			print ("select")
	finally:      
		connection.close()
	return cursor_2


def insert(employee_code,employee_name,employee_sex,employee_address,employee_phone,employee_DOB,employee_FWD,employee_salary):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"       
			cursor.execute(sql,(employee_code,employee_name,employee_sex,employee_address,employee_phone,employee_DOB,employee_FWD,employee_salary))
			connection.commit()
			print('insert')                 
	finally:     
		connection.close()
