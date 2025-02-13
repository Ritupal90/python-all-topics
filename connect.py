import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="9594pal")

print(mydb.connection_id)