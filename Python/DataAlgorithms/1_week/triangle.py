
def triangle(a, b, c):
    sides = sorted([a,b,c])
    if (a <= 0 or b <= 0 or c <= 0 or sides[0] + sides[1] <= sides[2]): return False
    return True

if __name__ == "__main__":
    print(triangle(3,5,4))
    print(triangle(-2,2,3))
    print(triangle(5,9,14))
    print(triangle(-30,120,29))
    print(triangle(2,3,4))
