
def greeting(name=' '):
    '''
    Docstring for greeting
    
    :name: prints name along with a greeting
    '''
    print(f'Hello {name}!! , Have a nice day')
    
greeting('koumudi')  #greeting with name
greeting() # default greting


def addEven(a,b):
    if a%2==0 and b%2==0 :
        return a+b  
    else:
        return 0
even=addEven(2,3)
print(even)




