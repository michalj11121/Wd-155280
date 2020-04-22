class Foo:
    
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index +2
        return self.data[self.index]

a=Foo("broda")
for i in range(0,len(a.data)):
    if i%2==0:
        print(next(a))

b=Foo("zdjecie")
print("\n")
for i in range(0,len(b.data)):
    if i%2==0:
        print(next(b))




