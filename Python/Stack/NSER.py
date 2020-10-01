
# @author
# Aakash.Verma

# Problem: Given an array, print the Next Smaller Element (NSE) for every element.
# 		 The Next Smaller Element for an element x is the first smaller element
# 		 on the right side of x in array. Elements for which no smaller element exist,
# 		 consider next smaller element as -1.


def nextSmallerElementToRight(arr, n):
	s = []
	v = []

	for i in range(n - 1, -1, -1):
		while(len(s) != 0 and s[-1] > arr[i]):
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
	ans = nextSmallerElementToRight(arr, len(arr))
	print(ans)
