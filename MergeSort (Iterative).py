import  random
def merge(A, left, middle, right):

    i = 0
    j = 0
    k = 0

    n1 = middle - left + 1
    n2 = right - middle

    L = []
    R = []

    while i < n1:
        L.append(A[left+i])
        i+=1
    while j < n2:
        R.append(A[middle+j+1])
        j+=1

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:

        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k += 1


    while i < n1:
        A[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort (A):
    current_size = 1
    starting_index = 0

    length = len(A)

    while current_size <= length-1:
        starting_index = 0

        while starting_index < length-1:

            mid = starting_index + current_size - 1
            ending_index = min(starting_index+2*current_size-1, length-1)

            merge(A, starting_index, mid, ending_index)

            starting_index+=2*current_size

        current_size*=2



A = []

for i in range (10):
    A.append(random.randint(0, 200))

print(A)

merge_sort(A)

print (A)