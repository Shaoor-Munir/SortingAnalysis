import random


def heapify(A, heapsize, i):
    left =  2*i
    right = 2*i+1
    largest = i

    if left <= heapsize and A[left] > A[largest]:
        largest = left
    if right <= heapsize and A[right] > A[largest]:
        largest = right

    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, heapsize, largest)



def build_heap(A):

    n = len(A)
    n = int(n/2)
    for i in range(n, 0, -1):
        heapify(A, len(A)-1,  i)

def heap_sort(A):
    build_heap(A)
    heap_size = len(A)-1

    while heap_size > 0:
        A[1], A[heap_size] = A[heap_size], A[1]
        heap_size-=1
        heapify(A, heap_size, 1)


A = []

for i in range(20):
    A.append(random.randint(0,100))


print(A)

heap_sort(A)

A.remove(A[0])
print(A)

