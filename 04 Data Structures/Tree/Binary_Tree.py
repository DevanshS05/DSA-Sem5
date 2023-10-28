class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def preOrder(self):
        #Root, Left, Right
        print(self.data,end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        #Left, Root, Right
        if self.left:
            self.left.inOrder()
        print(self.data,end=" ")
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        #Left, Right, Root
        if self.left: self.left.postOrder()
        if self.right: self.right.postOrder()
        print(self.data,end=" ")

    def levelOrder(self):
        queue = []
        queue.append(self)
        while(len(queue)!=0):
            curr_node = queue.pop(0)
            print(curr_node.data,end=" ")
            if curr_node.left!=None: queue.append(curr_node.left)
            if curr_node.right!=None: queue.append(curr_node.right)

#Here is some driver code
root = node(5)
root.left = node(3)
root.right = node(8)
root.left.right = node(4)
root.left.left = node(2)
root.right.left = node(6)
root.right.right = node(9)

print("Pre-Order: ",end="")
root.preOrder()
print("\nIn-Order: ",end="")
root.inOrder()
print("\nPost-Order: ",end="")
root.postOrder()
print("\nLevel Order: ",end="")
root.levelOrder()
