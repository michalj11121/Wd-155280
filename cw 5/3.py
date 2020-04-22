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
    def __gt__(self,other):
        pass
    def __ge__(self,other):
        pass
    def __le__(self,other):
        pass
    def __lt__(self,other):
        pass
        
a=Kwadrat(6)
b=Kwadrat(5)
c=a.obwod()!=b.obwod()
d=a.obwod()>b.obwod()
e=a.obwod()<b.obwod()
f=a.obwod()<=b.obwod()
print(d)
print(c)
print(e)
print(f)