

def merge(A, B):

    comparisons = 0
    exchanges = 0

    mergedArray = []

    while len(A) != 0 and len(B) != 0:
        if A[0] < B[0]:
            mergedArray.append(A[0])
            exchanges+=1
            comparisons+=1
            A.remove(A[0])
        else:
            mergedArray.append(B[0])
            exchanges+=1
            B.remove(B[0])

    if len(A) == 0:
        mergedArray += B
        exchanges+=len(B)
    else:
        mergedArray += A
        exchanges+=len(A)

    return mergedArray, comparisons, exchanges


def merge_sort(A):
    comparisons = 0
    exchanges = 0
    if len(A) == 0 or len(A) == 1:
        return A, comparisons, exchanges
    else:
        mid = int(len(A) / 2)
        c1 = 0
        c2 = 0
        e1 = 0
        e2 = 0
        firstHalf, c1, e1 = merge_sort(A[:mid])
        secondHalf, c2, e2 = merge_sort(A[mid:])

        c3 =0
        e3 =0

        A, c3, e3 = merge(firstHalf, secondHalf)
        return A, c3, e3
