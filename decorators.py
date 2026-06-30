"""
Personal insight:
decorators [those starting with @] means a fcuntion that
takes another function as a parameter.

It is the another way of passing a function as a parameter.

E.g: You have

@function
def another_function():
return 0

is literally like:
def function(another_function):
    def wrapper():
        print("Doing something BEFORE the function runs.")
        
        # Calling another_function in between
        result = another_function() 
        
        print("Doing something AFTER the function runs.")
        return result
        
    # 3. It returns the wrapper function ITSELF
    return wrapper
"""

def my_logger(function):
    def wrpapper():
        print("Staring the funcion ---- ")
        function()
        print("Finished the function ----")
    return wrpapper

@my_logger
def fun ():
    print("Running the original function.")

fun()

def do_seomthing_else(original_function):
    return original_function

@do_seomthing_else
def another_function():
    print("This is the secon function.=---")

another_function()

import time
from functools import wraps

def time_deceorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        starting_at = time.time()

        result = func(*args, **kwargs)

        ends_at = time.time()
        print(f"Function {func.__name__} took {ends_at- starting_at:.4f} seconds to complete")
        return result
    return wrapper

@time_deceorator
def process_data():
    time.sleep(1.7)

process_data()