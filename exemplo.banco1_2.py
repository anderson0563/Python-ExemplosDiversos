import mysql.connector
db_connection = mysql.connector.connect(host='localhost', 
user='galvaobueno', password='ronaldinho', database='futebol', port=3306)
cursor = db_connection.cursor()
cursor.execute("insert into time (`nome`,`atleta`) values (%s, %s)", 
("América", "Romário"))
db_connection.commit()