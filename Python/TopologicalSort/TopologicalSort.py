# @author
# Aakash Verma

# Output:
# 5 6 3 4 0 2 1 

from collections import deque

def topologicalSort(edges, vertices):
	sorted_order = []
	if(vertices <= 0):
		return sorted_order

	in_degree = dict()
	graph = dict()

	# intializing the graph
	for i in range(vertices):
		in_degree[i] = 0
		graph[i] = []

	# building the graph
	for i in range(len(edges)):
		parent = edges[i][0]
		child = edges[i][1]
		in_degree[child] += 1
		graph[parent].append(child)

	# processing all valid starting nodes
	queue = deque()
	for key in in_degree:
		if in_degree[key] == 0:
			queue.append(key)

	while queue:
		vertex = queue.popleft()
		sorted_order.append(vertex)
		children = graph[vertex]
		for child in children:
			in_degree[child] -= 1
			if in_degree[child] == 0:
				queue.append(child)

	if len(sorted_order) != vertices:
		return []

	return sorted_order



if __name__ == '__main__':
	
	edges = [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
	ans = topologicalSort(edges, 7)
	print(ans)