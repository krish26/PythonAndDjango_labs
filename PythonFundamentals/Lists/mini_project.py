name = input('enter your name : ' )
age = input('enter your age : ')
fav_subject=input('enter fav subject : ')
fav_quote=input('enter fav quote : ')

n = name.upper()
list_n= list(n)
print(list_n)

print(list_n[0] , list_n[-1])

print ( f"my name is {n} and i'm {age} years old ,my favourite subject is {fav_subject} and one of my fav quotes is {fav_quote}")
 #