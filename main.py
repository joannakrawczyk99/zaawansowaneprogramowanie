from Zamowienie import Zamowienie

if __name__ == '__main__':
    z = Zamowienie("123", "321", [1, 2, 3], [1000000, 12000000, 50000])
    print(z)
    print(z.sumuj_m2())
    print(z.sumuj_cena())
