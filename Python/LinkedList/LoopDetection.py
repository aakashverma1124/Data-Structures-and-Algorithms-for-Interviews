#
#
#
#   @author
#   Aakash Verma
#	
# 	Middle Of a Linked List
#
#	Output: 
#	true
#


# Below is the structute of a node which is used to create a new node every time.
class Node: 

	def __init__(self, data): 
		self.data = data
		self.next = None # None is nothing but null 

# Creating a class for implementing the code for Loop Detection in a LinkedList
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

	# middle of a linked list
	def isLoopFound(self):
		fast = self.head
		slow = self.head

		if self.head is None:
			print("The list doesn't exist.")
			return False

		
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True

		return False


# Code execution starts here 
if __name__=='__main__': 

	myList = LinkedList() 
	myList.append(3)
	myList.append(4)
	myList.append(5)
	myList.append(6)
	myList.append(7)
	myList.head.next.next.next.next.next = myList.head.next.next
	loopFound = myList.isLoopFound()
	print(loopFound)


