class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

x=isinstance(jozek,Osoba)
y=isinstance(adrian,Osoba)
print(x)
print(y)
x=isinstance(jozek,Pracownik)
y=isinstance(adrian,Pracownik)
print(x)
print(y)
x=isinstance(jozek,Menadzer)
y=isinstance(adrian,Menadzer)
print(x)
print(y)
Marian=Pracownik("Marian","Nowak","1800")
a=isinstance(Marian,Menadzer)
print(a)
a=issubclass(Menadzer,Pracownik)
print("\n")
print(a)
a=issubclass(Pracownik,Menadzer)
print(a)
a=issubclass(Menadzer,Osoba)
print(a)
a=issubclass(Osoba,Menadzer)
print(a)