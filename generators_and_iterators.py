# Generator fuction
def large_error_log(file_path):
    with open(file_path) as file:
        for line in file:
            if "Error" in line:
                yield line.strip()

for err in large_error_log("error_log.txt"):
    print(err)

# Generator Syntactic sugar [Lazy - and waits till used]
squares = (x * x for x in range(10_000_000))
for s in squares:
    print(s)
    if s > 130:
        break

print("--------")

# Function version of squares generator
def sqr_gen_yiel():
    for x in range(100):
        yield x * x

for s in sqr_gen_yiel():
    print(s)
    if s > 100:
        break

import time

# Forced to calculate right now
start = time.perf_counter()
squares2 = [x * x for x in range(10_000_000)]
print(f"Took {time.perf_counter() - start:.4f}s.")

# Did not calculate and waiting for explicitly being used
start = time.perf_counter()
squares3 = (x * x for x in range(10_000_000))
print(f"Took {time.perf_counter() - start:.4f}s.")