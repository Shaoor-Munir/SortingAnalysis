import  random
def merge(A, B, left, mid, right):

    i = left
    j = mid+1
    k = left

    while i <= mid and j <= right:
        if(A[i] <=  A[j]):
            B[k] = A[i]
            i+=1
            k+=1
        else:
            B[k] = A[j]
            j+=1
            k+=1

    while i <= mid:
        B[k] = A[i]
        i+=1
        k+=1

    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1

def merge_pass(A, B, segment_size, length):

    i = 0

    while i <= length - 2*segment_size:
        merge(A, B, i, i+segment_size-1, i+2*segment_size-1)
        i = i + 2*segment_size

    if(i+segment_size<length):
        merge(A, B, i, i+segment_size-1, length-1)
    else:
        j = i

        while j<=length-1:
            B[j] = A[j]
            j+=1



def merge_sort (A):

    segment_size = 1

    length = len(A)

    B = [0] * length

    while segment_size < length:

        merge_pass(A, B, segment_size, length)

        segment_size +=segment_size

        merge_pass(B, A, segment_size, length)

        segment_size+=segment_size