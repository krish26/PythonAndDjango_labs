for i in range(1,20):   #Printing Odd numbers
    if(i %2 !=0):
        print(i,end=' ,')

sum=0
for i in range(1,100):
    sum=sum+i
print("Sum of 1-100 numbers is : " ,sum)  #Printing sum of 100 numbers


num=int(input("Enter a number to get multiplication table : "))
for i in range(1,11):
    mul=i*num
    print(f'{num} X {i} = ', mul)


    