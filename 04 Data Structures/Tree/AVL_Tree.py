#Program to implement an AVL Tree
import math

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1 #Facilitates in calculation of balance factor

class AVLTree:

    def insert(self, root, key):
        if not root: #If there is no root
            return node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        if key > root.data:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor>1:
            if key < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor<-1:
            if key > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root

    def leftRotate(self, root):
        y = root.right
        z = y.left
        y.left = root
        root.left = z
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, root):
        y = root.left
        z = y.right
        y.right = root
        root.left = z
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getBalance(self, root):
        if not root: return 0
        return self.getHeight(root.left)-self.getHeight(root.right)

    def getHeight(self, root):
        if not root: return 0
        return root.height

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        print(root.data, "Height:",root.height-1, "BalFac:", self.getBalance(root))
        self.inOrder(root.right)
            
tree = AVLTree()
root = None
arr = [33, 13, 52, 9, 21, 61, 8, 11]
for num in arr:
    root = tree.insert(root, num)
tree.inOrder(root)
