#
# @author
# Aakash Verma
#
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from heapq import *

def findKthSmallestNumber(nums, k):
	max_heap = []

	for i in range(k):
		heappush(max_heap, -nums[i])

	for i in range(k, len(nums)):
		if -nums[i] > max_heap[0]:
			heappop(max_heap)
			heappush(max_heap, -nums[i])

	return -max_heap[0]

if __name__ == '__main__':
	
	print(findKthSmallestNumber([3, 1, 5, 12, 2, 11], 3))
