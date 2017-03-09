import random
import timeit
import HeapSort
import InsertionSort
import MergeSortIterative
import MergeSortRecursive
import QuickSortDeterministic
import QuickSortRandomized

A = []



for i in range (1000000):
    A.append(random.randint(0, 2**32-1))


print ("Total comparisons, exchanges and running time for value = 1000 are:")

print("---------Heap Sort--------")

B = A.copy()

start_time = timeit.default_timer()

comparisons, exchanges = HeapSort.heap_sort(B)

total_time = timeit.default_timer() - start_time
print("Total comparisons are ", comparisons, " and total exchanges are ", exchanges)

print("Total time taken is ", total_time)

print("---------Insertion Sort---------")

B = A.copy()


start_time = timeit.default_timer()

#comparisons, exchanges = InsertionSort.insertion_sort(B)

total_time = timeit.default_timer() - start_time

print("Total comparisons are ", comparisons, " and total exchanges are ", exchanges)

print("Total time taken is ", total_time)

print("---------Merge Sort (Recursive)--------")

B = A.copy()

start_time = timeit.default_timer()

B, comparisons, exchanges = MergeSortRecursive.merge_sort(B)

total_time = timeit.default_timer() - start_time

print("Total comparisons are ", comparisons, " and total exchanges are ", exchanges)

print("Total time taken is ", total_time)

print("---------Merge Sort (Iterative)--------")

B = A.copy()

start_time = timeit.default_timer()

comparisons, exchanges = MergeSortIterative.merge_sort(B)

total_time = timeit.default_timer() - start_time

print("Total comparisons are ", comparisons, " and total exchanges are ", exchanges)

print("Total time taken is ", total_time)

print("---------Quick Sort (Deterministic)--------")

B = A.copy()

start_time = timeit.default_timer()

comparisons, exchanges = QuickSortDeterministic.quick_sort(B, 0, len(B)-1)

total_time = timeit.default_timer() - start_time

print("Total comparisons are ", comparisons, " and total exchanges are ", exchanges)

print("Total time taken is ", total_time)

print("---------Quick Sort (Randomized)--------")

B = A.copy()

start_time = timeit.default_timer()

comparisons, exchanges = QuickSortRandomized.quick_sort(B, 0, len(B)-1)

total_time = timeit.default_timer() - start_time

print("Total comparisons are ", comparisons, " and total exchanges are ", exchanges)

print("Total time taken is ", total_time)


print("---------Python--------")

B = A.copy()

start_time = timeit.default_timer()

B.sort()

total_time = timeit.default_timer() - start_time

print("Total time taken is ", total_time)
