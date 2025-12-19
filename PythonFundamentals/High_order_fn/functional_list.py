'''
Built in Higher Order Functions in Python
Python provides several built-in Higher Order Functions such as 
map(), filter() and sorted(), which simplify operations on iterable objects.

'''

my_list=[2,3,4,5,6,7,8]

print(list(map(lambda n: n*n , my_list)))

print(list(filter(lambda n : n%2 ==0 , my_list)))