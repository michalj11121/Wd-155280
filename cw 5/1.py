class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        print(f"rodzaj = {self.rodzaj}")

class Ubrania(Material):
    rozmiar="M"
    kolor="czerwony"
    dla_kogo="damski"
    def wyswietl_dane(self):
        print(f"rozmiar = {self.rozmiar} kolor = {self.kolor} dla kogo = {self.dla_kogo} rodzaj = {self.rodzaj} dlugosc = {self.dlugosc} szerokosc = {self.szerokosc}")

class Sweter(Ubrania):
    rodzaj_swetra="z golfem"
    def wyswielt_dane(self):
        print(f"rozmiar = {self.rozmiar} kolor = {self.kolor} dla kogo = {self.dla_kogo} rodzaj = {self.rodzaj} dlugosc = {self.dlugosc} szerokosc = {self.szerokosc} rodzaj swetra = {self.rodzaj_swetra}")

a=Material("bawelna",10,15)
a.wyswietl_nazwe()
b=Ubrania("welna",15,30)
b.wyswietl_nazwe()
b.wyswietl_dane()
c=Sweter("poliester",15,20)
c.wyswielt_dane()
