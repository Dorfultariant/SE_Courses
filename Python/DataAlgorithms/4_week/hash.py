
def hash(S, B):
    sum = 0
    for ch in S:
        sum += ord(ch)

    return sum % B

def hashnum(N, B):
    return N % B

def hashfloor(K, M):
    return int(K / M)


hassi = [ "dog", "cat", "bird", "worm", "fish", "cow", "wolf", "fox", "seal", "fly"]
hassi_kakonen = [91,103,79,247,9]
hassi_kolmonen = [27, 32, 15, 77, 6, 11, 22, 45, 99, 40]

for element in hassi_kolmonen:
    print(element,hashfloor(element, 10))
