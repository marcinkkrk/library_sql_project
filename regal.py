class Regal:
    def __init__(self, regal, polka, miejsce):
        self.regal = regal
        self.polka = polka
        self.miejsce = miejsce

    @property
    def regal(self):
        return self._regal

    @regal.setter
    def regal(self,regal):
        self._regal = regal

    @property
    def polka(self):
        return self._polka

    @polka.setter
    def polka(self, polka):
        self._polka = polka

    @property
    def miejsce(self):
        return self._miejsce

    @miejsce.setter
    def miejsce(self,miejsce):
        self._miejsce = miejsce
