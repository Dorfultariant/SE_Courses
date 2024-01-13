def sums(items):
    # Create a set with first item of items -list
    foundSums = set([items[0]])

    for number in items:
        # For each iteration new sum set is created and after each iteration, the foundSums is updated, removing dublicates
        newSums = set()
        for foundSum in foundSums:
            # accumulating the foundSums set, number is added to each sum
            newSums.add(foundSum + number)
        ## This updates the foundSums set with unique sums getting rid of dublicates
        foundSums.update(newSums)

    return len(foundSums) -1


if __name__=="__main__":
    #print(sums([1, 2, 3]))                  # 6
    #print(sums([2, 2, 3]))                  # 5
    #print(sums([1, 3, 5, 1, 3, 5]))         # 18
    #print(sums([1, 15, 5, 23, 100, 55, 2])) # 121


    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
