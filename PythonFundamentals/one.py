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

"""




num=[1,2,3,4]

def even(num):
    return num %2==0

result=filter(even,num)
print(list(result))




   
    



   

    

    






