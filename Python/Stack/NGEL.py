# @author
# Aakash.Verma

# Problem: Given an array, print the Next Greater Element (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element 
# 		 on the left side of x in array. Elements for which no greater element exist, 
# 		 consider next greater element as -1.

def nextGreaterElementToLeft(arr) :

	s = []
	l = []

	s.append(arr[0])
	l.append(-1)

	for i in range(1, len(arr)):

		# if stack is not empty, then pop an element from stack. 
		# 	If the popped element is smaller than next, then 
		# 	a) push element to the list 
		# 	b) keep popping while elements are 
		# 	smaller and stack is not empty 
		while(len(s) != 0 and s[-1] < arr[i]):
			s.pop()

		if(len(s) == 0):
			l.append(-1)
		else:
			l.append(s[-1])
		
		# push next to stack so that we can find 
		# next greater for it
		s.append(arr[i])

	return l

if __name__ == '__main__':
	arr = [4, 5, 2, 25]
	l = nextGreaterElementToLeft(arr)
	print(l)