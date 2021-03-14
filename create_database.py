
#for creating database "audiolibrary"
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="sunidhi")
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE audiolibrary")

mycursor.execute("SHOW DATABASES")

for db in mycursor:
	print(db)