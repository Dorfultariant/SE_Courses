n = 5  # Change 'n' to the desired number of digits
numbers = [0] * (n )  # Initialize an array to store the permutation
included = [False] * (n + 1)  # Initialize an array to keep track of included numbers


def permutations(k):
    if k == n:
        print(numbers)  # Print the current permutation

    else:
        for i in range(1, n+1):
            if not included[i]:
                included[i] = True
                numbers[k] = i
                permutations(k+1)
                included[i] = False


permutations(0)  # Start the permutation generation from the first position

#permutations(80)
#print(numbers)

