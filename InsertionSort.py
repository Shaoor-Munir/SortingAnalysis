def insertion_sort(A):
    comparisons = 0
    exchanges = 0

    for i in range(len(A)):
        valueToInsert = A[i]
        j = i
        exchanges += 1
        while j > 0 and A[j - 1] > valueToInsert:
            comparisons+=1
            A[j] = A[j - 1]
            exchanges+=1
            j = j - 1

        A[j] = valueToInsert
        exchanges+=1

    return comparisons, exchanges
