class Zamowienie:
    def __init__(self,
                 numer_zamowienia: str,
                 id: str,
                 kwota_za_m2: float,
                 cena: float):
        self._numer_zamowienia = numer_zamowienia
        self._id = id
        self._kwota_za_m2 = kwota_za_m2
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
    def kwota_za_m2(self) -> None:
        return self._kwota_za_m2

    @kwota_za_m2.setter
    def kwota_za_m2(self, value: float):
        self._kwota_za_m2 = value

    @property
    def cena(self) -> None:
        return self._cena

    @cena.setter
    def cena(self, value: float):
        self._cena = value

    def __str__(self):
        return f'Numer zamówienia: {self.numer_zamowienia}, ' \
               f'Id zamówienia: {self.id}, ' \
               f'Kwota za m2: {self.kwota_za_m2}, ' \
               f'Cena zamówienia: {self.cena}.'
