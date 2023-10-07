class node:
     def __init__(self,data):
         self.data = data
         self.next = None

class CircularLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtHead(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head  = new_node
            self.tail.next  = self.head
        self.size+=1

    def insertAtEnd(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.size+=1
            

    def printList(self):
        current_node = self.head
        for i in range(0,self.size*2):
            print(current_node.data,end=" ")
            current_node = current_node.next


#Here is some driver code
l = CircularLL()
for i in range(0,5):
    l.insertAtHead(i+1)
l.insertAtEnd(-1)
l.insertAtEnd(-2)
l.printList()

