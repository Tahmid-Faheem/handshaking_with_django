import time
import functools

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        span = end - start
        print(f"Function {func.__name__} took {span}s")
        return result
    return wrapper


@timed
def processing(n):
    mul = 0
    for _ in range(n):
        for _1 in range(n):
            mul *= n


processing(10000)


def retry(times = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
            raise last_exc
        return wrapper
    return decorator

@retry(times = 5)
def fun(c):
    print("Hey")
    b = 0
    a = b / c

fun(2)
fun(0) #intentional