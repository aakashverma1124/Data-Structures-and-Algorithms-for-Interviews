# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from collections import deque

# there will be a condition when node's neighbour will be visited and it might seem that there is a cycle 
# but this is not the case because the node, which has already been visited, might be it's parent. So, 
# we will have a condition that node's neighbour is visited then is should not be it's parent, only then 
# we can declare that the graph has a cycle.

def cycle_detection_bfs(src, edges, vertices):
    
    # creating a graph (adjacency list) from edges
    graph = dict()
    for i in range(1, vertices + 1):
        graph[i] = list()
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    visited = [False] * (vertices + 1)
    parent = [-1] * (vertices + 1)
    queue = deque([])

    queue.append(src)
    visited[src] = True
    parent[src] = -1

    while(len(queue) != 0):
        curr = queue.popleft()

        # iterate over the neighbours of the curr node
        for neighbour in graph[curr]:
            if visited[neighbour] is not True:
                visited[neighbour] = True
                parent[neighbour] = curr
                queue.append(neighbour)
            elif (visited[neighbour] is True and parent[curr] != neighbour):
                return True

    return False
	

if __name__ == '__main__':
    
    edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
    # edges = [[2, 1], [2, 3]]
    vertices = 6
    ans = cycle_detection_bfs(1, edges, vertices)
    print(ans)