#Zad.1

# f=open("liczby.txt","w")
# tab=[]
# for i in range (4,101,4):
#  tab.append(i)

# f.writelines(str(tab))

#Zad.2

# f=open("liczby.txt","r")
# a=f.readline()
# print(a)

#Zad.3

# with open("liczby.txt","a") as f:
#    for i in range (0,10):
#        f.write("cos\n")
# with open("liczby.txt","r") as f:
#    for i in f:
#        print(i,end="")

#Zad.4

# class NaZakupy:


#    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
#        self.nazwa_produktu=nazwa_produktu
#        self.ilosc=ilosc
#        self.jednostka_miary=jednostka_miary
#        self.cena_jed=cena_jed

#    def wyświetl_produkt(self):
#        return(self.nazwa_produktu,self.ilosc,self.jednostka_miary,self.cena_jed)

#    def ile_produktu(self):
#        return(self.ilosc,self.jednostka_miary)

#    def ile_kosztuje(self):
#        return int(self.cena_jed)*int(self.ilosc)
#Zad.5

# class ciag:
#     pierwszy=0
#     roznica=0
#     ile=0

#     def wyswietl_dane(self):
#         print(f"pierwszy element={self.pierwszy} ,roznica ciagu={self.roznica}")

#     def pobierz_parametry(self,a,b,c):
#         self.pierwszy=a
#         self.roznica=b
#         self.ile=c

#     def pobierz_element(self,a):
#         pom=self.pierwszy
#         i=0
#         while pom!=a:
#             pom=pom+self.roznica
#             i=i+1
#         return i

#     def policz_sume(self):
#         wynik=0
#         pom=self.pierwszy
#         for i in range (0,self.ile):
#             wynik+=pom
#             pom=pom+self.roznica
#         return wynik

#     def policz_elementy(self):
#         if(self.pierwszy!=0 and self.roznica!=0):
#             pom=self.pierwszy
#             for i in range (0,self.ile):
#                 pom+=self.roznica
#             return pom

# x=ciag()
# x.pobierz_parametry(1,2,3)
# x.wyswietl_dane()
# print(x.pobierz_element(7))
# print(x.policz_sume())
# print(x.policz_elementy())

#Zad.6
# class Slowa:


#    def sprawdz_czy_palindrom(self,slowo):
#        if(slowo==slowo[::-1]):
#            return "slowo jest polindromem"
#        else:
#            return "slowo nie jest polindromem"
#    def sprawdz_czy_anagramy(self,slowo1,slowo2):
#        if(sorted(slowo1)==sorted(slowo2)):
#            return "slowa sa anagrami"
#        else:
#            return "slowa nie sa angrami"
#    def wyświetl_wyrazy(self,slowo1,slowo2):
#        return slowo1,slowo2
#    def sprawdz_czy_metagramy(self,slowo1,slowo2):
#        pom=0
#        for i in range (0,len(slowo1)):
#            if(slowo1[i]!=slowo2[i]):
#                pom=pom+1
#        if(pom==1):
#            return "slowa sa metagramami"
#        else:
#            return "slowa nie sa metagramami"


# a=Slowa()
# print(a.sprawdz_czy_metagramy("mata","tata"))
# print(a.sprawdz_czy_palindrom("kajak"))
# print(a.wyświetl_wyrazy("mata","tata"))
# print(a.sprawdz_czy_anagramy("hak","kha"))

#Zad.7

# class Robaczek:
#    def __init__(self,x,y,krok):
#        self.x=x
#        self.y=y
#        self.krok=krok

#    def idz_w_gore(self,ile_krokow):
#        self.x+=ile_krokow*self.krok

#    def idz_w_dol(self,ile_krokow):
#        self.x-=ile_krokow*self.krok

#    def idz_w_lewo(self,ile_krokow):
#        self.y-=ile_krokow*self.krok

#    def idz_w_prawo(self,ile_krokow):
#        self.y+=ile_krokow*self.krok

#    def pokaz_gdzie_jestes(self):
#        return f"x={self.x} , y={self.y}"

# a=Robaczek(10,10,1)
# a.idz_w_dol(5)
# a.idz_w_gore(2)
# a.idz_w_lewo(5)
# a.idz_w_prawo(2)
# print(a.pokaz_gdzie_jestes())

#Zad.8

# class Robaczek:
#     def __init__(self,x,y,krok):
#        self.x=x
#        self.y=y
#        self.krok=krok

#     def idz_w_gore(self,ile_krokow):
#        self.x+=ile_krokow*self.krok

#     def idz_w_dol(self,ile_krokow):
#        self.x-=ile_krokow*self.krok

#     def idz_w_lewo(self,ile_krokow):
#        self.y-=ile_krokow*self.krok

#     def idz_w_prawo(self,ile_krokow): 
#         self.y+=ile_krokow*self.krok

#     def pokaz_gdzie_jestes(self):
#       return f"x={self.x} , y={self.y}"
#     def __del__(self):
#        print("usuniete")

# a=Robaczek(10,10,1)
# a.idz_w_dol(5)
# a.idz_w_gore(2)
# a.idz_w_lewo(5)
# a.idz_w_prawo(2)
# print(a.pokaz_gdzie_jestes())

