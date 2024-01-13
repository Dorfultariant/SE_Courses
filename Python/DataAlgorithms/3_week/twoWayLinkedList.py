class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            current = self.head
            while current != None:
                if current.next == None:
                    # Added nodes previous is set to be current
                    newNode.previous = current
                    # Currents next is set to point to newNode
                    current.next = newNode
                    # Tail is updated to newNode
                    self.tail = newNode
                    break
                current = current.next
        return True

    def insert(self, data, index):
        i = 0
        current = self.head
        newNode = Node(data)

        if index == i:
            self.head = newNode
            current.previous = newNode
            newNode.next = current
            return True
        else:
            while current != None:
                if (i + 1) == index:
                    if current == self.tail:
                        newNode.previous = current
                        current.next = newNode
                        self.tail = newNode
                        return True
                    newNode.previous = current
                    current.next.previous = newNode
                    newNode.next = current.next
                    current.next = newNode
                    return True
                i += 1
                current = current.next

        return False

    def delete(self, index):
        i = 0
        current = self.head
        if index == i:
            current.next.previous = None
            data = current.data
            self.head = current.next
            return data
        else:
            while current != None:
                if i == index:
                    if current == self.tail:
                        data = current.data
                        self.tail = current.previous
                        current.previous.next = None
                        return data
                    data = current.data
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return data
                i += 1
                current = current.next
        return

    def index(self, data):
        i = 0
        current = self.head
        while current != None:
            if current.data == data:
                return i
            i += 1
            current = current.next

        return -1

    def swap(self, a, b):
        current = self.head
        i = 0
        A = None
        B = None
        if a == b:
            return
        while current != None:
            if i == a:
                A = current
            if i == b:
                B = current
            current = current.next
            i += 1

        if A == None or B == None:
            return
        else:
            # Set the nodes before A and B to point to B and A
            A.previous.next = B
            B.previous.next = A

            # Set the nodes after A and B to point to B and A
            A.next.previous = B
            B.next.previous = A

            # Set A.next to B.next and B.next to A.next
            current = A.next
            A.next = B.next
            B.next = current

            # Set the previous values to cross
            current = A.previous
            A.previous = B.previous
            B.previous = current
            print("Swapped")
            return
        return

    def print(self):
        current = self.head
        while current != None:
            print(current.data, end="")
            current = current.next
            if current != None:
                print(" -> ", end="")

        print()
        return True

    def printReversed(self):
        current = self.tail
        while current != None:
            print(current.data, end="")
            current = current.previous
            if current != None:
                print(" <- ", end="")

        print()
        return True


if __name__ == "__main__":
    L = LinkedList()
    print(L.append(14))
    print(L.append(20))
    print(L.append(550))
    print(L.append(2))
    print("After append")
    L.print()
    L.printReversed()
    print()
    L.swap(1, 2)
    print("After swap")
    L.print()
    #L.printReversed()

    # print()
    # print(L.insert(5,4))
    # print(L.insert(3,1))
    # print(L.insert(1,0))
    # print("After insert")
    # L.print()
    # L.printReversed()
    # print()
    # print(L.delete(0))
    # print("After delete")
    # L.print()
    # L.printReversed()

