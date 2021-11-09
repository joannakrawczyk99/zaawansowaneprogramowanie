class FirmaTransportowa:

    def __init__(self,
                 nazwa: str,
                 ilosc_pojazdow: int,
                 ilosc_pracownikow: int,
                 kategoria_dzialanosci: str,
                 ilosc_klientow: int):
        self.nazwa = nazwa
        self.ilosc_pojazdow = ilosc_pojazdow
        self.ilosc_pracownikow = ilosc_pracownikow
        self.kategoria_dzialanosci = kategoria_dzialanosci
        self.ilosc_klientow = ilosc_klientow

    @property
    def nazwa(self) -> None:
        return self.nazwa

    @property
    def ilosc_pojazdow(self) -> None:
        return self.ilosc_pojazdow

    @property
    def ilosc_pracownikow(self) -> None:
        return self.ilosc_pracownikow

    @property
    def kategoria_dzialanosci(self) -> None:
        return self.kategoria_dzialanosci

    @property
    def ilosc_klientow(self) -> None:
        return self.ilosc_klientow

    def __init__(self,
                 nazwa: str,
                 ilosc_pojazdow: int,
                 ilosc_pracownikow: int,
                 kategoria_dzialanosci: str,
                 ilosc_klientow: int):
        self.nazwa = nazwa
        self.ilosc_pojazdow = ilosc_pojazdow
        self.ilosc_pracownikow = ilosc_pracownikow
        self.kategoria_dzialanosci = kategoria_dzialanosci
        self.ilosc_klientow = ilosc_klientow

    def __str__(self):
        return f'Nazwa firmy: {self.nazwa}, ' \
               f'Ilość posiadanych pojazdów: {self.ilosc_pojazdow}, ' \
               f'Ilość pracowników: {self.ilosc_pracownikow}, ' \
               f'Kategoria działalności: {self.kategoria_dzialanosci}, ' \
               f'Ilość klientów: {self.ilosc_klientow}.'
