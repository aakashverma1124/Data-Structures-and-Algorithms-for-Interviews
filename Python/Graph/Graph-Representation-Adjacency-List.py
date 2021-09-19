 # 
 # @author 
 # aakash.verma
 # 
 # Output:
 # Adjacency List of Undirected Graph
 # |0| => 1 2 
 # |1| => 0 3 
 # |2| => 0 3 
 # |3| => 1 2 
 # 
 #

class Graph:

	def __init__(self, vertices):
		self.vertices = vertices
		self.adjacency_list = [[] for i in range(self.vertices)]

	def add_edge(self, source, destination):
		self.adjacency_list[source].append(destination)
		self.adjacency_list[destination].append(source) # for directed graph comment this line

	def print_graph(self):
		print("Adjacency List of Undirected Graph")
		for i in range(self.vertices):
			print("|", i, "| => ", end = " ")
			for nbr in self.adjacency_list[i]:
				print(nbr, end = " ")
			print()


if __name__ == '__main__':
	
	g = Graph(4);
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 3)
	g.print_graph()


