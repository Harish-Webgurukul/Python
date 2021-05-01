a=34
b=0
try:
	print("Division is ", a/b)
except ZeroDivisionError:
	print("Cannot divide number by zero")


import pymysql
try:
	conn = pymysql.connect(host='loclhost', user='root', password='password', database=
	'bank')
	myCursor = conn.cursor()
	myCursor.close()
	conn.close()
except Exception as e:
	print("Import pymysql Module", str(e))
except:
	print("Error Occured!")



