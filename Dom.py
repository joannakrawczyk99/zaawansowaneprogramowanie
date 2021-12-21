class Dom:

    def __init__(self,
                 powierzchnia: float,
                 wysokosc: float,
                 ilosc_pieter: float,
                 pokoje: int):
        self._powierzchnia = powierzchnia
        self._wysokosc = wysokosc
        self._ilosc_pieter = ilosc_pieter
        self._pokoje = pokoje

    @property
    def powierzchnia(self) -> None:
        return self._powierzchnia

    @property
    def wysokosc(self) -> None:
        return self._wysokosc

    @property
    def ilosc_pieter(self) -> None:
        return self._ilosc_pieter

    @property
    def pokoje(self) -> None:
        return self._pokoje

    def __str__(self):
        return f'Powierzchnia mieszkania: {self.powierzchnia}, ' \
               f'Wysokość mieszkania: {self.wysokosc}, ' \
               f'Ilość pięter: {self.ilosc_pieter}, ' \
               f'Pokoje: {self.pokoje}.'
