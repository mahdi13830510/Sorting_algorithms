import math

def main():
    ...


def get_input():
    ...


def Mearge_Sort(A, p, r):
    
    def Merge(A, p, q, r):
        nL = q - p + 1
        nR = r - q

        L = []
        R = []

        for i in range(nL - 1):
            L.append(A[p + 1])

        for j in range(nR - 1):
            R.append(A[q + j + 1])
        
        i = 0
        j = 0
        k = p

        while i < nL and j < nR:
            
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            
            
            elif A[k] == R[j]:
                j += 1
            
            k += 1

        while i < nL:
            A[k] = L[i]
            i += 1
            k += 1


        while j < nR:
            A[k] = R[j]
            j += 1
            k += 1

    if p >= r:
        return

    q = math.ceil((p + r) / 2)
    Merge_Sort(A, p, q)
    Merge_Sort(A, q + 1, r)

    Merge(A, p, q, r)



def Insertion_Sort(A):
    
    for i in range(len(A), 2):
        key = A[i]
        j = i - 1
        
        while (j > 0) and A[j] > key:
            A[j] = key
            j -= 1
        
        A[j + 1] = key
    
    return A


def Heap_Sort(A):
    def Max_Heapify(A, i):
        LEFT = (lambda x: 2 * x)
        RIGHT = (lambda x: 2 * x + 1)
        l = LEFT(i)
        r = RIGHT(i)

        if l <= len(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= len(A) and A[r] > A[largest]:
            largest = r
        if largest != i:
            temp = A[i]
            A[i] = A[largest]
            A[largest] = temp
            Max_Heapify(A, largest)

    def Build_Max_Heap(A, n):
        A = A[:n]
        for i in range(math.ceil(n / 2), 0, -1):
            Max_Heapify(A, i)

    Build_Max_Heap(A, n)
    for i in range(n, 1, -1):
        temp = A[1]
        A[1] = A[i]
        A[i] = temp
        A1 = A[:-1]
        Max_Heapify(A1, 1)

               
def Quick_Sort(A, p, r):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(r - 1, p):
            if A[j] <= x:
                i += 1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        temp = A[i + 1]
        A[i + 1] = A[r]
        A[r] = temp
        return (i + 1)

    if p < r:
        q = partition(A, p, r)
        Quick_Sort(A, p, q - 1)
        Quick_Sort(A, q + 1, r)


def Selection_Sort(A):
    ...

def Radix_Sort(A):
    ...

def Counting_Sort(A):
    ...



if __name__ == '__main__':
    main()
