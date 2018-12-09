import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM bill "       
			row = cursor.execute(sql)
			print ("select all")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]

    
def select(bill_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM bill WHERE bill_code = %s"       
			row = cursor.execute(sql,(bill_code))
			print ("select")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def insert(bill_code,employee_code,bill_date,bill_time,customer_code,total_cost,discount,bill_cost,bill_note):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO bill VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"       
			cursor.execute(sql,(bill_code,employee_code,bill_date,bill_time,customer_code,total_cost,discount,bill_cost,bill_note))
			connection.commit()
			print('insert')                 
	finally:     
		connection.close()


def update(bill_code,employee_code,bill_date,bill_time,customer_code,total_cost,discount,bill_cost,bill_note,old_bill_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE bill SET bill_code = %s, employee_code = %s, bill_date = %s, bill_time = %s, customer_code = %s, total_cost = %s, discount = %s, bill_cost = %s, bill_note = %s WHERE bill_code = %s"       
			cursor.execute(sql,(bill_code,employee_code,bill_date,bill_time,customer_code,total_cost,discount,bill_cost,bill_note,old_bill_code))
			connection.commit()
			print('update')                 
	finally:     
		connection.close()


def delete(bill_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM bill where bill_code = %s"
			cursor.execute(sql,(bill_code))
			connection.commit()
			print('delete')
	finally:
		connection.close()