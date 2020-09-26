
# @author
# Aakash.Verma

# In this code, we'll implement the Stack using Linked List. 
# In the previous code, there was a problem that the stack using array is of fixed size which means
# we can't increase the size of the stack as per the requirement. 
# But in case of linked list, we'll create nodes dynamically as per our need and the size of stack will
# grow as per the requirement.

# Output:

# The element is pushed and top points to => 10
# The element is pushed and top points to => 20
# The element is pushed and top points to => 30
# Deleted Element: 30
# Top element is: 20

import sys

# A simple Node Structure 
class Node:
	def __init__(self, key):
		self.data = key
		self.next = None

class StackLinkedList:

	# defining node as None upon creation of the object.
	def __init__(self):
		self.root = None;

	# if root doesn't point to anything, then stack is obviously empty and it will return true.
	def isEmpty(self):
		if(self.root is None):
			return True
		return False

	def push(self, key):

		# creating a node with the given key.
		node = Node(key)

		# IMPORTANT
		# Let's suppose: initially we have 10 in the stack and root points to 10 only.
		# root => 10

		# Now, we'll push one more node to the stack, so it should be like this:
		# 10 -> 20 (and acc. to us, root still should point to 10, because it's a root node)
		# But Stack is a LIFO data structure and the element which is added at last should be
		# deleted first.

		# We can do it so by iterating everytime till the last node and delete it in pop() function.
		# But this will be time taking process everytime.
		# For example: 
		# 10 -> 20 -> 30 -> 40 -> 50
		# So, 50 is the last node and should be deleted it when pop() will be called.
		# Same problem will be to find the top element by using peek()
		# We'll have to iterate everytime.

		# So, we can do some changes while pushing element in the stack.
		# What we are doing is: if 10 is already there in the linked list and I want to add 20.
		# So my list should be like this: 10 <- 20 and root will point to 20 
		# instead of 10 -> 20 and root points to 10

		# the idea is if initially root was poining to 10.
		# then I store root into tempNode
		# I make node as root
		# and I add node.next to tempNode.
		# which turns my list as 20 -> 10


		node.next = self.root
		self.root = node
		print("The element is pushed and top points to => ", self.root.data)
 
	# If isEmpty() returns true, we can't delete element.
	# Otherwise we return root.data because everytime root points to last added element, 
	# so we directly return root.data and we make root = root.next;
	def pop(self) :
		deletedElement = -sys.maxsize-1
		if(self.isEmpty()):
			print("Stack Underflow")
		else:
			deletedElement = self.root.data
			self.root = self.root.next
		return deletedElement

	# simply returns the root.data
	def peek(self):
		topElement = -sys.maxsize-1
		if(self.isEmpty()):
			System.out.println("Stack Underflow")
		else:
			topElement = self.root.data
		return topElement

if __name__ == '__main__':
	s = StackLinkedList()
	s.push(10)
	s.push(20)
	s.push(30)
	deletedElement = s.pop()
	print("Deleted Element: ", deletedElement)
	print("Top element is: ", s.peek())