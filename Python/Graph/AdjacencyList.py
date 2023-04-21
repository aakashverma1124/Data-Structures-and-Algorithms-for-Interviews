from collections import deque

class Graph:

    @staticmethod
    def build_graph(edges, v):
        graph = dict()
        # initialisation process of empty graph
        for i in range(v):
            graph[i] = list()

        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u) # add this if graph is undirected only

        return graph

    @staticmethod
    def breadth_first_search(edges, v, src):
        graph = Graph.build_graph(edges, v)
        queue = deque()
        visited = [False] * v
        bfs = []
        queue.append(src)
        visited[src] = True

        while queue:
            node = queue.popleft()
            bfs.append(node)
            for nbr in graph[node]:
                if visited[nbr] is not True:
                    queue.append(nbr)
                    visited[nbr] = True
    
        return bfs

    @staticmethod
    def dfs_util(node, graph, dfs, visited):
        dfs.append(node)
        visited[node] = True
        for nbr in graph[node]:
            if visited[nbr] is not True:
                Graph.dfs_util(nbr, graph, dfs, visited)

    @staticmethod
    def depth_first_search(edges, v, src):
        graph = Graph.build_graph(edges, v)
        visited = [False] * v
        dfs = []
        Graph.dfs_util(src, graph, dfs, visited)
        return dfs

if __name__ == "__main__":
    # edges = [[0, 1], [0, 2], [1, 2], [2, 4], [3, 4]]
    # v = 5
    # edges = [[0, 1], [0, 3], [1, 2], [1, 4], [2, 3], [2, 7], [3, 5], [4, 6], [5, 7], [6, 7]]
    # v = 8
    edges = [[0, 1], [0, 4], [0, 7], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6]]
    v = 8
    print(Graph.depth_first_search(edges, v, 0))
    print(Graph.breadth_first_search(edges, v, 0))