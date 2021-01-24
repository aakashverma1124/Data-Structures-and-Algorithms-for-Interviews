from heapq import *

def top_k_numbers(arr, k):
	min_heap = []

	# add k numbers in min heap, this will add min of first k elements.
	for i in range(k):
		heappush(min_heap, arr[i])

	# now start deleting elements from root and add further elements one by one,
	for i in range(k, len(arr)):
		if arr[i] > min_heap[0]:
			heappop(min_heap)
			heappush(min_heap, arr[i])

	return list(min_heap)

if __name__ == '__main__':
	
	arr = [3, 1, 5, 12, 2, 11]
	k = 3
	print(top_k_numbers(arr, k))
