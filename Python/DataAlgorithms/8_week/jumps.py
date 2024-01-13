#import math

def jumps(n, a, b):
    numberOfSolutions = 0
    for i in range(n // b + 1):
        aStepper = n - i * b
        if aStepper % a == 0:
            bStepper = i
            numberOfSolutions += nCr(aStepper // a + bStepper, bStepper)
    return numberOfSolutions

def nCr(n, r):
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= n - i
        denominator *= i + 1
    return numerator // denominator

if __name__ == "__main__":

    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937
