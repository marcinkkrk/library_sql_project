import mysql.connector

def filtr2(regal, polka, miejsce):
    db = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port=3306,database="dbksiazki")
    cursorObject = db.cursor()


    query = 'SELECT idmiejsca, regal, polka, miejsce FROM regaly WHERE regal ="' + str(regal) + '" and polka="' + str(polka) + '" and miejsce="' + str(miejsce) + '"'
    cursorObject.execute(query)
    wynik = cursorObject.fetchall()[0] [0]
    yield(wynik)
    db.close()