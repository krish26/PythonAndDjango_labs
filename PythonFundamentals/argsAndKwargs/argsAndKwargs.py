def sum(*args):
    total=0
    for num in args:
        total += num
    return total

print(sum(1,2,3,4,5,6))
print(sum(99,100))


def max(*args):

    if len(args)==0:
        return 'No max value'
    max_num=args[0]
    for num in args:
        if num>max_num:
            max_num=num
    return max_num
print('the max value is : ' , max(22,1,89))


def any(**kwargs):
    print(kwargs)
any(k=2,b=3,u=9)


def all(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
all(1,2,3,k=0,i=1)






        

