
def partition(A, s, pivot):
    i = s-1
    j = s

    while i< pivot and j < pivot:
        if(A[j] > A[pivot]):
            j+=1
        else:
            i+=1
            A[i], A[j] = A[j], A[i]
            j += 1

    pivot = i+1
    A[pivot], A[j] = A[j], A[pivot]
    return pivot


def quick_sort(A, s, e):

    if s >= e:
        return A

    pivot = e
    print (pivot)

    pivot = partition(A, s, pivot)

    quick_sort(A, s, pivot-1)
    quick_sort(A, pivot+1, e)

    return

A = [8,6,7,3,2,1,5,6,7,4]

print(A)

quick_sort(A, 0, len(A)-1)

print(A)