import mysql.connector

def filtr(name, surname):
    db = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port=3306,database="dbksiazki")
    cursorObject = db.cursor()


    query = 'SELECT idautor, imie, nazwisko FROM autor WHERE imie ="' + name + '" and nazwisko="' + surname + '"'
    cursorObject.execute(query)
    wynik = cursorObject.fetchall()[0][0]
    print(wynik)
    yield wynik
    db.close()