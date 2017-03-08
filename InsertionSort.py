def insertion_sort(A):
    for i in range(len(A)):
        valueToInsert = A[i]
        j = i

        while j > 0 and A[j - 1] > valueToInsert:
            A[j] = A[j - 1]
            j = j - 1

        A[j] = valueToInsert

    return A
