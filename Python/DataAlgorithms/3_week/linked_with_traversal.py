class Node:
    data = None
    previous = None
    link = None

    def __init__(self,previous, data, link):
        self.previous = previous
        self.data = data
        self.link = link

class LinkedList:

    def __init__(self):
        self.start = None
        self.end = None

    def append(self, data):
        if self.start == None:
            self.start = Node(data, None, None)
            self.end = self.start
        else:
            self.previous = self.end
            self.end.link = Node(data, None, None)
            self.end = self.end.link

    def insert(self, data, index):
        i = 0
        lastNode = None
        curNode = self.start
        while curNode != None:
            if i == index and lastNode != None:
                lastNode.link = Node(data, curNode, lastNode)
            if i == index and lastNode == None:
                self.start = Node(data, curNode, None)
            i += 1
            lastNode = curNode
            curNode = curNode.link

    def isort(self):
        i = 0

        iterationPoint = self.start
        lastNode = self.start
        curNode = lastNode.link
#        nextNode = curNode.link

        while iterationPoint.link != None:
            iterationPoint = curNode
            while (lastNode != None):
                if (lastNode.data > curNode.data):
                    lastNode.data, curNode.data = curNode.data, lastNode.data

                curNode = lastNode
                lastNode = lastNode.previous

            lastNode = iterationPoint
            curNode = lastNode.link

            if curNode == None:
                print("Breakation")
                break
 #           nextNode = curNode.link
            print(i)
            i += 1

    def index(self, data):
        i = 0
        curNode = self.start
        while curNode != None:
            if curNode.data == data:
                return i
            i += 1
            curNode = curNode.link
        return -1

    def swap(self, ii, jj):
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
                curNode.link.previous = lastNode
                lastNode.link = curNode.link
                removed = curNode
            if i == index and lastNode == None:
                self.start = curNode.link
                curNode.link.previous = None
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
            #print(node.data)
            node = node.link
            if node != None:
                print(" -> ", end="")
            #print(node.data)
        print()

if __name__ == "__main__":
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
    #
    # L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    # print(L.index(7))   # 3
    # print(L.index(9))   # -1
    # L.swap(1, 4)
    # L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6
    # L.swap(2, 0)
    # L.print()           # 2 -> 8 -> 3 -> 7 -> 5 -> 10 -> 6
    #
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    L.isort()
    L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10



