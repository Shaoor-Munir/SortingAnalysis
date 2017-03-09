import  random
def merge(A, B, left, mid, right):

    comparisons = 0
    exchanges = 0


    i = left
    j = mid+1
    k = left

    while i <= mid and j <= right:
        if(A[i] <=  A[j]):
            comparisons+=1
            B[k] = A[i]
            exchanges+=1
            i+=1
            k+=1
        else:
            B[k] = A[j]
            exchanges+=1
            j+=1
            k+=1

    while i <= mid:
        B[k] = A[i]
        exchanges+=1
        i+=1
        k+=1

    while j <= right:
        B[k] = A[j]
        exchanges+=1
        j += 1
        k += 1

    return comparisons, exchanges

def merge_pass(A, B, segment_size, length):

    comparisons = 0
    exchanges = 0

    i = 0

    while i <= length - 2*segment_size:
        c1, e1= merge(A, B, i, i+segment_size-1, i+2*segment_size-1)
        comparisons+=c1
        exchanges+=e1
        i = i + 2*segment_size

    if(i+segment_size<length):
        c1, e1 = merge(A, B, i, i+segment_size-1, length-1)
        comparisons+=c1
        exchanges+=e1
    else:
        j = i

        while j<=length-1:
            B[j] = A[j]
            exchanges+=1
            j+=1

    return comparisons, exchanges

def merge_sort (A):

    comparisons = 0
    exchanges = 0

    segment_size = 1

    length = len(A)

    B = [0] * length

    while segment_size < length:

        c1, e1 = merge_pass(A, B, segment_size, length)

        comparisons+=c1
        exchanges+=e1

        segment_size +=segment_size

        c1, e1 = merge_pass(B, A, segment_size, length)

        comparisons+=c1
        exchanges+=e1

        segment_size+=segment_size

    return comparisons, exchanges