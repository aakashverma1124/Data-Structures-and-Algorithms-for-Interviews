 # 
 # @author 
 # aakash.verma
 # 
 # Output:
 # 0 1 2 3 4 5
 # 
 
from collections import deque

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for i in range(self.vertices)]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source) # for directed graph comment this line

    def dfs_util(self, node, visited, dfs):
        dfs.append(node)
        visited[node] = True
        for child in self.adjacency_list[node]:
            if visited[child] is not True:
                self.dfs_util(child, visited, dfs)

    def depth_first_search(self, source):
        dfs = []
        visited = [False] * self.vertices
        self.dfs_util(source, visited, dfs)
        return dfs

if __name__ == '__main__':
    
    g = Graph(6);
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    ans = g.depth_first_search(0)
    for ele in ans:
        print(ele, end = " ")
