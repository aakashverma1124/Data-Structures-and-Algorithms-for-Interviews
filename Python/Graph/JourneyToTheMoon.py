# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

# Problem Link: https://www.hackerrank.com/challenges/journey-to-the-moon/problem
# Only functions are written in this code

def dfs(node, visited, graph):
    count = 1
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] is not True:
            count += dfs(neighbour, visited, graph)
            
    return count

def gridToAdjacencyList(cities, n):
    graph = dict()
    for i in range(n):
        graph[i] = list()
    for city in cities:
        graph[city[0]].append(city[1])
        graph[city[1]].append(city[0])

def journeyToMoon(n, astronauts):
    
    graph = gridToAdjacencyList(astronaut, n)
        
    visited = [False] * (n)
    components = []   
    
    for v in range(n):
        if len(graph[v]) > 0 and visited[v] is not True:
            components.append(dfs(v, visited, graph))
        elif (len(graph[v]) == 0):
            components.append(1)








    length = len(components)
    prefix_array = [0] * length
    prefix_array[-1] = components[-1]
    for i in range(length - 2, -1, -1):
        prefix_array[i] = prefix_array[i + 1] + components[i]
        
    ans = 0
    for i in range(length - 1):
        ans = ans + components[i] * prefix_array[i + 1]            
    return ans