# @author
# Aakash Verma

from collections import deque

def bfs(n, source, tree):
	
	queue = deque([])
	queue.append(source)
	distance = [0] * (n + 1)
	
	while queue:
		current = queue.popleft()
		for node in tree[current]:
			queue.append(node)
			distance[node] = distance[current] + 1

	return distance

if __name__ == '__main__':
	
	t = int(input())
	for i in range(t):
		n = int(input())
		
		tree = dict()
		
		for i in range(1, n + 1):
			tree[i] = []

		for i in range(n - 1):
			a, b = tuple(map(int, input().split()))
			tree[a].append(b)
			
		distance = bfs(n, 1, tree)

		for i in range(1, n + 1):
			print(distance[i], end = " ")
		print()
		
