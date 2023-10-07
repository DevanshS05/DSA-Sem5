import Linked_List as LL

class Queue:
    size=0

    def __init__(self):
        self.llist = LL.LinkedList()

    def enqueue(self, num):
        self.llist.insertAtEnd(num)
        self.size+=1

    def dequeue(self):
        self.size-=1
        return self.llist.removeAtHead()

    def peek(self):
        if self.size==0:
            print("Queue is empty")
            return
        else:
            return self.llist.getElementAtHead()

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size==0: return True
        else: return False

    def printQueue(self):
        self.llist.printList()

#Below is some driver code
queue = Queue()
for i in range(0,10):
    queue.enqueue(i+1)
queue.printQueue()
queue.dequeue()
queue.printQueue()
