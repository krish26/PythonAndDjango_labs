'''

decorator(like): The decorator function now directly accepts the parameter like.
inner(func): This function wraps the actual function func and uses the parameter like within its scope.
wrapper(): The wrapper function is used to call the actual func, and it is returned from the inner function.

'''
from functools import wraps

def Deco_par(num): #decorator  arg
    def Deco_fn(func):  #actual decor
        @wraps(func)
        def wrapper(*args,**kwargs): #wrapper with logic 
            for n in range(num):
                print("warning battery low!!!")
            return func(*args,**kwargs)
        return wrapper
    return Deco_fn

@Deco_par(num=4)

def Alert():
    print('Agasya')

Alert()
