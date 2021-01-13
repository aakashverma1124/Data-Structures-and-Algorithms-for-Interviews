# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from collections import deque

graph = dict()
def gridToAdjacencyList(edges):
    d = dict()
    
    # initializing the graph (converting edges into an adjacency list)
    for i in range(1, vertices + 1):
        d[i] = list()
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])
    return d

# there will be a condition when node's neighbour will be visited and it might seem that there is a cycle 
# but this is not the case because the node, which has already been visited, might be it's parent. So, 
# we will have a condition that node's neighbour is visited then is should not be it's parent, only then 
# we can declare that the graph has a cycle.
def cycle_detection_dfs(graph, node, visited, parent):
	
	visited[node] = True

	for neighbour in graph[node]:
		if visited[neighbour] is not True:
			cycle_found = cycle_detection_dfs(graph, neighbour, visited, node)
			if(cycle_found):
				return True

		elif (neighbour != parent):
			return True

	return False


def contains_cycle(graph, vertices):
	visited = [False] * (vertices + 1)
	return cycle_detection_dfs(graph, 1, visited, -1) # passing graph, starting node, visited array, and parent

if __name__ == '__main__':
    
    # edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
    edges = [[2, 1], [2, 3]]
    vertices = 3
    graph = gridToAdjacencyList(edges)
    ans = contains_cycle(graph, vertices)
    print(ans)