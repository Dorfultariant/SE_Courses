class HashLinear:

    def __init__(self, size):
        self.tableSize = size
        self.hashTable = [None]*size

    def hashlin(self, string):
        sum = 0
        for char in string:
            sum += ord(char)
        return sum % self.tableSize


    def insert(self, strToInsert):

        hashed = self.hashlin(strToInsert)
        start = hashed

        # self.hashTable[hashed] == strToInsert
        if strToInsert in self.hashTable:
            return

        while self.hashTable[hashed] != None:
            hashed += 1
            ## Start from the beginning of table
            if hashed == self.tableSize:
                hashed = 0
            ## Table is full
            if hashed == start:
                return

        self.hashTable[hashed] = strToInsert
        return


    def print(self):
        for item in self.hashTable:
            if item != None:
                print(item," ", end="")
        print()

    def print2(self):
        for item in self.hashTable:
            print(item, " ", end="")
        print()

    def delete(self, strToDelete):
        hashed = self.hashlin(strToDelete)
        if self.hashTable[hashed] == strToDelete:
            self.hashTable[hashed] = None
            return

        start = hashed

        while True:
            hashed += 1
            if hashed == self.tableSize:
                hashed = 0
            if hashed == start:
                break
            if self.hashTable[hashed] == strToDelete:
                self.hashTable[hashed] = None
                break

        return


if __name__ == "__main__":
    # table = HashLinear(8)
    # table.insert("BM40A1500")
    # table.insert("fOo")
    # table.insert("123")
    # table.insert("Bar1")
    # table.insert("10aaaa1")
    # table.insert("BM40A1500")
    # table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    # table.delete("fOo")
    # table.delete("Some arbitary string which is not in the table")
    # table.delete("123")
    # table.print()   # 10aaaa1 BM40A1500 Bar1
    table = HashLinear(10)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print()
    table.delete("buttermilk")
    table.print()
    table.delete("cores")
    table.print()
    table.delete("cheiromegaly")
    table.print()
    table.delete("iodations")
    table.print()
    # table = HashLinear(10)
    # table.print()
    # table.insert("buttermilk")
    # table.print()
    # table.insert("shim")
    # table.print()
    # table.insert("resolvend")
    # table.print()
    # table.insert("cheiromegaly")
    # table.print()
    # print(table.hashlin("premillennialise"))
    # table.insert("premillennialise")
    # table.print()
    # table.insert("finebent")
    # table.print()


