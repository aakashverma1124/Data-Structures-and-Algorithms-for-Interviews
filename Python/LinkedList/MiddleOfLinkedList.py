#
#
#
#   @author
#   Aakash Verma
#	
# 	Middle Of a Linked List
#
#	Output: 
#
#	Original List is:  3 4 5 6 7 
#	Middle of List is: 5
#	Original List is:  3 4 5 6 7 9 
#	Middle of List is: 6
#
#	Note: In case of even number of nodes, we are printing the ((n/2)+1)th node. 
#	If you want to print (n/2)th node you can customize your code as per your requirement.	
#
#


# Below is the structute of a node which is used to create a new node every time.
class Node: 

	def __init__(self, data): 
		self.data = data
		self.next = None # None is nothing but null 

# Creating a class for implementing the code for Middle in a Linked List
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

	# middle of a linked list
	def findMiddle(self):
		fast = self.head
		slow = self.head

		if self.head is None:
			print("The list doesn't exist.")
			return

		# move one pointer one time & other pointer two times
		# which will result fast pointer at the end and slow pointer in the middle of a list
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next

		# finally printing data of middle of linked list
		print(slow.data)


# Code execution starts here 
if __name__=='__main__': 

	myList = LinkedList() 
	myList.append(3)
	myList.append(4)
	myList.append(5)
	myList.append(6)
	myList.append(7)

	print("Original List is: ", end = " ")
	myList.printList()
	print("Middle of List is:", end = " ")
	myList.findMiddle()

	myList.append(9)

	print("Original List is: ", end = " ")
	myList.printList()
	print("Middle of List is:", end = " ")
	myList.findMiddle()

