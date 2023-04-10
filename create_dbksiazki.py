import mysql.connector

db = mysql.connector.connect(user='root', password = 'root', host='127.0.0.1', port=3306) #połączenie
cursorObject = db.cursor()  #stworzenie kursora

cursorObject.execute('CREATE DATABASE IF NOT EXISTS dbksiazki')
db.close()