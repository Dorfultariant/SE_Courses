def sales(cars, customers):
    sortedA = sorted(cars)
    sortedB = sorted(customers)
    print(sortedA)
    print(sortedB)
    counter = 0
    if len(cars) < len(customers):
        up = len(cars)
    else:
        up = len(customers)
    length = len(sortedB)
    for i in range(up):
        j=0
        while j < len(sortedB):
            if sortedA[i] <= sortedB[j]:
                counter += 1
                sortedB.pop(j)
                break
            j += 1


    return counter

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5
