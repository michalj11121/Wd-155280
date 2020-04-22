class Ksztalty:

    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik



class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __add__(self,other):
        wynik=self.x + other.x
        return Kwadrat(wynik)

a=Kwadrat(5)
b=Kwadrat(6)
c=a+b
print(c.obwod())