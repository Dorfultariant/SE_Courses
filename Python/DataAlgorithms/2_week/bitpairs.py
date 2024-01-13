def pairs(s):
    sums = 0
    lastOne = 0
    amountOfOnes = 0
    totalSum = 0

    for i in range(len(s)+1):
        # If the current char is 1 we add to the amount of ones 1
            # and check whether more than 2 ones has been found to calculate sum
        if s[i-1:i] == "1":
            # Ones count is increased
            amountOfOnes += 1
            # The difference between ones times the amount of ones found is summed up
            sums += (i - lastOne) * (amountOfOnes-1)
            totalSum += sums
            # After sum calculation the lastOnes index is stored
            lastOne = i

    return totalSum


if __name__ == "__main__":
    A = "100101"
    B = "101"
    C = "100100111001"
    D = "10001110011"

    print(pairs(A)) # 4
    print(pairs(B)) # 8
    print(pairs(C)) # 71
    print(pairs(D)) # 71
