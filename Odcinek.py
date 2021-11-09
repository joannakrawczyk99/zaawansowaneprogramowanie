class Odcinek:

    def __init__(self,
                 odleglosc: float,
                 miejscowosc_poczatkowa: str,
                 miejscowosc_docelowa: str,
                 miejscowosc_posrednia: str,
                 idn_odcinka: str):
        self.odleglosc = odleglosc
        self.miejscowosc_poczatkowa = miejscowosc_poczatkowa
        self.miejscowosc_docelowa = miejscowosc_docelowa
        self.miejscowosc_posrednia = miejscowosc_posrednia
        self.idn_odcinka = idn_odcinka

    @property
    def odleglosc(self) -> None:
        return self.odleglosc

    @property
    def miejscowosc_poczatkowa(self) -> None:
        return self.miejscowosc_poczatkowa

    @property
    def miejscowosc_docelowa(self) -> None:
        return self.miejscowosc_docelowa

    @property
    def miejscowosc_posrednia(self) -> None:
        return self.miejscowosc_posrednia

    @property
    def idn_odcinka(self) -> None:
        return self.idn_odcinka

    def __init__(self,
                 odleglosc: float,
                 miejscowosc_poczatkowa: str,
                 miejscowosc_docelowa: str,
                 miejscowosc_posrednia: str,
                 idn_odcinka: str):
        self.odleglosc = odleglosc
        self.miejscowosc_poczatkowa = miejscowosc_poczatkowa
        self.miejscowosc_docelowa = miejscowosc_docelowa
        self.miejscowosc_posrednia = miejscowosc_posrednia
        self.idn_odcinka = idn_odcinka

    def __str__(self):
        return f'Odległość: {self.odleglosc}, ' \
               f'Miejscowość początkowa: {self.miejscowosc_poczatkowa}, ' \
               f'Miejscowość docelowa: {self.miejscowosc_docelowa}, ' \
               f'Miejscowość pośrednia: {self.miejscowosc_posrednia}, ' \
               f'Identyfikator odcinka: {self.idn_odcinka}.'
