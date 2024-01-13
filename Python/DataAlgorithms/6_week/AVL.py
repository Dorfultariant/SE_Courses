
## Most of the code for this assignment was taken from the example python code given in the weeks study material "Python: The AVL Tree".
## My Own additions are basically the PreOrder method, left_rotation, right_left_rotation, and rest of the insert operation

class AVLNode:
    # Initialize new node
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.balance = 0

class AVL:
    # Initialize new tree
    def __init__(self) -> None:
        self.root = None
        self.is_balanced = True


    # Inserts a new key to the search tree
    def insert(self, key: int):
        self.root = self.insert_help(self.root, key)


    # Help function for insert
    def insert_help(self, root, key):
        if not root:
            root = AVLNode(key)
            self.is_balanced = False
        elif key < root.key:
            root.left = self.insert_help(root.left, key)
            if not self.is_balanced:                           # Check for possible rotations
                if root.balance >= 0:                       # No Rotations needed, update balance variables
                    self.is_balanced = root.balance == 1
                    root.balance -= 1
                else:                                       # Rotation(s) needed
                    if root.left.balance == -1:
                        root = self.right_rotation(root)    # Single rotation
                    else:
                        root = self.left_right_rotation(root)   # Double rotation
                    self.is_balanced = True
        elif key > root.key:
            root.right = self.insert_help(root.right, key)
            if not self.is_balanced:                           # Check for possible rotations
                if root.balance <= 0:                       # No Rotations needed, update balance variables
                    self.is_balanced = root.balance == -1
                    root.balance += 1
                else:                                       # Rotation(s) needed
                    if root.right.balance == 1:
                        root = self.left_rotation(root)    # Single rotation
                    else:
                        root = self.right_left_rotation(root)   # Double rotation
                    self.is_balanced = True

        return root

    # Single rotation: right rotation around root
    def right_rotation(self, root):
        child = root.left                   # Set variable for child node

        root.left = child.right             # Rotate
        child.right = root

        child.balance = root.balance = 0    # Fix balance variables

        return child


    # Single rotation: left rotation around root
    def left_rotation(self, root):
        child = root.right                   # Set variable for child node

        root.right = child.left # Rotate
        child.left = root

        child.balance = root.balance = 0    # Fix balance variables

        return child


    # Double rotation: left rotation around child node followed by right rotation around root
    def left_right_rotation(self, root: AVLNode):
        child = root.left
        grandchild = child.right            # Set variables for child node and grandchild node

        child.right = grandchild.left       # Rotate
        grandchild.left = child

        root.left = grandchild.right
        grandchild.right = root

        root.balance = child.balance = 0    # Fix balance variables

        if grandchild.balance == -1:
            root.balance = 1
        elif grandchild.balance == 1:
            child.balance = -1
        grandchild.balance = 0

        return grandchild


    def right_left_rotation(self, root: AVLNode):
        child = root.right
        grandchild = child.left # Set variables for child node and grandchild node

        child.left = grandchild.right # Rotate
        grandchild.right = child

        root.right = grandchild.left
        grandchild.left = root

        root.balance = child.balance = 0    # Fix balance variables

        if grandchild.balance == 1:
            root.balance = -1
        elif grandchild.balance == -1:
            child.balance = 1
        grandchild.balance = 0

        return grandchild


    def preorder(self):
        self.__preorderHelp(self.root)
        print()
        return

    def __preorderHelp(self, node):
        if node == None:
            return
        self.__visiter(node)
        self.__preorderHelp(node.left)
        self.__preorderHelp(node.right)

    def __visiter(self, node):
        print(f"{node.key};{node.balance}", end=" ")
        return



if __name__ == "__main__":
    Tree = AVL()
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
        Tree.insert(key)
    Tree.preorder()     # 9;-1 4;0 2;0 1;0 3;0 6;0 5;0 7;0 10;1 11;0
