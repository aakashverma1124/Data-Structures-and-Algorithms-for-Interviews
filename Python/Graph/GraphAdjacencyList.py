class Graph:

	vertices = 0
	graph = {}

	def __init__(self, vertices):
		self.vertices = vertices
		for i in range(1, vertices + 1):
			self.graph[i] = []
		print(self.graph)

	def add_edge(self, edges):
		for edge in edges:
			self.graph[edge[0]].append(edge[1])
			self.graph[edge[1]].append(edge[0])

		print(self.graph)

	def print_graph(self):

		for key in self.graph:
			print(key, "is connected to ", self.graph[key])

if __name__ == '__main__':
	
	vertices = 4
	edges = [[1, 2], [1, 3], [1, 4], [2, 3]]

	graph = Graph(vertices)
	graph.add_edge(edges)
	graph.print_graph()

