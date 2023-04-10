class Autor:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, imie):
        self._imie = imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self._nazwisko = nazwisko


