import random
import timeit
import HeapSort
import InsertionSort
import MergeSortIterative
import MergeSortRecursive
import QuickSortDeterministic
import QuickSortRandomized

A = []

for i in range (100):
    A.append(random.randint(0, 2**32-1))

print("Insertion Sort")
start_time = timeit.default_timer()
InsertionSort.insertion_sort(A)
elapsed = timeit.default_timer() - start_time
print(elapsed)


print("Merge Sort Recursive")
start_time = timeit.default_timer()
A, c, e = MergeSortRecursive.merge_sort(A)
elapsed = timeit.default_timer() - start_time
print(elapsed)
print("Comparisons =", c)
print("Exchanges =", e)


print("Merger Sort Iterative")
start_time = timeit.default_timer()
MergeSortIterative.merge_sort(A)
elapsed = timeit.default_timer() - start_time
print(elapsed)


print("Quick Sort Deterministic")
start_time = timeit.default_timer()
QuickSortDeterministic.quick_sort(A, 0, len(A)-1)
elapsed = timeit.default_timer() - start_time
print(elapsed)


print("Quick Sort Randomized")
start_time = timeit.default_timer()
QuickSortRandomized.quick_sort(A, 0, len(A)-1)
elapsed = timeit.default_timer() - start_time
print(elapsed)


print("Heap Sort")
start_time = timeit.default_timer()
HeapSort.heap_sort(A)
elapsed = timeit.default_timer() - start_time
print(elapsed)
