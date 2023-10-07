#Program to implement a List
class List:

    def __init__(self):
        print("You have created a list")
        self.lst = list(10)
        self.size=10
        self.top=-1

    def insert(self, num):
        if self.top==self.size-1:
            self.tmp = list(
            

