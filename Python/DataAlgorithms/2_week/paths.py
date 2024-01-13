def bachs(n):
    bachs = [0] * (n + 1)
    bachs[0] = 1

    for i in range(1, n + 1):
        bachs[i] += bachs[i - 1]
        bachs[i] += bachs[i - 2]

    return bachs[n]

print(bachs(2))     # 2
print(bachs(3))     # 3
print(bachs(4))     # 5
print(bachs(5))     # 8
print(bachs(6))     # 13
print(bachs(7))     # 21
print(bachs(8))     # 34
print(bachs(9))     # 55
print(bachs(10))    # 89

