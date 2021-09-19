 # 
 # @author 
 # aakash.verma
 # 
 # Output:
 # 2 0 1 3
 # 
 
from collections import deque

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for i in range(self.vertices)]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source) # for directed graph comment this line

    def breadth_first_search(self, source):
        bfs = []
        queue = deque([])
        visited = [False] * self.vertices
        queue.append(source) 
        visited[source] = True

        while len(queue) != 0:
            curr = queue.popleft() 
            bfs.append(curr)
            for nbr in self.adjacency_list[curr]:
                if visited[nbr] is not True:
                    queue.append(nbr)
                    visited[nbr] = True
        return bfs

if __name__ == '__main__':
    
    g = Graph(4);
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    ans = g.breadth_first_search(2)
    for ele in ans:
        print(ele, end = " ")
