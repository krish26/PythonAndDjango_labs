"""""

9 dec
my_list=['koumudi',20,100.00,'o',89]
my_list =my_list+ ['new_item']
print(my_list *9)

l=[1,2,3]
l.append("append me !")
popped_item=l.pop(0)
print(popped_item)
print(l[100])

new_list=['a','e','x']
new_list.sort()
print(new_list)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]
print(matrix[0][0])

first_col = [row[0] for row in matrix]
print(first_col)


#10 dec

#dictonary

my_dictonary = {
    1:'value one',
    3:'value two',
    3:'value threee',
    'three' :56,
    4:['name_one' , 'name_two']
}


my_dictonary[4]+=['name_three']

my_dictonary[1] ='updated vaue'
print(my_dictonary)
print(my_dictonary[3].upper()) #value three is printed insted of value two 



new_dictonary={}
new_dictonary['animal'] = 'cat' #added key and value
new_dictonary['answer'] = 100
print(new_dictonary)


nested_dictonary={
    'person1' :{
        'name' : {
            'first' :'krishna',
            'last' :'koravi'
        },
        'age' : 28
    },

    'person2' :{
        'name' : 'koumudi',
        'age' : 28
    },
}
print(nested_dictonary['person1']['name']['last'])
dictonary ={
    'key1':1,
    'key2':2,
    'key3':3
}

print(dictonary.keys()) #gets all keys keys() is a method
print(dictonary.values()) #print values
print(dictonary.items()) #gives values inside a tuple inside list


#tuple

my_tuple =(1,2,3,'koumudi',3)
print(len(my_tuple))
print(my_tuple)
print(my_tuple[-1])
print(my_tuple.index('koumudi'))
print(my_tuple.count(3))


#sets

my_set = {1,2,3,4}
my_set.add(6)
my_set.add(3)

print(my_set)


my_list =[1,1,2,1,3,4,4,5,5,6,6,7,7,8]
print(set(my_list))


#boolen


print(1>2)


#control flow

print(2>1)
print(1<2)
print(1<=1)



print(1 =='1')   #in javascript we can compare a string to int it become true but in python its false 
print('one' =='one') #true
print('hi' =='bye') #false
print (1!=2) #true

#logical operators

print((1<2 and 2<3)) #true
print((1<2 or 3>4))  #true


#indentation & if statment

if 1<2 :
    print('yes')
else:
    print('no')


if 1==2:
    print('first')
elif 3==3:
    print('middle')
else:
    print('last')



#loops

sequence =[1,2,3,4,5]  #list data

for i in sequence:    #i represents every ele. in sequence 
    print(i)


for i in sequence:
    print('yes',end=' ')  # this prints yes 5 times

    
    
    #loop through dictonary

ages = {
    'john':4,
    'doe' :5,
    'moe' :10
}

for key in ages:
    print("this is the key: ", key)
    print("this is the value : " , ages[key] ,'\n')


#tuple unpacking 

mypairs =[(1,10) , (2,3) , (6, 7)]

for tup in mypairs:
    print(tup)

for item1,item2 in mypairs:
    print(item1)
    print(item2)

#if no pairs then there will be type error coz no pairs to unpack

#if 3 values then error coz too many values 





#while loop 

i=1
while i < 5:
    print("i is : {} " .format(i))
    i+=1



s='koumudi'




    

    #11 dec 

    #list comprehension
x=[1,2,3]
out=[]

for item in x:
    out.append(item**2)
x=[1,2,3]

print([item**2 for item in x])


def hello():
    print('hello')

hello()
def giveMeHello():
    return "Hello"

result=giveMeHello()
print(result)


def even(num):  # we can also use if but this is easy 
   
   print(f"im checking to see if {num} is even !")
   print(num % 2 ==0)

even(41)

def helloYou(name='default'):
   return(f'hello {name} , have a nice day !')
result=helloYou('koumudi')
print(result)


#fn to add 2 num only if eeven
def addEvenOnly(num1,num2):
    '''
    Docstring for addEvenOnly
    INPUT : two numbers 
    OUTPUT: False if both numbers are not even ,
    the sum if both numbers are even 
   
    '''
    if(num1 %2 !=0) or (num2%2 !=0):
        return False
    else:
        return (num1+num2)

x=addEvenOnly(1,2)
y=addEvenOnly(2,2)
print(x)
print(y)

#lamda expression or anonimus fn

def timestwi(num):
    return num *2

result =timestwi(10)

    
lambda num:num *2 

my_list=[1,2,3,4,6,7,8,9]

def evenbool(num):
    return num %2 ==0
evens=filter(evenbool,my_list)
print(list(evens))


#with lambda

evens=filter(lambda num: num %2==0,my_list)
print(list(evens))


st='hello my name is koumudi'
st.lower() # these are methods of string not functions
st.upper()
st.split()
 
def fun (*args):
    print(args)
fun()
fun(1)
fun(1,2)


def fun2(a,b, **kwargs): #kwargs give dictonary
    print(a,b)
    print(kwargs)

fun2(1,2,c=10,d=11)

#can use this for cal, passing arg to other fn 
def fun3(a,b, *args , name='koumu' , **kwargs):
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('args={}'.format(args))
    print('name={}'.format(name))
    print('kwargs={}'.format(kwargs))

fun3(1,2,3,name='krishna' , age=28,email='koumudi@email.com')



#12 dec


x=15

def printer():
    x=30
    return x
print(x)
print(printer())
print(x)

#python Scopes

# 1. Name assignment will create or change local names vy default
# 2. Name references search (at most) four scopes, these are: (LEGB rule)
    # Local- Name assigned in any way within a function (def or lambda) and not declared global in that function
    # Enclosing functions - Name in the local scope of any and all enclosing func, inner or outer
    # Global - Names assigned at the top-level of a module file, or declared globaly in a def within a file
    # Built-in - Built-in names, module, range.....(all that is built in)
# 3. Names declared in global and nonlocal statement map assigned names to enclosing module and function scopes


#local
f=lambda x:x**2

#enclosing fn

name='is is global name'

def greet():
    name='kk'

    def hello():
        print('hello',name)
    hello()
greet()

#global scope
print(name)

#build in 

len()
x=50
def fun(x):
    print('x is ', x)
    x=2
    print('change local x to ' , x)
fun(x)
print('x is still', x)



name='is is global name'

def greet():
    name='kk'

    def hello():
        name='not kk'
        print('hello',name)
    hello()
greet()

x=50

def fun():
    global x
    print('this fn is now using global x')
    print('becoz of global x is :',x)
    x=2
    print('ran fun() ahanged global to ' , x)

print('before calling fun() x is ', x)
fun()
print('value of x outside of fun() is ', x)
class sample():
    pass

x= sample()
print(type(x))

class Dog():
    #class obj attribute
    species='mamel'

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

milo=Dog('lab','milo')

# normal way

class Circle:
    pi=3.14
   #Circle get instantiated with radius
    def __init__(self,radius=1):
        self.radius=radius
   
   #area method cal are , use of self
    def area(self):
        return self.radius *self.radius *Circle.pi
    
    #method for resetting radius
    def setRadius(self,radius):
        self.radius=radius

   #method to getting radius
    def getRadius(self):
        return self.radius
    
c=Circle()
c.setRadius(2)
print('Area is ', c.area())


#15 dec

class Circle:
    p1=3.14
    def __init__(self):
        pass

    @property
    def area(self):
        return self.radius * self.radius *Circle.pi
    
    @property
    def radius_value(self):  # getters
        return self.radius
    
    @radius_value.setter
    def radius_value(self,value):
        self.radius=value

c= Circle()
c.radius_value=2

print('radius is : ', c.radius_value)
print('Area is ', c.area)


class Person:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and has {self.email}'

p1=Person('Agasya' , 'kou@gmail.com' , 28)
p2=Person('Auro' , 'Auro@email.com', 33)

print(p1)
print(p2)


class Person:
    def __init__(self,**kwargs):
        self.__dict__=kwargs

    def __str__(self):
        return f'{self.name} is {self.age} years old '
    
p1=Person(name='agasya' , age =28 )
p2=Person(name='auro' , age= 33)   # only works for key value 

print(p1)
print(p2)

class Something:
    def __init__(self,data:dict):
        self.__dict__=data

    def __str__(self):
        str_rep=' ' #empty for available info
        for key,value in self.__dict__.items():
            str_rep+= f'{key} = {value} , '
        return str_rep
    
    def __str__(self):
        str_rep =' '

        return ','.join(f'{key}={value}' for key,value in self.__dict__.items())
    #first write for loop the write key=value 


data_dict1= {
    'a':10,
    'b':20,
    'c':30,
    'name':'ll'
}


s1 = Something(data_dict1)
print(s1)




class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
   
    #string rep of object 
    def __repr__(self):
        return f'Point(x={self.x} , y={self.y})'
    
    def __str__(self):
        return f'Point object with (x={self.x} , y{self.y})'

point1= Point(10,20)
#print(point1.x , point1.y)
print(point1)
print(repr(point1))

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

point1=Point(10,20)
point2=Point(10,20)

print(point1==point2)

#swap code 


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def swap_xy(self):
        self.x,self.y=self.y,self.x
point1=Point(10,20)

point1.swap_xy()
print(point1.x,point1.y)
#---------------------------------------------------------------------------------
#17 dec 

#inheritance

class A:
    def __init__(self,value):
        print(f'In A.__init__ and value is = {value}')
        self.value=value

class B(A):    #B is inheriting from A
    def __init__(self, value):
        print(f'In B.__init__ and value is {value}')
        super().__init__(value)
        self.value+=10

class C(A):
    def __init__(self, value):
        print(f'In C.__init__ and value is {value}')
        super().__init__(value)
        self.value*=4
class D(C,B):  #multiple inheritance
    def __init__(self, value):
        print(f'In D.__init__ and value is {value}')
        super().__init__(value)  # even we use many classes we use one super

d=D(10)   #first looks at D and then its uper b then c and then its super a
print(d.value)  
print(D.mro())  




class Animal:        #base class
    def __init__(self):
        print('Animal created')
    
    def WhoAmI(self):
        print('Animal')
    
    def eat(self):
        print('eating........')

class Dog(Animal):     #derived classs
    def __init__(self):
        print('Dog Created')

    def WhoAmI(self):
        print('Dog')

    def bark(self):
        print("woooof!")

d= Dog()
d.WhoAmI()
d.eat()
d.bark()


class Employee:
    increase =1.04    # all classses hsare this
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    
    def __str__(self):
        return f'Employee name is {self.first_name}{self.last_name}, and earns {self.salary} salary'
    
    def increase_sal(self):
        self.salary=int(self.salary*self.increase)

class Developer(Employee):
    increase =1.10
    def __init__(self, first_name, last_name, salary,prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang=prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'



e1=Employee('Auro','Drake', 45000)
e2=Employee('krishna','koumudi', 40000)

dev1=Developer('carl','season',70000,'python')

print ('before increase:')
print(e1)
print(e2)
print(dev1)

e1.increase_sal()
e2.increase_sal()
dev1.increase_sal()

print('after increase')
print(e1)
print(e2)
print(dev1)

#18 dec 

#polimorphism-many forms 

#one buttor diff devices diff behaviour 


def make_it_upper(s):
    return s.upper()

class shouty:
    def __init__(self,text):
        self.text=text
    def upper(self):
        return self.text.upper() +'!!!'

#print(make_it_upper('hello'))
#print(make_it_upper(shouty('hello')))



#2 types of coding 
#defensive coding - 1. look before you leap 2. easier to ask permission

#1

#if isinstance(x,str):
   # print(x.upper())

#2

def safe_upper(x):
    try:
        return x.upper()
    except AttributeError:
        return str(x).upper()
    
#print(safe_upper('h1'))
#print(safe_upper(123))
#print(safe_upper(shouty('hi')))

#first we define base class 
#we define subclass
#subclasses override methods


class Animal:
    def speak(self):
        raise NotImplementedError   #you must override the method in subclasses 
    
class Dog(Animal):
    def speak(self):
        return "Woof!!"
    
class Cat(Animal):
    def speak(self):
        return "Meowww"

print(Dog().speak())
print(Cat().speak())

#Abstract base class - thse make the rules explicit 
#it has methods that are impl by subclasses 
#it says what methods shoud exixst for the obj


from abc import ABC, abstractmethod 
import json
class Serializer(ABC):
    @abstractmethod    #this is decorator that this method should exixsts in all subclasses
    def serialize(self,obj):
        pass # no impl here subclass is responsible 

class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj)
    

js=JsonSerializer()
print(js.serialize({'name':'kk'}))


class SimpleCsvSerializer(Serializer):
    def serialize(self, obj):
        keys=obj[0].keys()
        lines=[','.join(keys)]
        for row in obj:
            lines.append(",".join(str(row[k])for k in keys))

        return "\n".join(lines)
    
csv=SimpleCsvSerializer()
print(csv.serialize([
    {'name':'koumudi','age':28},
    {'name':'kkkk','age':29}
]))

-------------------------------------------------------------------------------
#imports

#dec 19th 

from math import sqrt as sq # from math library import sqrt fn, can write sq insted of sqrt
import math

from math import*  # its bad because it causes name conflicts

def sqrt(num):
    return 'hello'

print(sqrt(25))   # prints hello because of the fn 

print(math.sqrt(25)) # gets the ans , better to use math.sqrt insted of just importing 




print(sq(25))  # no name ambiquity problem 


#to split a project into several modules 



#decorator 

def my_decorator(func):
    def wrapper():  #wrapper is necessary , 
        print('something happining before fnvis called')
        func()
        print('something happining after fn is called ')
    return wrapper

@my_decorator
def say_hello():
    print('helo')

#call dec fun
say_hello()



#decor with arguments

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print(f'Arguments passed to the fn :{args} {kwargs}')
        result=func(*args,**kwargs)
        print(f'fn returned : {result}')
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b

add(5,10)

#static method 

#dont operate on class data , they act as regular fn they belong to class namespace 

class MathHelper:
    @staticmethod   #does not req self , it will not use any class data so no init method or no self
    def adder(x,y):
        return x+y
    
print(MathHelper.adder(10,2))


#built in decorator 

# @functools.wraps ( saves the metadata )


import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f'calling {func.__name__}') 
        return func(*args,**kwargs)
    return wrapper

@my_decorator
def greet(name):
    print(f'hello , {name}')

greet('koumudi')


#we can pass fn as args to other functions -py is a fnctional programming 
#higher ordered fn 


def apply(func,value):  #higher ordered fn coz it take other fn as arg
    return func(value)

def square(x):
    return x*x

def cube(x):
    return x*x*x


print(apply(square,3))
print(apply(cube,8))

def apply(func,value):  #higher ordered fn coz it take other fn as arg
    return func(value)


def square(x):
    return x*x

sq_lambda = lambda x:x*x
print(sq_lambda(6))
print(square(9))


print(apply(lambda x:x *x +10, 5))
"""




#recurssive fn  & memoization
#recursion can be bad so we use memoization what it does is store values

# can be inefficient for large data , 
#memoization cache the data and reuse if the same input occurs 


def fact(num):
    if num== 0:
        return 1
    return num* fact(num-1)

print(fact(5))




from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(num):
    if num <=1 :
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
print(fibonacci(20))
print(fibonacci.cache_info())






# imports, decorators, recurssive , high order fn , built in dec , 



    




































    