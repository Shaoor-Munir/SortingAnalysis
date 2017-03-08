import random
import timeit
import HeapSort
import InsertionSort
import MergeSortIterative
import MergeSortIterative
import QuickSortDeterministic
import QuickSortRandomized

A = []


for i in range (100):
    A.append(random.randint(0, 2**32-1))


start_time = timeit.default_timer()

MergeSortIterative.merge_sort(A)

elapsed = timeit.default_timer() - start_time

print(elapsed)