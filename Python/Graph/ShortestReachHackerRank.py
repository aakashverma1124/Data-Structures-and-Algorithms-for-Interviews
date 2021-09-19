 # 
 # 
 # @author 
 # aakash.verma
 # 
 # Problem Link: https://www.hackerrank.com/challenges/bfsshortreach/problem
 # Note: I have completed the function only.
 # 

def bfs(n, m, edges, s):
    distance = [-1] * (n + 1)
    q = deque([])
    visited = [False] * (n + 1)
    q.append(s)
    visited[s] = True
    distance[s] = 0

    # creating adjacency list from the given set of edges. 
    adjacency_list = [[] for i in range(n + 1)]
    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    while len(q) != 0:
        curr = q.popleft() 
        for nbr in adjacency_list[curr]:
            if visited[nbr] is not True:
                q.append(nbr)
                visited[nbr] = True
                distance[nbr] = distance[curr] + 6 
    
    distance.remove(0)
    return distance[1:]