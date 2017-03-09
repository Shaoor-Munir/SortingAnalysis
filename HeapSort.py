import random


def heapify(A, heapsize, i):
    comparisons = 0
    exchanges = 0

    left =  2*i
    right = 2*i+1
    largest = i

    if left <= heapsize and A[left] > A[largest]:
        comparisons+=1
        largest = left
    if right <= heapsize and A[right] > A[largest]:
        comparisons+=1
        largest = right

    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        exchanges+=1
        c1, e1= heapify(A, heapsize, largest)
        comparisons+=c1
        exchanges+=e1

    return comparisons, exchanges

def build_heap(A):

    comparisons = 0
    exchanges = 0
    n = len(A)
    n = int(n/2)
    for i in range(n, 0, -1):
        c1, e1 = heapify(A, len(A)-1,  i)
        comparisons+=c1
        exchanges+=e1

    return comparisons, exchanges

def heap_sort(A):
    comparisons = 0
    exchanges = 0
    c1, e1 = build_heap(A)
    heap_size = len(A)-1

    while heap_size > 0:
        A[1], A[heap_size] = A[heap_size], A[1]
        exchanges+=1
        heap_size-=1
        c1, e1 = heapify(A, heap_size, 1)
        comparisons+=c1
        exchanges+=e1

    A.remove(A[0])

    return comparisons, exchanges

