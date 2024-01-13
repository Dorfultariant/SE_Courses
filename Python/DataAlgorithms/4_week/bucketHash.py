class HashBucket:


    def __init__(self, M, B):
        self.tableSize = M
        self.buckets = B
        self.overFlow = [] #[None] * M
        self.itemsPerBucket = int(M / B)
        self.hashTable = [[None for i in range(self.itemsPerBucket)] for j in range(B)]
        #self.hashTable = [[None]*self.itemsPerBucket]*B

    def hashlin(self, strToHash):
        sum = 0
        for char in strToHash:
            sum += ord(char)
        return sum % self.buckets

    def valueInMatrix(self, strToFind):
        return any(strToFind in sub for sub in self.hashTable)


    def insert(self, strToInsert):
        hashed = self.hashlin(strToInsert)

        i = 0

        # If str already exists in the hashTable, return as dublicates are not allowed
        if self.valueInMatrix(strToInsert):
            return

        for i in range(self.itemsPerBucket):
            if self.hashTable[hashed][i] == None:
                self.hashTable[hashed][i] = strToInsert
                return

        # limits the size of overFlow array
        if len(self.overFlow) == self.tableSize:
            return

        self.overFlow.append(strToInsert)

        return

    def delete(self, strToDelete):

        hashed = self.hashlin(strToDelete)

        for i in range(self.itemsPerBucket):
            if self.hashTable[hashed][i] == strToDelete:
                self.hashTable[hashed][i] = None
                return

        if strToDelete in self.overFlow:
            self.overFlow.remove(strToDelete)
        return

    def print(self):
        for item in self.hashTable:
            for i in range(self.itemsPerBucket):
                if item[i] != None:
                    print(item[i],sep="", end=" ")
        for item in self.overFlow:
            if item != None:
                print(item,sep="", end=" ")

        print()


if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1
