class Cal:
    def __init__(self,a): #value is assigned to a
        self.a=a
    
    @property
    def power_cal(self):  #cal property 
        return self.a*self.a
    
    @property
    def num_value(self): 
        return self.a
    
    @num_value.setter
    def num_value(self,value):
        self.a=value

c1=Cal(10)
print('power is' , c1.power_cal)


class Bike:
    def __init__(self,brand,cc,colour):
        self.brand=brand
        self.cc=cc
        self.colour=colour

    def __str__(self):
        return f'The bike is {self.brand} with {self.cc} cc and it is {self.colour} colour'

b1=Bike('honda',500,'black')

print(b1)

class Demo:
    def __init__(self,a):
        self.a=a
    
    def __repr__(self):
        return f'Demo ({self.a})'
             
d1=Demo(10)
print(repr(d1))


class Flexible:
    def __init__(self,**kwrgs):
        self.__dict__=kwrgs

    def __str__(self):
        set_atr=' '
        for key,value in self.__dict__.items():
            set_atr+= f'{key}, {value}'
        return set_atr
    
f1=Flexible(a=10,b=20)
f2=Flexible(name='auro ' , game= 'rivals')

print(f1)
print(f2)



class Myself:
    def __init__(self,name,age,hobby,fav_colour):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.fav_colour=fav_colour
    
    def __str__(self):
        about =' '
        about = ' '.join (f'{key},{value} 'for key,value in self.__dict__.items())
        return(about)
m1=Myself('agasya',28,'gaming','purple')
print(m1)


class Idk:
    def __init__(self, data=dict):
        self.__dict__=data

    def __str__(self):
        return ''.join(f'{key},{value}' for key,value in self.__dict__.items())

data_dict1={
    'a':10,
    'b':20,
    'c':30,
    'name':'ll'
}

i1=Idk(data_dict1)
print(i1)

