# ZADANIE 1

# A = [ 1/x for x in range (1,11) ]
# print(A)
# B = [ pow(2,x) for x in range(0,11) ]
# print(B)

#ZADANIE 2

# import random 
# X = [[ random.randint(1,9) for i in range (0,4)]  for y in range (0,4) ] 
# for i in X :
#     print(i)
# Y = [ X[i][i] for i in range(0,4) ]  
# print(Y)

#ZADANIE 3

# lista = {"mleko":"sztuki","maslo":"sztuki","jablka":"kg","mieso":"kg"}
# print(lista)
# X = [ x for x,y in lista.items() if y == "sztuki" ]
# print(X)


#ZADANIE 4

# def foo(a,b):
    
#     if a == 0:
#         print("Funkcja jest stała")
#     elif a < 0:
#         print("Funkcja jest malejąca")
#     elif a > 0:
#         print("Funkcja jest rosnąca")

# print("y=ax+b")
# a = int(input("Podaj a"))
# b = int(input("Podaj b"))
# foo(a,b)

#ZADANIE 5

# def foo(a1,b1,a2,b2):
#     if a1 == a2:
#         print("funkcje są równoległe")
#     elif a1 * a2 == -1:
#         print("funkcje sa prostopadłe")
#     else :
#         print("funckje nie są ani prostopadłe ani równoległe")

# print("y=a1x+b1 Podaj a1,b1 ")
# a1 = int(input())
# b1 = int(input())
# print("y=a2x+b2 Podaj a2,b21 ")
# a2 = int(input())
# b2 = int(input())
# foo(a1,b2,a2,b2)

# ZADANIE 6

# import math
# def foo(x = 8,y = 8,a = 4,b =5 ):
#   return math.sqrt(pow(x-a,2)+pow(y-b,2))
# print(foo())

# ZADANIE 7

# import math
# def foo(a = 3,b = 4,c = 1):
#   return math.sqrt(pow(a,2)+pow(b,2))
# print(foo())

# ZADANIE 8

# def foo(a1 = 1,r = 1,ile = 10):
#   wynik = 0
#   for i in range(0,ile):
#     wynik = wynik + a1
#     a1 += r
#   return wynik
# print(foo())

#ZADANIE 9

# def foo(*elementy):
#   wynik=1
#   for i in elementy:
#     wynik*=i
#   return wynik
# print(foo(1,2,3,4,5))

#ZADANIE 10

# def foo(**produkty):
#   wynik = 0
#   for i in produkty.values():
#     wynik += i
#   return (f"ilosc produktow to {wynik}")
# print(foo(mleko = 3,chleb = 2,maslo = 3,makaron = 100,papier = 1000000))

# ZADANIE 10

# from zespolone import *
# print(jeden.dod(3+5j,3+5j))
# print(dwa.uroj(3+5j))

# ZADANIE 11

from ciagi import *
print(arytm.suma())
print(geo.ciag())



