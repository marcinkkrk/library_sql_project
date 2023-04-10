from ksiazka import Ksiazka
from insert_ksiazka_data import dodaj_ksiazke
from insert_autor_data import dodaj_autora
from check_autor_id import filtr
from insert_regal_data import dodaj_regal
from check_regal_id import filtr2

x = Ksiazka.dodaj()

print(x)
dodaj_autora(x[0], x[1])
dodaj_regal(x[7], x[8], x[9])

idautora = next(filtr(x[0], x[1]))
idmiejsca = next(filtr2(x[7], x[8], x[9]))
            #(autor, tytul,oprawa, isbn, strony, stan, idmiejsca)
dodaj_ksiazke(idautora, x[2], x[3], x[4], x[5], x[6], idmiejsca)