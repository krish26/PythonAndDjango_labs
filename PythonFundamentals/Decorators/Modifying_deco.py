def greeting(func):
    def wrapper(*args,**kwargs):
       # print(f'Hellooooo!! {func.__name__} , have a good day')
        return f'Helloo {func(*args,**kwargs)}  have a good day'
    return wrapper

@greeting
def fun1(name):
    return name.upper()

print(fun1('Auro'))

        