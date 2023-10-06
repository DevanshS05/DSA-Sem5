import Linked_List as LL

class Stack:
    size=10 #The default size is 10
    top = -1
    def __init__(self, size):
        self.llist = LL.LinkedList()
        self.size = size

    def push(self, num):
        if self.top==self.size-1:
            print("Stack is already full")
        else:
            self.top+=1
            self.llist.insertAtHead(num)

    def pop(self):
        if self.top==-1:
            print("Stack is already empty")
        else:
            self.top-=1
            return self.llist.removeAtHead()

    def peek(self):
        if self.top==-1:
            print("Stack is already empty")
        else:
            return self.llist.getElementAtHead()

    def printStack(self):
        self.llist.printList()

    def isEmpty(self):
        if self.top==-1: return True
        else: return False

    def isFull(self):
        if self.top==size-1: return True
        else: return False
        

#Driver code
stack = Stack(10)
for i in range(1,15):
    stack.push(i)
stack.printStack()
print(stack.pop())
