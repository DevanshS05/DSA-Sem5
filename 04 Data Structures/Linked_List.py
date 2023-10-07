class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    size=0
    
    def __init__(self):
        self.head = None
        self.size=0

    #Insertion at the head 
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
            
    #Indexing starts from 0 to size-1
    def insertAtIndex(self, idx, data):
        new_node = node(data)
        if idx==0:
            self.insertAtHead(data)
        elif idx==self.size-1:
            self.insertAtEnd(data)
        else:
            current_node = self.head
            for i in range(1,idx-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.size+=1
            
    #Insertion towards the end
    def insertAtEnd(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.size+=1
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        self.size+=1

    def removeAtHead(self):
        if self.head is None:
            return
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size-=1
            return temp
            

    def removeAtEnd(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            self.size-=1
            return
        else:
            current_node = self.head
            #Reaches to the second last node
            while(current_node.next.next): current_node = current
            current_node.next = Null
            self.size-=1

    def removeAtIndex(self, idx):
        if self.head is None:
            return
        elif idx==0: self.removeAtHead()
        elif idx==self.size-1: self.removeAtEnd()
        else:
            current_node = self.head
            for i in range(1,idx):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.size-=1
            
    def printList(self):
        current_node = self.head
        print("[",end=" ")
        while(current_node):
            print(current_node.data,end=" ")
            current_node = current_node.next
        print("]")

    def getSize(self):
        return self.size

    def getElementAtHead(self):
        if self.head is None:
            return
        else:
            return self.head.data

    def getElementAtEnd(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            return current_node.data
        


#This is driver code
'''
llist = LinkedList()
for i in range(1,6):
    llist.insertAtHead(i)
llist.removeAtIndex(3)
llist.printList()
'''
