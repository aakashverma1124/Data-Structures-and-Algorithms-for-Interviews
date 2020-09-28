
# @author
# Aakash.Verma

# Problem: Given an array, print the Next Greater Element (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element 
# 		 on the right side of x in array. Elements for which no greater element exist, 
# 		 consider next greater element as -1.


def nextGreaterElementToRight(arr, n):
	l = []
	s = []
	s.append(arr[0])

	for i in range(1, len(arr)):
		if(len(s) == 0):
			s.append(arr[i])
			continue

		# if stack is not empty, then pop an element from stack. 
		# 		If the popped element is smaller than next, then 
		# 		a) push element to the list 
		# 		b) keep popping while elements are 
		# 		smaller and stack is not empty 
		while len(s) != 0 and s[-1] < arr[i]:
			l.append(arr[i])
			s.pop()

		s.append(arr[i])


	while len(s) != 0:
		l.append(-1)
		s.pop()
		
	return l

if __name__ == '__main__':
	arr = [4, 5, 2, 25]
	n = len(arr)
	l = nextGreaterElementToRight(arr, n)
	print(l)