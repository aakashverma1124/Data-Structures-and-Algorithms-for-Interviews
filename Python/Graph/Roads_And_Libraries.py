# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

# Problem Link: https://www.hackerrank.com/challenges/torque-and-development/problem
# Only functions are written in this code

def dfs(node, visited, graph):
    count = 1
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] is not True:
            count += dfs(neighbour, visited, graph)
            
    return count
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = dict()
    # initializing the graph (converting cities into an adjacency list)
    for i in range(1, n + 1):
        graph[i] = list()
    for city in cities:
        graph[city[0]].append(city[1])
        graph[city[1]].append(city[0])
        
    visited = [False] * (n + 1)
    components = []   
    
    for v in range(1, n + 1):
        if len(graph[v]) > 0 and visited[v] is not True:
            components.append(dfs(v, visited, graph))
        elif (len(graph[v]) == 0):
            components.append(1)
    ans = 0
    for i in range(len(components)):
        ans += min((components[i]-1) * c_road + c_lib, components[i] * c_lib)
    return ans