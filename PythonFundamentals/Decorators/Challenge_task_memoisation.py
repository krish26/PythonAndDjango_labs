from functools import lru_cache
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

def fibonacci(num):
    if num <=1 :
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
@lru_cache(maxsize=None)
@Exec_time   
def run_fib(num):
    return fibonacci(num)
   
print(run_fib(30))
print(run_fib.cache_info())

print('<----------------------time taken without memoisation :--------------------------------------------->')
def fibonacci(num):
    if num <=1 :
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
@Exec_time    
def run_fib(num):
    return fibonacci(num)

print(run_fib(30))




