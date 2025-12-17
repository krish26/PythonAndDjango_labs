class Base:
    def __init__(self,a):
        self.__a=a
        

b1=Base(100)
print(b1._Base__a) # mangling
