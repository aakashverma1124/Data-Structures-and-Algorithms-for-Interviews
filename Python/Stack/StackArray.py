	
# @author
# Aakash.Verma

# Stack is a LIFO data structures:
# LIFO stands for Last In First Out 

# We can't access any element except top. Top is that element which has been inserted at last
# and can be retrieved first.

# I am assuming that you are here after going through the theory of Stack and looking for implementation.

# Output:
# The element is pushed and top points to => 10
# The element is pushed and top points to => 20
# The element is pushed and top points to => 30
# Deleted element is: 30
# Top element is: 20


class StackArray:

	# We are assuming that the size of our stack is 1000, you may take any size
	MAX = 1000

	stack = [] 	# stack
	
	# As soon as the object of this class is created, top is assigned as -1.
	def __init__(self):
		self.top = -1

	# It checks whether the stack is empty or not, obviously if top is -1, the stack will be empty.
	def isEmpty(self):
		if(self.top < 0):
			return True
		return False

	# It checks whether the stack is full or not, obviously if top is MAX - 1, the stack will be full.
	def isFull(self):
		if(self.top >= self.MAX - 1):
			return True
		return False



	#function to push an element in the stack.
	def push(self, key):
		# if top becomes equal to MAX-1, then it means the array is full and we can't insert any element.
		# isFull() will return true, if stack is full.
		if(self.isFull()):
			print("Stack Overflow")
			return False

		# otherwise, increment top and add key to a[top], here top works as an index only. 
		self.top += 1
		self.stack.append(key)
		print("The element is pushed and top points to => ",self.stack[self.top])
		return True

	# function to delete an element in the stack, it returns the deleted element otherwise -1. */
	def pop(self):
		# if top is -1, it means there is no element to be deleted
		if(self.isEmpty()):
			print("Stack underflow")
			return -1

		# otherwise, delete the element from the top and decrement top.
		deletedElement = self.stack[self.top]
		self.top -= 1
		return deletedElement

	# function through which we can see the element present at the top.
	def peek(self):
		if(self.isEmpty()):
			print("There is no record in the stack.")
			return -1

		peekElement = self.stack[self.top];
		return peekElement;

if __name__ == '__main__': 
	s = StackArray()
	s.push(10) # now top is 10
	s.push(20) # now top is 20
	s.push(30) # now top is 30
	temp = s.pop() # after performing pop, top will point to 20 again.
	print("Deleted element is: ", temp)
	print("Top element is: " , s.peek())
