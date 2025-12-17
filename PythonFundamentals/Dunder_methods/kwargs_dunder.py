class Combi:
    def __init__(self,**kwargs): 
        self.__dict__=kwargs
    
    @property
    def a_value(self):
        return self.a
    
    @a_value.setter
    def a_value(self,x):
        self.a=x

    def __add__(self,other):
        return self.a + other.a
    
    def total(self):
        return sum(n for n in __dict__.values())
    
    def __str__(self):
        return ', '.join(f'{key}={value}' for key,value in self.__dict__.items())
        pass
    
dict1={'a':10,'b':20}
dict2={'a':30,'b':40}

c1=Combi(**dict1)
c2=Combi(**dict2)

print(c1)
print(c1+c2)

c1.get_value=50
print(c1.get_value)




        
        
        