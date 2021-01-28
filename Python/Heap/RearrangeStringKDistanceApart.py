# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/
# Youtube: https://www.youtube.com/channel/UC7A5AUQ7sZTJ7A1r8J9hw9A

# Problem Statement: Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
# If possible, output any possible result.  If not possible, return the empty string.
# Problem Link: https://leetcode.com/problems/reorganize-string/


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


	return ''.join(resultString)
	if(len(resultString) == len(string)):
		return resultString
	else:
		return ""

if __name__ == '__main__':
	string1 = "Programming"
	ans1 = rearrange_string_k_distnace_apart(string1, 3)
	print(ans1)

	