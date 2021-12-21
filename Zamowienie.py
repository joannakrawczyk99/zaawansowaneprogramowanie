class Zamowienie:
    def __init__(self,
                 numer_zamowienia: str,
                 id: str,
                 m2: list,
                 cena: list):
        self._numer_zamowienia = numer_zamowienia
        self._id = id
        self._m2 = m2
        self._cena = cena

    @property
    def numer_zamowienia(self) -> None:
        return self._numer_zamowienia

    @numer_zamowienia.setter
    def numer_zamowienia(self, value: str):
        self._numer_zamowienia = value

    @property
    def id(self) -> None:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def m2(self) -> None:
        return self._m2

    @m2.setter
    def m2(self, value: list):
        self._m2 = value

    @property
    def cena(self) -> None:
        return self._cena

    @cena.setter
    def cena(self, value: list):
        self._cena = value

    def __str__(self):
        return f'Numer zamówienia: {self.numer_zamowienia}, ' \
               f'Id zamówienia: {self.id}, ' \
               f'M2: {self.m2}, ' \
               f'Ceny: {self.cena}.'

    def sumuj_cena(self):
        suma = 0
        for i in range(len(cena)):
            suma = suma + i
        return round(suma, 2)

    def sumuj_m2(self):
        suma = 0
        for i in range(len(m2)):
            suma = suma + i
        return suma
