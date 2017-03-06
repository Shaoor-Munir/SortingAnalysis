

def heapify(A, heapsize, i):
    left =  2*i
    right = 2*i+1
    largest = i

    if left <= len(A) and A[i] > A[largest]:
        largest = left
    if right <= heapsize and A[right] > A[largest]:
        largest = right

    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, heapsize, largest)



def build_heap(A):

    n = len(A)
    n = int(n/2)
    for i in range(n, 1, -1):
        heapify(A, len(A),  i)

def heap_sort(A):
    build_heap(A)
    heap_size = len(A)

    while heap_size > 0:
        A[0], A[heap_size] = A[heap_size], A[0]
        heap_size-=1
        heapify(A, heap_size, 1)


A = [23,3,4,2,3,6,6,5,4,2,11]

print(A)
heap_sort(A)

print(A)

