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


def add_edge(source, destination):
	adjacency_list[source].append(destination)
	adjacency_list[destination].append(source) # for directed graph comment this line

def print_graph():
	print("Adjacency List of Undirected Graph")
	for i in range(vertices):
		print("|",i,"| => ", end = " ")
		for nbr in adjacency_list[i]:
			print(nbr, end = " ")
		print()


if __name__ == '__main__':
	
	vertices = 4
	adjacency_list = [[] for i in range(vertices)]
	add_edge(0, 1)
	add_edge(0, 2)
	add_edge(1, 3)
	add_edge(2, 3)
	print_graph()


