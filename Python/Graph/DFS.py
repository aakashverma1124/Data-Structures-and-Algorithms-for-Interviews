# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from collections import deque

def gridToAdjacencyList(edges):
    d = dict()
    
    # initializing the graph (converting edges into an adjacency list)
    for i in range(1, vertices + 1):
        d[i] = list()
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])
    return d

def dfs_util(s, graph, visited, dfs_ans):

    visited[s] = True
    dfs_ans.append(s)

    for neighbour in graph[s]:
        if visited[neighbour] is not True:
            dfs_util(neighbour, graph, visited, dfs_ans)
            
def dfs(s, edges, vertices):

	# getting converted edges into an adjacency list
    graph = gridToAdjacencyList(edges)
    visited = [False] * (vertices + 1)
    dfs_ans = []

    dfs_util(s, graph, visited, dfs_ans)
    return dfs_ans

    

if __name__ == '__main__':
    
    edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
    vertices = 6
    ans = dfs(1, edges, vertices)
    print(ans)




