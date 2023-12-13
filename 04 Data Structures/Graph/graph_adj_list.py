#Program to implement graph using adjacency list
class node:
    def __init__(self,value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self,size):
        self.V = size
        self.graph = [None] * self.V

    def add_edge(self,v1,v2):
        new_node = node(v1)
        new_node.next = self.graph[v2]
        self.graph[v2] = new_node

        new_node = node(v2)
        new_node.next = self.graph[v1]
        self.graph[v1] = new_node

    def print(self):
        for i in range(0,self.V):
            print("Vertex [{}] :".format(i),end=" ")
            ptr = self.graph[i]
            while(ptr!=None):
                print("{} ->".format(ptr.vertex),end=" ")
                ptr = ptr.next
            print("\n")

#Below is some driver code
V=5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.print()

        
