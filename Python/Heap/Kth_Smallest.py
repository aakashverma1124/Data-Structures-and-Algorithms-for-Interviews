# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/
# Youtube: https://www.youtube.com/channel/UC7A5AUQ7sZTJ7A1r8J9hw9A

# Problem Statement: Given an unsorted array of numbers, find Kth smallest number in it.

from heapq import *

def kth_smallest(arr, k):
	max_heap = []

	# add k numbers in max heap, this will add max of first k elements.
	for i in range(k):
		heappush(max_heap, -arr[i])

	# now start deleting elements from root and add further elements one by one,
	for i in range(k, len(arr)):
		if -arr[i] > max_heap[0]:
			heappop(max_heap)
			heappush(max_heap, -arr[i])

	# now root has kth smallest element in the max heap
	return -max_heap[0]

if __name__ == '__main__':
	
	arr = [1, 5, 12, 2, 11, 5]
	k = 3
	print(kth_smallest(arr, k))
