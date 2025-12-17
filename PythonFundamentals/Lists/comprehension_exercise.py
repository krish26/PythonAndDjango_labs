my_list=list(range(1,7))
print('list' , my_list)  # creating a list

squares=[n*n for n in my_list]
print(squares)  # list of squates using coprehension

print('evens', [n for n in my_list if n%2==0]) # filtering the evens using comp

dict = {my_list:squares for my_list,squares in zip(my_list,squares) }
print(dict)

def format():
    dict1 = {
        'first_name': 'krishna',
        'middle_name': 'koumudi',
        'last_name': 'koravi'
    }

    fullname = ' '.join(value for value in dict1.values()) # join and comp
    result=f'full name is {fullname}'
    print(result)
format()

def nested():
    matrix=[[c for c in range(3)]for r in range(3)] # creating matrix
    print(matrix)
    print('\n'.join([' '.join([str(c) for c in row]) for row in matrix])) 

nested()







