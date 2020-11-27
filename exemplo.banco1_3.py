import mysql.connector
db_connection = mysql.connector.connect(host='localhost', 
user='galvaobueno', password='ronaldinho', database='futebol', port=3306)
cursor = db_connection.cursor()
cursor.execute("delete from time where `nome` = %s", ("América",))
db_connection.commit()