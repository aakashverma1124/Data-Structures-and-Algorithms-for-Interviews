 # 
 # @author 
 # aakash.verma
 # 
 # Output:
 # Adjacency List of Undirected Graph
 # |Delhi| => Mumbai Bangalore 
 # |Mumbai| => Delhi Hyderabad Bangalore 
 # |Bangalore| => Delhi Mumbai 
 # |Hyderabad| => Mumbai
 # 
 #

class Graph:

	def __init__(self, cities):
		self.cities = cities
		self.adjacency_list = dict()
		for city in self.cities:
			self.adjacency_list[city] = list()

	def add_edge(self, source, destination):
		self.adjacency_list[source].append(destination)
		self.adjacency_list[destination].append(source) # for directed graph comment this line

	def print_graph(self):
		print("Adjacency List of Undirected Graph")
		for city in self.cities:
			print("|", city, "| => ", end = " ")
			for nbr_city in self.adjacency_list[city]:
				print(nbr_city, end = " ")
			print()


if __name__ == '__main__':
	
	cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad"]
	g = Graph(cities);
	g.add_edge("Delhi", "Mumbai")
	g.add_edge("Delhi", "Bangalore")
	g.add_edge("Mumbai", "Hyderabad")
	g.add_edge("Mumbai", "Bangalore")
	g.print_graph()


