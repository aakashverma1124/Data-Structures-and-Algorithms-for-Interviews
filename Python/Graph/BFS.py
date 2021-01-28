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
            
def bfs(s, edges, vertices):

	# getting converted edges into an adjacency list
    graph = gridToAdjacencyList(edges)

    # taking a visited array and marking every node as unvisited
    visited = [False] * (vertices + 1)
    distance = [-1]  * (vertices + 1)
    queue = deque([]) 	# creating a queue
    queue.append(s) # appending source node into queue
    visited[s] = True # marking source node as visited
    distance[s] = 0
    bfs_ans = [] # array to store the bfs

    while len(queue) != 0:
        curr = queue.popleft() # popping element from queue and storing it into bfs array
        bfs_ans.append(curr)

        # now we'll explore all the nodes that can be reached from current node
        # also, if node is not visited we'll add it into the queue and mark as visited
        for v in graph[curr]:
            if visited[v] is not True:
                queue.append(v)
                visited[v] = True
                distance[v] = distance[curr] + 6
    print(distance[1:])
    return bfs_ans

if __name__ == '__main__':
    
    edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
    vertices = 6
    ans = bfs(1, edges, vertices)
    print(ans)