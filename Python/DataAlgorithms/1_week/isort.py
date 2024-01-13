def isort(A):
    Incounter = 0
    Outcounter = 0

    for i in range(len(A)):
        j = i -1
        while (j >= 0) and (A[j] > A[j + 1]):
            A[j], A[j+1] = A[j+1], A[j]
            j = j - 1
            Incounter += 1
        Outcounter += 1
    return A

if __name__ == "__main__": 

    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    B = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    C = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
    D = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]

    print(isort(A))
    print()
    print(isort(B))
    print()
    print(isort(C))
    print()
    print(isort(D))
    print()
