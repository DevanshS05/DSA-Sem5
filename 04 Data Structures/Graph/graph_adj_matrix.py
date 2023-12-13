#Program to implement a graph using adjacency matrix
class Graph:
    def __init__(self,size):
        self.adj_matrix = []
        for i in range(0,size):
            self.adj_matrix.append([0 for i in range(0,size)])
        self.size = size

    #Add an edge
    def add_edge(self,v1,v2):
        if v1==v2:
            print("Same vertex {} and {}".format(v1,v2))
        self.adj_matrix[v1][v2]=1
        self.adj_matrix[v2][v1]=1

    def remove_edge(self,v1,v2):
        if self.adj_matrix[v1][v2] == 0:
            print("There is no edge between {} and {}".format(v1,v2))
        else:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0

    def print(self):
        print("  ",end="")
        for i in range(0,self.size): print(i,end=" ")
        print("\n")
        
        for i in range(0,self.size):
            print(i,end=" ")
            for j in range(0,self.size):
                print(self.adj_matrix[i][j],end=" ")
            print("\n")

#Below is some driver code
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

g.print()
