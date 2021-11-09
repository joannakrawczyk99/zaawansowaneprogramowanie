class Kurs:

    def __init__(self,
                 miejscowosc_poczatkowa: str,
                 miejscowosc_docelowa: str,
                 odleglosc: float,
                 marka_pojazdu: str,
                 idn_kierowcy: str):
        self.miejscowosc_poczatkowa = miejscowosc_poczatkowa
        self.miejscowosc_docelowa = miejscowosc_docelowa
        self.odleglosc = odleglosc
        self.marka_pojazdu = marka_pojazdu
        self.idn_kierowcy = idn_kierowcy

        @property
        def miejscowosc_poczatkowa(self) -> None:
            return self.miejscowosc_poczatkowa

        @property
        def miejscowosc_docelowa(self) -> None:
            return self.miejscowosc_docelowa

        @property
        def odleglosc(self) -> None:
            return self.odleglosc

        @property
        def marka_pojazdu(self) -> None:
            return self.marka_pojazdu

        @property
        def idn_kierowcy(self) -> None:
            return self.idn_kierowcy

        @miejscowosc_poczatkowa.setter
        def miejscowosc_poczatkowa(self, miejscowosc_poczatkowa: str) -> None:
            self.miejscowosc_poczatkowa = miejscowosc_poczatkowa

        @miejscowosc_docelowa.setter
        def miejscowosc_docelowa(self, miejscowosc_docelowa: str) -> None:
            self.miejscowosc_docelowa = miejscowosc_docelowa

        @odleglosc.setter
        def odleglosc(self, odleglosc: list) -> None:
            self.odleglosc = odleglosc

        @marka_pojazdu.setter
        def marka_pojazdu(self, marka_pojazdu: str) -> None:
            self.marka_pojazdu = marka_pojazdu

        @idn_kierowcy.setter
        def idn_kierowcy(self, idn_kierowcy: str) -> None:
            self.idn_kierowcy = idn_kierowcy

    def __str__(self):
         return f'Miejscowość początkowa: {self.miejscowosc_poczatkowa}, ' \
                f'Miejscowość docelowa: {self.miejscowosc_docelowa},' \
                f' Odległość: {self.odleglosc},' \
                f'Marka pojazdu : {self.marka_pojazdu}, ' \
                f'Identyfikatow kierowcy: {self.idn_kierowcy}.'


    def suma_kilometrow(self):
        suma = 0
        for i in range(len(self.odleglosc)):
            suma = suma + self.odleglosc[i]
        return suma

    def marka_pojazdu(self):
        return self.marka_pojazdu


if __name__ == '__main__':
    kurs1 = Kurs("Warszawa", "Katowice", [10, 20, 30], "Fiat", "KIER123")
    print(kurs1)
    print(kurs1.suma_kilometrow())


