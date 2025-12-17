cart=[]


for i in range(1,6):
    item = input(f'Enter item {i} : ')
    cart.append(item)

print("Full cart after adding items : " , cart )
cart.pop(-1)
print("Items remaining after removing last item  " , cart)

print('first and last ele : ' ,cart[0],cart[-1])
  #