
# @author
# Aakash.Verma

# Problem: Given an array, print the Next Smaller Element (NSE) for every element.
# 		 The Next Smaller Element for an element x is the first smaller element
# 		 on the left side of x in array. Elements for which no smaller element exist,
# 		 consider next smaller element as -1.


def nextSmallerElementToLeft(arr, n):
	s = []
	v = []

	for i in range(0, n):

		if(len(s) == 0):
			v.append(-1)

		elif(s[-1] < arr[i]):
			v.append(s[-1])

		else:

			while(len(s) != 0 and s[-1] >= arr[i]):
				s.pop()

			if len(s) == 0 :
				v.append(-1)

			else:
				v.append(s[-1])

		s.append(arr[i])

	return v

if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = nextSmallerElementToLeft(arr, len(arr))
	print(ans)
