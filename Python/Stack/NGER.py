
# @author
# Aakash.Verma

# Problem: Given an array, find an array of Next Greater Elements (NGE) for every element.
# 		 The Next Greater Element for an element x is the first greater element
# 		 on the right side of x in array. Elements for which no greater element exist,
# 		 consider next greater element as -1.


def nextGreaterElementToRight(arr, n):
	s = []
	v = []

	for i in range(n-1, -1, -1):
		while(len(s) != 0 and s[-1] <= arr[i]):
			s.pop()

		if len(s) == 0 :
			v.append(-1)

		else:
			v.append(s[-1])
		s.append(arr[i])

	v.reverse()
	return v

if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = nextGreaterElementToRight(arr, len(arr))
	print(ans)
