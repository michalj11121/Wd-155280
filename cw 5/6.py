class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

a=Wspak("lody")

for i in range(0,len(a.data)):
    print(next(a),end='')
    
b=Wspak("parapet")
print("\n")
for i in range(0,len(b.data)):
    print(next(b),end='')

