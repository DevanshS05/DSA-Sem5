class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class CircularLL:
    def __init__(self):
        self.head = None
        self.size=0
        self.cycleSize=0

    def insertAtHead(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.size+=1
            return
        else:
            new_node.next = self.head
            self.head = new_node
            self.size+=1

    def setCycle(self, idx):
        if idx>self.size-1:
            print("Index value cannot be greater than size of LinkedList")
        else:
            current_node = self.head
            target_node = self.head
            while(current_node.next):
                current_node = current_node.next
            for i in range(0,idx-1):
                target_node = target_node.next
            print("Set Cycle: ","Current node is",current_node.data,"Target node is",target_node.next.data)
            current_node.next = target_node.next

            #Next we need to find the size of the cycle because only then we can print it
            self.cycleSize = self.size-idx

    def printList(self):
        if self.cycleSize!=0:
            print("[")
            print("Cycle is set")
            current_node = self.head
            while(current_node):
                print(current_node.data)
                current_node = current_node.next
            print("]")
            
        else:
            print("[",end=" ")
            current_node = self.head
            while(current_node):
                print(current_node.data,end=" ")
                current_node = current_node.next
            print("]")

    def printCycle(self):
        if self.cycleSize>0:
            print("[",end=" ")
            current_node = self.head
            for i in range(0,self.size-self.cycleSize): current_node = current_node.next
            for i in range(0,self.cycleSize):
                print(current_node.data,end=" -> ")
                current_node = current_node.next
            print("]")
        else:
            print("Cycle is not set")


    

#Below is some driver  code
l = CircularLL()
for i in range(0,10):
    l.insertAtHead(i+1)
l.printList()
l.setCycle(0)
l.printCycle()


    
            
