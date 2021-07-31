#
#
#
#   @author
#   Aakash Verma
#	
# 	Nth Node from the Last of a Linked List
#
#	Output: 
#
#	Original List is:  3 4 5 6 7 9 
#	6
#


# Below is the structute of a node which is used to create a new node every time.
class Node: 

	def __init__(self, data): 
		self.data = data
		self.next = None # None is nothing but null 

# Creating a class for implementing the code for nth Node from end in a Linked List
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

	# nth Node from end
	def nthNodeFromEnd(self, nthNode):
		prev = self.head
		curr = self.head
		if self.head is None:
			print("The list doesn't exist.")
			return

		# curr pointer is being moved ahead n times.
		for i in range(nthNode):
			if curr is not None:
				curr = curr.next
			else:
				print("Enough nodes are not present in the linked list.")
				return

		# Now the difference between prev and curr pointer is n

		# now we'll move prev and curr pointer both until curr becomes null and finally prev will be at n from last
		while curr is not None:
			curr = curr.next
			prev = prev.next

		# finally printing data of nth node from last
		print(prev.data)


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
	myList.nthNodeFromEnd(3)

