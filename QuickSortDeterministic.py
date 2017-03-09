
def partition(A, s, e):
    comparisons = 0
    exchanges = 0
    i = s-1

    for j in range(s, e):
        if(A[j] < A[e]):
            comparisons+=1

            i+=1
            A[i], A[j] = A[j], A[i]
            exchanges+=1

    pivot = i+1
    A[pivot], A[e] = A[e], A[pivot]
    exchanges+=1
    return pivot, comparisons, exchanges


def quick_sort(A, s, e):
    comparisons = 0
    exchanges = 0

    if s >= e:
        return comparisons, exchanges

    pivot = e

    pivot, c1, e1 = partition(A, s, pivot)
    comparisons+=c1
    exchanges+=e1

    c1, e1 = quick_sort(A, s, pivot-1)

    c2, e2 = quick_sort(A, pivot+1, e)

    comparisons+=c1+c2

    exchanges+=e1+e2

    return comparisons, exchanges