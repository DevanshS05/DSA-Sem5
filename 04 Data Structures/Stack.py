class Stack:
    myList = list()
    top = -1
    size = 0

    def __init__(self,size):
        self.size = size
        self.myList.extend(list(range(0,size))) #Creates a list of given size

    def push(self,num):
        if self.top==self.size-1:
            print("Overflow")
            return
        else:
            self.top+=1
            self.myList[self.top]=num

    def pop(self):
        if self.top==-1:
            print("Underflow")
            return
        else:
            self.top-=1
            return self.myList[self.top+1]

    def peek(self):
        if self.top==-1:
            print("List is empty")
            return
        else:
            return self.myList[self.top]

    def isEmpty(self):
        if self.top==-1: return True
        else: return False

    def isFull(self):
        if self.top==self.size-1: return True
        else: return False

    def currSize(self):
        return self.top+1

#Here is some driver code
stack = Stack(5)
for i in range(1,8):
    stack.push(i)
print("The element at top of stack is: {}".format(stack.peek()))
print("Stack is full: {}".format(stack.isFull()))
for i in range(1,8):
    print("Popped element: {}".format(stack.pop()))
print("Size of stack is: {}".format(stack.currSize()))
print("Stack is empty: {}".format(stack.isEmpty()))
