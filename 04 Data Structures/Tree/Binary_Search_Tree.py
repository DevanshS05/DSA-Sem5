#Code to implement binary Search Tree

import math
import random

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        new_node = node(data)
        if data<self.data:
            if self.left is None: self.left = new_node
            else: self.left.insert(data)
        else:
            if self.right is None:self.right = new_node
            else: self.right.insert(data)

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
        print("\n")
            
    #Unimprovised
    def printTree(self):
        queue = []
        printQueue = []
        queue.append(self)
        while(len(queue)!=0):
            curr_node = queue.pop(0)
            #print(curr_node.data,end=" ")
            printQueue.append(curr_node.data)
            if curr_node.data=='00': continue
            if curr_node.left!=None: queue.append(curr_node.left)
            else: queue.append(node('00'))
            if curr_node.right!=None: queue.append(curr_node.right)
            else: queue.append(node('00'))

        #Finding the number of levels in the tree
        queueSize = len(printQueue)
        levels = int(math.log(queueSize+1, 2))
        for i in range(0,levels):
            #For printing the appropriate number of spaces
            for s in range(0,3*(levels-i)): print(" ",end="")
            for j in range(0,2**i):
                print(printQueue.pop(0),end=" ")
            print("\n")

       
#Below is some driver code
root = node(50)

for i in range(0,10):
    root.insert(random.randint(10,90))
    

root.levelOrder()
