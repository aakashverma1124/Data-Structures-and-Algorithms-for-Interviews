# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/
# Youtube: https://www.youtube.com/channel/UC7A5AUQ7sZTJ7A1r8J9hw9A

# Problem Statement: Given a string and a number ‘K’, find if the string can be rearranged such that the same characters 
# are at least ‘K’ distance apart from each other.
# Problem Link: https://leetcode.com/problems/rearrange-string-k-distance-apart/


from heapq import *
from collections import deque

def rearrange_string_k_distnace_apart(string, k):

	if k <= 1:
		return string

	hash_map = dict()
	for char in string:
		hash_map[char] = hash_map.get(char, 0) + 1

	max_heap = []

	for char, freq in hash_map.items():
		heappush(max_heap, (-freq, char))

	queue = deque([])
	resultString = []

	while max_heap:
		freq, char = heappop(max_heap)
		resultString.append(char)
		queue.append((char, freq + 1))

		if len(queue) == k:
			character, frequency = queue.popleft()
			if -frequency > 0:
				heappush(max_heap, (frequency, character))


	resultString = ''.join(resultString)
	if(len(resultString) == len(string)):
		return resultString
	else:
		return ""

if __name__ == '__main__':
	string1 = "aaadbbcc"
	ans1 = rearrange_string_k_distnace_apart(string1, 2)
	print(ans1)

	