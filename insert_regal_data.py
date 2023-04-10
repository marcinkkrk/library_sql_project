import mysql.connector

def dodaj_regal(regal, polka, miejsce):
    db = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port=3306,database="dbksiazki")
    cursorObject = db.cursor()


    dodaj = "INSERT INTO regaly(regal, polka, miejsce) VALUES(%s,%s,%s);"
    val = (regal, polka, miejsce)
    cursorObject.execute(dodaj,val)
    db.commit()
    db.close()