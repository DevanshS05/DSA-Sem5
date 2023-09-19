class Stack:
    size = 0
    top=-1
    arr = list(range(0,5))

    def __init__(self,size):
        print("Stack has been created")
        self.size = size
        self.arr = list(range(0,size))

    def peek(self):
        if self.top==-1:
            print("Stack is empty")
            return 
        else:
            return self.arr[self.top]

    def push(self, number):
        if self.top==self.size-1:
            print("Stack is already full, overflow")
            return
        else:
            self.top+=1
            self.arr[self.top]=number

    def pop(self):
        if self.top==-1:
            print("Stack underflow")
            return
        else:
            return self.arr[self.top]
            self.top-=1

#Driver code goes below
stack = Stack(25)
