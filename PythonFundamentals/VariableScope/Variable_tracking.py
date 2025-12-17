x='global variable'

def fun1():
    x='enclosed variable'
    print('this is outermost function ', x)
    

    def fun2():
        x='local variable'
        print('this is inner function ', x)

        def fun3():
            nonlocal x 
            print('this is last function before changing  ', x)
            x='changed by fun3'
            print('aftr changing :' , x)
        fun3()
    fun2()
fun1()