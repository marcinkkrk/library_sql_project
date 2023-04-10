import mysql.connector

def dodaj_autora(imie, nazwisko):
    db = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port=3306,database="dbksiazki")
    cursorObject = db.cursor()


    dodaj = "INSERT INTO autor(imie, nazwisko) VALUES(%s,%s);"
    val = (imie,nazwisko)
    cursorObject.execute(dodaj,val)
    db.commit()
    db.close()