#
# @author
# Aakash Verma
#
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from heapq import *

def findKLargestNumbers(nums, k):
	min_heap = []

	for i in range(k):
		heappush(min_heap, nums[i])

	for i in range(k, len(nums)):
		if nums[i] > min_heap[0]:
			heappop(min_heap)
			heappush(min_heap, nums[i])

	return min_heap[0]

if __name__ == '__main__':
	
	print(findKLargestNumbers([3, 1, 5, 12, 2, 11], 3))
