x=10
def fun1():
    x=20
    print('x val is ', x)
    
    def fun2():
        nonlocal x
        print('x value is' , x)
        x=30
        print('x after change',x)
    fun2()
print('global x value ', x)
fun1()