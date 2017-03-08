import random

def merge(A, start, middle, end):
    mergedArray = []
    l = 0
    r = 0
    i = 0

    while l < (middle - start) and r < (end - middle):
        if A[l] < A[r]:
            mergedArray.append(A[l])
            l+=1
        else:
            mergedArray.append(A[r])
            r+=1

    while r <(end- middle):
        mergedArray.append(A[r])
        r+=1
    while l <(middle -start):
        mergedArray.append(A[l])
        l+=1
    j = start
    while i < len(mergedArray):
        A[j] = mergedArray[i]
        j+=1
        i+=1

def merge_sort(A):
    length = len(A)
    i = 1

    while i < length/2+1:
        j = 1
        while j < len(A):
            min = i+j
            if j+i > length:
                min  = length

            merge(A, (j-1), j , min)
            j+=1

        i+=1

A = []

for i in range(20):
    A.append(random.randint(0, 100))

print(A)

merge_sort(A)

print (A)