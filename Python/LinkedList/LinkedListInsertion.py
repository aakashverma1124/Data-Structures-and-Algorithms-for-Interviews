#
#
#
#   @author
#   Aakash Verma
#	
# 	Insertions in Linked List
#
#	Output: 
#
#	Initial Linked List:  1 
#	After inserting at the end of Linked List:  1 6 
#	After inserting at the beginning of Linked List:  7 1 6 
#	After inserting after node 7 in Linked List:  7 8 1 6 	
#


# Below is the structute of a node which is used to create a new node every time.
class Node: 

	def __init__(self, data): 
		self.data = data
		self.next = None # None is nothing but null 

# Creating a class for implementing the code for Insertion in a Linked List
class LinkedListInsertion: 

	# Whenever I'll create the object of a LinkedList class head will be pointing to null initially
	def __init__(self): 
		self.head = None

	def returnLastNode(self, n):
		temp = self.head
		c = 0
		iterations = 0
		while temp is not None:
			temp = temp.next
			iterations += 1
			c += 1

		p = self.head
		for i in range(c - n):
			iterations += 1
			p = p.next
		print("Iterations: ", iterations)
		return p.data

	# Inserting at the beginning of a Linked List
	def insertAtBeginning(self, key): 
		new_node = Node(key)  
		new_node.next = self.head 
		self.head = new_node 

	# Inserting after a specific node assuming the data is given of the node after which
	# insertion has to be done.
	def insertAfter(self, nodeAfter, key): 

		h = self.head
		
		if h is None: 
			print ("The node can't be inserted in this case as the list doesn't exist.")
			return

		else:
			while h.data != nodeAfter:
				h = h.next
				if h is None:
					print("The node can't be inserted")
					return

			

			new_node = Node(key) 
			new_node.next = h.next
			h.next = new_node

 	# Inserting at the end of a Linked List (append function)
	def insertionAtEnd(self, key): 

		h = self.head

		if h is None:
			new_node = Node(key)
			self.head = new_node
		else:
			while h.next != None:
				h = h.next
			new_node = Node(key)
			h.next = new_node

	# Utility function to print the linked list 
	def printList(self): 
		h = self.head 
		while h is not None: 
			print (h.data, end = " -> ") 
			h = h.next
		print("None")



# Code execution starts here 
if __name__=='__main__': 

	myList = LinkedListInsertion()

	myList.insertionAtEnd(4)
	myList.insertionAtEnd(5)
	myList.insertionAtEnd(2)
	myList.insertionAtEnd(7)
	myList.insertionAtEnd(6)
	myList.insertionAtEnd(9)
	myList.printList()
	ans = myList.returnLastNode(2)
	print("Last 2nd Node:", ans)
	# myList.insertAtBeginning(7); 
	# print("After inserting at the beginning of Linked List: ", end = " ")
	# myList.printList()

	# myList.insertAtBeginning(8); 
	# print("After inserting at the beginning of Linked List: ", end = " ")
	# myList.printList()

	# myList.insertionAtEnd(1)
	# print("After inserting at the end of Linked List: ", end = " ")
	# myList.printList() 
	
	# myList.insertAfter(7, 12) 
	# print("After inserting after node %d in Linked List: " % (7), end = " ")
	# myList.printList()
