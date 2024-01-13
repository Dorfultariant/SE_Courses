def changes(A):
    changes = 0
    amountOfSameNumbersInARow = 1

    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            amountOfSameNumbersInARow += 1
            continue
        changes += int(amountOfSameNumbersInARow / 2)
        amountOfSameNumbersInARow = 1

    changes += int(amountOfSameNumbersInARow / 2)
    return changes

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    #print()
    print(changes([1, 2, 3, 4, 5]))     # 0
    #print()
    print(changes([1, 1, 1, 1, 1]))     # 2
