from dataclasses import dataclass, field
from regal import Regal
from autor import Autor


@dataclass
class Ksiazka:

    _autor:str=field(init=False)
    _tytul:str
    _oprawa:str
    _isbn:int
    _liczba_stron:int
    _stan:str
    _lokalizacja:int=field(init=False)

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self,autor):
        self._autor = autor

    @property
    def tytul(self):
        return (self._tytul)

    @tytul.setter
    def tytul(self,tytul):
        self._tytul = tytul

    @property
    def oprawa(self):
        return self._oprawa

    @oprawa.setter
    def oprawa(self,oprawa):
        self._ooprawa = oprawa

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def liczba_stron(self):
        return self._liczba_stron

    @liczba_stron.setter
    def liczba_stron(self, liczba_stron):
        self._liczba_stron = liczba_stron

    @property
    def stan(self):
        return (self._stan)

    @stan.setter
    def stan(self,stan):
        self._stan = stan


    @property
    def lokalizacja(self):
        return (self._lokalizacja)

    @lokalizacja.setter
    def lokalizacja(self, lokalizacja):
        self._lokalizacja = lokalizacja

    @staticmethod
    def dodaj():
        imie_autora = input("Podaj imie autora: ")
        nazwisko_autora = input("Podaj nazwisko autora: ")
        tytul = input("Podaj tytuł: ")
        oprawa = input("Podaj rodzaj oprawy: ")
        isbn = int(input('Podaj numer isbn: '))
        liczba_stron = int(input('Podaj liczbe stron: '))
        stan = input('Czy wypozyczona? (tak/nie): ')
        regal = input('Podaj regal: ')
        polka = input('Podaj polke: ')
        miejsce = input('Podaj miejsce: ')
        lokalizacja = Regal(regal, polka,  miejsce)
        autor = Autor(imie_autora, nazwisko_autora)
        nowa_ksiazka = Ksiazka(tytul, oprawa, isbn, liczba_stron, stan)
        return [autor.imie, autor.nazwisko, nowa_ksiazka.tytul, nowa_ksiazka.oprawa,
                nowa_ksiazka.isbn, nowa_ksiazka.liczba_stron, nowa_ksiazka.stan, lokalizacja.regal, lokalizacja.polka, lokalizacja.miejsce]


