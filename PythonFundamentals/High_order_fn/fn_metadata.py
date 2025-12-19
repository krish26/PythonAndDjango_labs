import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f'calling {func.__name__}') 
        return func(*args,**kwargs)
    return wrapper

@my_decorator
def greet(name):
    print(f'hello , {name}')

greet('koumudi')