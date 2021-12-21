class Mieszkanie:

    def __init__(self,
                 powierzchnia: float,
                 wysokosc: float,
                 czynsz: float,
                 pokoje: int):
        self._powierzchnia = powierzchnia
        self._wysokosc = wysokosc
        self._czynsz = czynsz
        self._pokoje = pokoje

    @property
    def powierzchnia(self) -> None:
        return self._powierzchnia

    @property
    def wysokosc(self) -> None:
        return self._wysokosc

    @property
    def czynsz(self) -> None:
        return self._czynsz

    @property
    def pokoje(self) -> None:
        return self._pokoje

    def __str__(self):
        return f'Powierzchnia mieszkania: {self.powierzchnia}, ' \
               f'Wysokość mieszkania: {self.wysokosc}, ' \
               f'Wysokość czynszu: {self.czynsz}, ' \
               f'Pokoje: {self.pokoje}.'
