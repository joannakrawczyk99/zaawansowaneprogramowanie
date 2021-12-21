class Developer:

    def __init__(self,
                 imie: str,
                 nazwisko: str,
                 nazwa_firmy: str,
                 miejscowosc: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nazwa_firmy = nazwa_firmy
        self._miejscowosc = miejscowosc

    @property
    def imie(self) -> None:
        return self._imie

    @property
    def nazwisko(self) -> None:
        return self._nazwisko

    @property
    def nazwa_firmy(self) -> None:
        return self._nazwa_firmy

    @property
    def miejscowosc(self) -> None:
        return self._miejscowosc

    def __str__(self):
        return f'Imię: {self.imie}, ' \
               f'Nazwisko: {self.nazwisko}, ' \
               f'Nazwa firmy: {self.nazwa_firmy}, ' \
               f'Miejscowość: {self.miejscowosc}.'
