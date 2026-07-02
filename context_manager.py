# Naive approach
file = open("OOP.py", "r")
try:
    data = file.read(10)
finally:
    file.close()
    
print(data)

# with "with" keyword
with open("OOP.py", "r") as file:
    data = file.read(10)

print(data)

from contextlib import contextmanager

@contextmanager
def execution_timer():
    import time
    start = time.perf_counter()
    print("Beg")
    try:
        print("Before yield")
        yield
        print("After yield")
    finally:
        end = time.perf_counter()
    print(f"Code Block too {end - start:.4f}s time to run.")    


with execution_timer():
    print("Mid")
    sum(i*i for i in range(1000))