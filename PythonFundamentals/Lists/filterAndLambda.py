my_list=[2,4,1,3,5,7,8,6]
def evenBool(num):
    return num %2==0
evens = filter(evenBool,my_list) # filter(function,iterable)
print(list(evens))

even_lamb= filter(lambda num:num%2==0,my_list) #lambda means fn without def (lambda arg:expression)
print(list(even_lamb))


list_names=['koumudi','auro','kv','k','v']
def charbool(name):
   return len(name) >3 

moreCharName=filter(charbool,list_names)
print(list(moreCharName))

def a(name):  
    return 'a' in name
containsA=filter(a,list_names)
print(list(containsA))  #using filter and def

containsA1 =filter(lambda name: 'a' in name,list_names)
print(list(containsA1))  # using lambda



