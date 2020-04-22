
            
            

class Foo:
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    def sprawdzanie(self):
        if isinstance(self.data,str)==True:
            return "to string"
        else:
            return "to nie string"

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index == len(self.data):
                raise StopIteration
            
            if(self.data[self.index]=='A' or self.data[self.index]=='a' or self.data[self.index]=='E' or self.data[self.index] =='e' or self.data[self.index]=='I' or self.data[self.index]=='i' or self.data[self.index]=='O' or self.data[self.index]=='o' or self.data[self.index]=='U' or self.data[self.index]=='u'):
                self.index = self.index +1
                return self.data[self.index-1]
            self.index=self.index+1
        

        
        

        
a=Foo("AbbaEbbeIbbi")
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(a.sprawdzanie())



