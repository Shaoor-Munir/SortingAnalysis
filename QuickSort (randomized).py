import random

def partition(A, s, e):
    i = s-1

    for j in range(s, e):
        if(A[j] < A[e]):

            i+=1
            A[i], A[j] = A[j], A[i]

    pivot = i+1
    A[pivot], A[e] = A[e], A[pivot]
    return pivot


def quick_sort(A, s, e):

    if s >= e:
        return A


    pivot = random.randint(s, e)
    A[pivot], A[e] = A[e], A[pivot]
    pivot = e
    pivot = partition(A, s, pivot)

    quick_sort(A, s, pivot-1)
    quick_sort(A, pivot+1, e)

    return


A = [5,3,2,3,5,6,67,3,2,21,100]

print(A)

quick_sort(A, 0, len(A)-1)

print (A)