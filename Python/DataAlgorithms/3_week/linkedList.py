class Node:
    data = None
    link = None

    def __init__(self, data, link):
        self.data = data
        self.link = link

class LinkedList:

    def __init__(self):
        self.start = None
        self.end = None

    def append(self, data):
        if self.start == None:
            self.start = Node(data, None)
            self.end = self.start
        else:
            self.end.link = Node(data, None)
            self.end = self.end.link

    def insert(self, data, index):
        i = 0
        lastNode = None
        curNode = self.start
        while curNode != None:
            if i == index and lastNode != None:
                lastNode.link = Node(data, curNode)
            if i == index and lastNode == None:
                self.start = Node(data, curNode)
            i += 1
            lastNode = curNode
            curNode = curNode.link

    def isort(self):
        lastNode = self.start
        curNode = lastNode.link
        inOrder = True

        while True:
            lastNode = self.start
            curNode = lastNode.link
            inOrder = True
            while (curNode != None):
                if (lastNode.data > curNode.data):
                    lastNode.data, curNode.data = curNode.data, lastNode.data
                    inOrder = False
                lastNode = curNode
                curNode = curNode.link
            if inOrder:
                break;

    def index(self, data):
        i = 0
        curNode = self.start
        while curNode != None:
            if curNode.data == data:
                return i
            i += 1
            curNode = curNode.link
        return -1

    def swap111(self, ii, jj):
        i = 0
        curNode = self.start

        firstFound = None
        secondFound = None
        if ii == jj:
            return

        while curNode != None:
            if i == ii:
                firstFound = curNode
            if i == jj:
                secondFound = curNode
            i += 1
            curNode = curNode.link

        if firstFound != None and secondFound != None:
            firstFound.data, secondFound.data = secondFound.data, firstFound.data

    def swap(self, i, j):
        if i == j:
            return
        selectedNode = self.start
        position = 0
        swap1 = None
        swap2 = None
        # check if index is 0
        if position == i:
            swap1 = self.start
            print("Whaaat")
        else:
            # we cycle through the list until we find the index
            while (selectedNode.link != None):
                if position + 1 == i:
                    swap1 = selectedNode.link
                if position + 1 == j:
                    swap2 = selectedNode.link

                position += 1
                selectedNode = selectedNode.link

            # check if the index is in the list
            if swap1 == None or swap2 == None:
                return

        swap1.data, swap2.data = swap2.data, swap1.data


    def swap2(self, ii, jj):
        i = 0
        curNode = self.start
        firstFound = None
        secondFound = None

        if ii == jj:
            return
        if ii == 0:
            print("first")
            firstFound = self.start
        if jj == 0:
            print("second")
            secondFound = self.start

        while curNode != None:
            if i+1 == ii and curNode.link != None:
                firstFound = curNode
            if i+1 == jj and curNode.link != None:
                print("second")
                secondFound = curNode
            i += 1
            curNode = curNode.link

        if firstFound == None or secondFound == None:
            return

        print(firstFound.link.data)
        print(secondFound.link.data)


    def valueOf(self, index):
        i = 0
        curNode = self.start
        while curNode != None:
            if i == index:
                print(curNode.data)
            i += 1
            curNode = curNode.link



    def delete(self, index):
        removed = None
        i = 0
        lastNode = None
        curNode = self.start
        while curNode != None:
            if i == index and lastNode != None:
                lastNode.link = curNode.link
                removed = curNode
            if i == index and lastNode == None:
                self.start = curNode.link
                removed = curNode
            i += 1
            lastNode = curNode
            curNode = curNode.link

        if removed == None:
            return removed
        return removed.data

    def print(self):
        node = self.start
        while node != None:
            print(node.data, end="")
            node = node.link
            if node != None:
                print(" -> ", end="")
        print()


if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    #print(L.index(7))   # 3
    #print(L.index(9))   # -1

    L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    L.swap(1, 3)
    L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6
    #L.swap(2, 0)
#L.print()           # 2 -> 8 -> 3 -> 7 -> 5 -> 10 -> 6


# for num in reversed(range(100000)):
#     L.append(num)

    #L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6


# L.isort()
    #L.swap2(1, 4)
   #L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6
   # L.print()           # 2 -> 8 -> 3 -> 7 -> 5 -> 10 -> 6


    #L = LinkedList()
    #L.append(1)
    #L.append(3)
    #L.print()           # 1 -> 3
    #L.insert(10, 1)
    #L.insert(15, 0)
    #L.print()           # 15 -> 1 -> 10 -> 3
    #L.delete(0)
    #L.print()           # 1 -> 10 -> 3

    # L3 = LinkedList()
    # L3.append(15)
    # L3.append(21)
    # L3.append(11)
    # L3.append(36)
    # L3.append(37)
    # L3.append(25)
    # L3.print()              # 15 -> 21 -> 11 -> 36 -> 37 -> 25
    #
    # L3.insert(32, 5)
    # L3.insert(29, 9)
    # L3.insert(18, 6)
    # L3.insert(5, 1)
    # L3.insert(27, 8)
    # L3.print()              # 15 -> 5 -> 21 -> 11 -> 36 -> 37 -> 32 -> 18 -> 27 -> 25
    # print(L3.delete(6))     # 32
    # print(L3.delete(4))     # 36
    # L3.valueOf(8)
    # print(L3.delete(8))     # None
    # L3.valueOf(8)
    # print(L3.delete(1))     # 5
    # print(L3.delete(5))     # 27
    # print(L3.delete(2))     # 11
    # L3.print()              # 15 -> 21 -> 37 -> 18 -> 25


    #
    # L = LinkedList()
    # for num in (3, 5, 2, 7, 8, 10, 6):
    #     L.append(num)
    # L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    # L.isort()
    # L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10



