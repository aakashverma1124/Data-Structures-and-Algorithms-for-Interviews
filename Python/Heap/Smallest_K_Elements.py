#
# @author
# Aakash Verma
#
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from heapq import *

def findKSmallestNumbers(nums, k):
	max_heap = []

	for i in range(k):
		heappush(max_heap, -nums[i])

	for i in range(k, len(nums)):
		if -nums[i] > max_heap[0]:
			heappop(max_heap)
			heappush(max_heap, -nums[i])

	ans = [-i for i in max_heap]
	return ans

if __name__ == '__main__':
	
	print(findKSmallestNumbers([3, 1, 5, 12, 2, 11], 3))
