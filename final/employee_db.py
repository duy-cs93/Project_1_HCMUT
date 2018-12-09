import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM employee "       
			row = cursor.execute(sql)
			print ("select all")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def select(employee_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM employee WHERE employee_code = %s"       
			row = cursor.execute(sql,(employee_code))
			print ("select")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


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


def update(employee_code,employee_name,employee_sex,employee_address,employee_phone,employee_DOB,employee_FWD,employee_salary,old_employee_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE employee SET employee_code = %s, employee_name = %s, employee_sex = %s, employee_address = %s, employee_phone = %s, employee_DOB = %s, employee_FWD = %s, employee_salary = %s WHERE employee_code = %s"       
			cursor.execute(sql,(employee_code,employee_name,employee_sex,employee_address,employee_phone,employee_DOB,employee_FWD,employee_salary,old_employee_code))
			connection.commit()
			print('update')                 
	finally:     
		connection.close()


def delete(employee_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM employee where employee_code = %s"
			cursor.execute(sql,(employee_code))
			connection.commit()
			print('delete')
	finally:
		connection.close()