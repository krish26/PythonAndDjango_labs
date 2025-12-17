my_list=list(range(-3,5))   # generates a list with positive and negtive numbers

squares=[]
for num in my_list:
    squares.append(num**2)
print(squares)     #squares using loop

print([x**2 for x in my_list]) # squares using list comprehension

positive_num= [x for x in my_list if x>0]
print(positive_num)  #shows positive number

