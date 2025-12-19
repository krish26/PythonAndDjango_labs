'''
Time.perf_counter()
Time.time()
Timeit module
Cprofile and profile


“Decorating recursive functions distorts 
performance measurement because the decorator executes at every recursive call.”

'''

import time

def Exec_time(func):
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        result=(func(*args,**kwargs))
        end=time.perf_counter()
        elapsed=end-start
        print(f'Time taken is {elapsed:.6f} seconds')  #.3f is sec and millisecond , .6f is sec and microsecond 
        return result
    return wrapper

@Exec_time
def square(n):
    return n * n  

print(square(10000))


def fibonacci(num):
    if num <=1 :
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
#print(fibonacci(100))   # have billions of times its not good decorating recurssive fn is BAD


@Exec_time
def run_fib(n):
    return fibonacci(n)

print(run_fib(20))