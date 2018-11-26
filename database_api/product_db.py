import pymysql.cursors
import connection_config


def select_all():
	connection = connection_config.get_connection()
	print ("connect successful!!")
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * FROM product "       
			cursor.execute(sql)
			cursor_2 = cursor
			print ("select")
	finally:      
		connection.close()
	return cursor_2


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
