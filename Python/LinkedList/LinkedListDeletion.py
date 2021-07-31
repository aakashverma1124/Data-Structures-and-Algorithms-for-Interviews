#
#
#
#   @author
#   Aakash Verma
#	
# 	Deletion in Linked List
#
#	Output: 
#
#	Original List is:  3 4 5 6 7 9 
#	After Deletion:  3 4 5 7 9 	
#


# Below is the structute of a node which is used to create a new node every time.
class Node: 

	def __init__(self, data): 
		self.data = data
		self.next = None # None is nothing but null 

# Creating a class for implementing the code for Deletion in a Linked List
class LinkedList: 
	
	# Whenever I'll create the object of a LinkedList class head will be pointing to null initially
	def __init__(self): 
		self.head = None


	# Inserting at the end of a Linked List (append function)
	def append(self, key): 

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

	# deleting a given node
	def deleteNode(self, key):
		h = self.head
		prev = None

		if h is None:
			print("The list is empty, the node can't be deleted.")
			return

		if h.data == key:
			self.head = h.next
			return

		while h is not None and h.data != key:
			prev = h
			h = h.next

		if h is None:
			print("The key is not present in the list.")
			return

		prev.next = h.next



# Code execution starts here 
if __name__=='__main__': 

	myList = LinkedList() 
	myList.append(3)
	myList.append(4)
	myList.append(5)
	myList.append(6)
	myList.append(7)
	myList.append(9) 
	print("Original List is: ", end = " ")
	myList.printList()
	myList.deleteNode(6)
	print("After Deletion: ", end = " ")
	myList.printList()

