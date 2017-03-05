

def merge(A, B):

    mergedArray = []

    while len(A) != 0 and len(B) != 0:
        if A[0] < B[0]:
            mergedArray.append(A[0])
            A.remove(A[0])
        else:
            mergedArray.append(B[0])
            B.remove(B[0])

    if len(A) == 0:
        mergedArray += B
    else:
        mergedArray += A

    return mergedArray


def merge_sort(A):
    if len(A) == 0 or len(A) == 1:
        return A
    else:
        mid = int(len(A) / 2)
        firstHalf = merge_sort(A[:mid])
        secondHalf = merge_sort(A[mid:])

        return merge(firstHalf, secondHalf)
