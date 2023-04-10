import mysql.connector

def dodaj_ksiazke(autor, tytul,oprawa, isbn, strony, stan, idmiejsca):
    db = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port=3306,database="dbksiazki")
    cursorObject = db.cursor()


    dodaj = "INSERT INTO ksiazki(isbn, tytul, oprawa, strony, stan, idmiejsca, autor) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s);"
    val = (isbn, tytul,oprawa, strony, stan, idmiejsca, autor)
    cursorObject.execute(dodaj,val)
    db.commit()
    db.close()