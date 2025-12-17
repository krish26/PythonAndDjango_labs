
print('<--------------1----------------->')
v1='global variable'
def v():
    v1='local variable'
    print( v1)
v()
print(v1)

print('<--------------2----------------->')

num=10
def func(num):
    print('value of num is ', num)
    num=20
    print('num value after changing :', num)
func(num)
print('value of num global is still ' , num)


print('<--------------3----------------->')

g1=26

def change_g():
    global g1
    print('globa value: ', g1)
    g1=30
    print('global value changed to ', g1)
change_g()


print('<--------------4----------------->')

n=2
def same():
    n=5
    print('local variable n is used here in fn same() ' , n)
same()
print('global variabe n is used here outside fn' , n)

print('<--------------5----------------->')


x='Global'  # global variable
def outer():
    x='enclosing'

    def inner():
        x='local'
        print("inner ", x)
    inner()
    print('outer ', x)
outer()
print('global', x)


print('<--------------6----------------->')

def outer():
    x=10  # enclosing variable

    def inner():
        nonlocal x
        print('enclosing variable value : ', x)
        x=20
        print('changed enclosing variable value' , x)

    inner()
outer()









