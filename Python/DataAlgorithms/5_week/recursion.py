def recursion(x):
    if x == 0:
        return 1
    else:
        return recursion(x-1) + recursion(x-1)

print(recursion(0))
print(recursion(1))
print(recursion(10))
print(recursion(15))
