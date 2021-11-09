class Pojazd:

    def __init__(self,
                 marka: str,
                 dlugosc: float,
                 pojemnosc_bagaznika: float,
                 idn_pojazdu: str,
                 model: str):
        self.marka = marka
        self.dlugosc = dlugosc
        self.pojemnosc_bagaznika = pojemnosc_bagaznika
        self.idn_pojazdu = idn_pojazdu
        self.model = model

    @property
    def marka(self) -> None:
        return self.marka

    @property
    def dlugosc(self) -> None:
        return self.dlugosc

    @property
    def pojemnosc_bagaznika(self) -> None:
        return self.pojemnosc_bagaznika

    @property
    def idn_pojazdu(self) -> None:
        return self.idn_pojazdu

    @property
    def model(self) -> None:
        return self.model

    @marka.setter
    def marka(self, marka: str):
        self.marka = marka

    @dlugosc.setter
    def dlugosc(self, dlugosc: float):
        self.dlugosc = dlugosc

    @pojemnosc_bagaznika.setter
    def pojemnosc_bagaznika(self, pojemnosc_bagaznika: float):
        self.pojemnosc_bagaznika = pojemnosc_bagaznika

    @idn_pojazdu.setter
    def idn_pojazdu(self, idn_pojazdu: str):
        self.idn_pojazdu = idn_pojazdu

    @model.setter
    def model(self, model: str):
        self.model = model

    def __str__(self):
        return f'Marka pojazdu : {self.marka}, ' \
               f'Długość pojazdu: {self.dlugosc}, ' \
               f'Pojemność bagażnika: {self.pojemnosc_bagaznika}, ' \
               f'Identyfikator pojazdu: {self.idn_pojazdu}, ' \
               f'Model: {self.model}.'


