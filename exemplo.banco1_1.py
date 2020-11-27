import mysql.connector
db_connection = mysql.connector.connect(host='localhost', 
user='galvaobueno', password='ronaldinho', database='futebol', port=3306)
cursor = db_connection.cursor()
cursor.execute("select * from time")
for x in cursor:
    print(x)
cursor.close()
db_connection.close()