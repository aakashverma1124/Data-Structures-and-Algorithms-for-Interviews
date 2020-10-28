# @author
# Aakash.Verma

# Queue is a FIFO/LILO data structures:
# FIFO stands for First In First Out 

# We can't access any element except front. Front is that element which has been inserted at first
# and will be retrieved first. Rear is that element which is inserted at last and will be deleted 
# at last.

# I am assuming that you are here after going through the theory of Queue and looking for implementation.

# Output: 	
# Enqueue Operation Done, rear is at 11
# Enqueue Operation Done, rear is at 12
# Enqueue Operation Done, rear is at 13
# Deleted Element is: 11
# Front element is: 12

# Run using: python filename.py

# A simple Node Structure 
class Node:
	def __init__(self, key):
		self.data = key
		self.next = None

class QueueUsingLinkedList:

	# defining front & rear as None upon creation of the object.
	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, item) : 
		new_node = Node(item)
		new_node.data = item
		
		if self.rear is None : 
			self.front = self.rear = new_node 
			print("Enqueue Operation Done, rear is at ", self.rear.data)
			return

		self.rear.next = new_node; 
		self.rear = new_node; 
		print("Enqueue Operation Done, rear is at ", self.rear.data)

	def dequeue(self):
		if self.front is None:
			return -1 
	
		temp = self.front
		self.front = self.front.next; 

		if self.front is None:
			self.rear = None

		return temp.data

	def peek(self):
		if self.front is None:
			return -1
		return self.front.data

if __name__ == '__main__':
	q = QueueUsingLinkedList()
	q.enqueue(11)
	q.enqueue(12)
	q.enqueue(13)
	deleted = q.dequeue()
	print("Deleted Element is: ", deleted)
	print("Front Element is: ", q.peek())

