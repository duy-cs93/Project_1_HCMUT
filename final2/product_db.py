import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM product "       
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
			sql = "SELECT * FROM product WHERE product_code = %s"       
			row = cursor.execute(sql,(product_code))
			print ("select")
	finally:      
		connection.close()
	return [cursor.fetchall(), row]


def insert(product_code,product_name,product_category,product_image,product_brand,product_price,product_detail):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO product VALUES (%s,%s,%s,%s,%s,%s,%s);"       
			cursor.execute(sql,(product_code,product_name,product_category,product_image,product_brand,product_price,product_detail))
			connection.commit()
			print('insert')                 
	finally:     
		connection.close()


def update(product_code,product_name,product_category,product_image,product_brand,product_price,product_detail,old_product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "UPDATE product SET product_code = %s, product_name = %s, product_category = %s, product_image = %s, product_brand = %s, product_price = %s, product_detail = %s WHERE product_code = %s"       
			cursor.execute(sql,(product_code,product_name,product_category,product_image,product_brand,product_price,product_detail,old_product_code))
			connection.commit()
			print('update')                 
	finally:     
		connection.close()


def delete(product_code):
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "DELETE FROM product where product_code = %s"
			cursor.execute(sql,(product_code))
			connection.commit()
			print('delete')
	finally:
		connection.close()