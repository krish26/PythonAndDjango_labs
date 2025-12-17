numbers = [1,2,3,4,5,6,7,8,9]

squares = []
even= []
doubled =[]
greaterthanfive =[]
addnum= []

for i in numbers:
    squares.append(i * i)
    if i % 2 ==0:
        even.append(i)
    doubled.append(i+i)

    if i > 5:
        greaterthanfive.append(i)

    addnum.append(f'number: {i}')


print(squares)
print(even)
print(doubled)
print(greaterthanfive)
print(addnum)
 #
