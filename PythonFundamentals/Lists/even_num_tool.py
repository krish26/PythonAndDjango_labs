my_list=input('Enter a list of numbers : ').split()

for n in range (len(my_list)):
    my_list[n] = int(my_list[n])
print('integer list : ' ,my_list)

even_numbers=list(filter(lambda nums:nums%2==0,my_list))
print('List of even numbers : ' ,even_numbers)
print('count of event numbers : ',len(even_numbers))
    



