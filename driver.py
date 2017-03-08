import random
import timeit

A = []


start_time = timeit.default_timer()

for i in range (1000000):
    A.append(random.randint(0, 2**32-1))

elapsed = timeit.default_timer() - start_time

print(elapsed)