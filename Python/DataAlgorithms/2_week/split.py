def split(T):
    counter = 0
    for i in range(1,len(T)):
        if max(T[0:i]) < min(T[i:]):
            counter += 1
    return counter


if __name__ == "__main__":
    print("Result ", split([1,2,3,4,5]))       # 4
    print("Result ",split([5,4,3,2,1]))       # 0
    print("Result ",split([2,1,2,5,7,6,9]))   # 3
    print("Result ",split([1,2,3,1]))         # 0

    print("Result ",split([1, 1, 2, 6, 1, 5, 7, 7, 7, 9, 9, 10, 13, 16, 12, 16, 11, 13]))          # 4

    print("Result ",split([1, 6, 4, 1, 2, 2, 2, 6, 6, 13, 12, 7, 10, 19, 15, 17, 17, 17, 19, 18])) # 2
