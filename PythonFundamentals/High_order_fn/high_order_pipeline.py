def pipeline(value,functions):
    for func in functions:
        value=func(value)   #The same value is passed through each function one by one
    return value

def add_one(x):
    return x+1  #3+1=4

def subTwo(x):
    return x-2  #4-2=2

result=pipeline(13,[add_one,subTwo,lambda x:x*x])  #2*2=4

print(result)


