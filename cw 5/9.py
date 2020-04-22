def Foo(data):
    for index in range (0,len(data),2):
        yield data[index]

a=Foo("broda")
print(next(a))
print(next(a))
print("cos")
print(next(a))