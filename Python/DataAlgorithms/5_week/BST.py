class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.stump = None
        self.isMirrored = False

    def insert(self, value):
        if self.stump == None:
            self.stump = Node(value)
        curr = self.stump
        if not self.isMirrored:
            while curr.data != value:
                if curr.data > value:
                    if curr.left == None:
                        curr.left = Node(value)
                        return
                    curr = curr.left
                elif curr.data < value:
                    if curr.right == None:
                        curr.right = Node(value)
                        return
                    curr = curr.right
        else:
            while curr.data != value:
                if curr.data > value:
                    if curr.right == None:
                        curr.right = Node(value)
                        return
                    curr = curr.right
                elif curr.data < value:
                    if curr.left == None:
                        curr.left = Node(value)
                        return
                    curr = curr.left
                

    def search(self, value):
        return self.__searchHelp(self.stump, value)

    def __searchHelp(self, node, value):
        if not self.isMirrored:
            if node == None:
                return False
            elif node.data > value:
                return self.__searchHelp(node.left, value)
            elif node.data < value:
                return self.__searchHelp(node.right, value)
            else:
                return True
        else:
            if node == None:
                return False
            elif node.data > value:
                return self.__searchHelp(node.right, value)
            elif node.data < value:
                return self.__searchHelp(node.left, value)
            else:
                return True
            

    def preorder(self):
        self.__preorderHelp(self.stump)
        print()
        return

    def __preorderHelp(self, node):
        if not self.isMirrored:
            if node == None:
                return
            self.__visiter(node)
            self.__preorderHelp(node.left)
            self.__preorderHelp(node.right)
        else:
            if node == None:
                return
            self.__visiter(node)
            self.__preorderHelp(node.right)
            self.__preorderHelp(node.left)
            
    def postorder(self):
        self.__postorderHelp(self.stump)
        print()
        return
        
    def __postorderHelp(self, node):
        if not self.isMirrored:
            if node == None:
                return
            self.__postorderHelp(node.left)
            self.__postorderHelp(node.right)
            self.__visiter(node)
        else:
            if node == None:
                return
            self.__postorderHelp(node.right)
            self.__postorderHelp(node.left)
            self.__visiter(node)

    def inorder(self):
        self.__inorderHelp(self.stump)
        print()
        return

    def __inorderHelp(self, node):
        if not self.isMirrored:
            if node == None:
                return
            self.__inorderHelp(node.left)
            self.__visiter(node)
            self.__inorderHelp(node.right)
        else:
            if node == None:
                return
            self.__inorderHelp(node.right)
            self.__visiter(node)
            self.__inorderHelp(node.left)
    
    def __visiter(self, node):
        print(node.data, end=" ")
        return

    def remove(self, value):
        self.stump = self.__removeHelp(self.stump, value)
    
    def __removeHelp(self, node, value):
        if not self.isMirrored:
            if node == None:
                return None
            elif node.data > value:
                node.left = self.__removeHelp(node.left, value)
            elif node.data < value:
                node.right = self.__removeHelp(node.right, value)
            else:
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                else:
                    node.data = self.__getMax(node.left)
                    node.left = self.__removeMax(node.left)
        else:
            if node == None:
                return None
            elif node.data > value:
                node.right = self.__removeHelp(node.right, value)
            elif node.data < value:
                node.left = self.__removeHelp(node.left, value)
            else:
                if node.right == None:
                    return node.left
                elif node.left == None:
                    return node.right
                else:
                    node.data = self.__getMax(node.right)
                    node.right = self.__removeMax(node.right)
        return node

    def breadthfirst(self):
        if self.stump == None:
            return
        pigqueue = []
        pigqueue.append(self.stump)
        i = 0
        if not self.isMirrored:
            while pigqueue[i] != None:
                print(pigqueue[i].data, end=" ")
                if pigqueue[i].left != None:
                    pigqueue.append(pigqueue[i].left)
                if pigqueue[i].right != None:
                    pigqueue.append(pigqueue[i].right)
                i += 1
        else:
            while 1 + 1 >= 2:
                print(pigqueue[i].data, end=" ")
                if pigqueue[i].right != None:
                    pigqueue.append(pigqueue[i].right)
                if pigqueue[i].left != None:
                    pigqueue.append(pigqueue[i].left)
                i += 1
        print()

    def __getMax(self, node):
        if not self.isMirrored:
            if node.right == None:
                return node.data
            return self.__getMax(node.right)
        else:
            if node.left == None:
                return node.data
            return self.__getMax(node.left)

    def __removeMax(self, node):
        if not self.isMirrored:
            if node.right == None:
                return node.left
            node.right = self.__removeMax(node.right)
            return node
        else:
            if node.left == None:
                return node.right
            node.left = self.__removeMax(node.left)
            return node

    def mirror(self):
        if self.isMirrored:
            self.isMirrored = False
            return
        self.isMirrored = True
        


if __name__ == "__main__":

    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.mirror()
    Tree.preorder()         # 5 9 7 6 1 3 4 2 

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))   # True
    Tree.preorder()         # 5 9 7 8 6 1 2 4
    Tree.mirror()
    Tree.preorder()         # 5 1 2 4 9 7 6 8
