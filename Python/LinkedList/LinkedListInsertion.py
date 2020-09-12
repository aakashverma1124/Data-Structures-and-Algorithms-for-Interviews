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
					print("The node can't be inserted");
					return;

			

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
		while (h): 
			print (h.data, end = " ") 
			h = h.next
		print()



# Code execution starts here 
if __name__=='__main__': 

	myList = LinkedListInsertion() 

	myList.insertionAtEnd(1)
	print("Initial Linked List: ", end = " ")
	myList.printList() 


	myList.insertionAtEnd(6) 
	print("After inserting at the end of Linked List: ", end = " ")
	myList.printList()

	myList.insertAtBeginning(7); 
	print("After inserting at the beginning of Linked List: ", end = " ")
	myList.printList()

	myList.insertAtBeginning(8); 
	print("After inserting at the beginning of Linked List: ", end = " ")
	myList.printList()

	myList.insertAtBeginning(9); 
	print("After inserting at the beginning of Linked List: ", end = " ")
	myList.printList()
	
	myList.insertAfter(7, 8) 
	print("After inserting after node 7 in Linked List: ", end = " ")
	myList.printList()
