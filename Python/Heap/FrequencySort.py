# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/
# Youtube: https://www.youtube.com/channel/UC7A5AUQ7sZTJ7A1r8J9hw9A

# Problem Statement: Given a string, sort it in decreasing order based on the frequency of characters.
# Problem Link: https://leetcode.com/problems/sort-characters-by-frequency/

from heapq import *

def sort_character_by_frequency(string):
	hash_table = dict()

	for char in string:
		hash_table[char] = hash_table.get(char, 0) + 1

	max_heap = []

	for char, frequency in hash_table.items():
		heappush(max_heap, (-frequency, char))

	sorted_string = []

	while max_heap:
		frequency, char = heappop(max_heap)
		for i in range(-frequency):
			sorted_string.append(char)

	return ''.join(sorted_string)

if __name__ == '__main__':
	
	string1 = "Programming"
	ans1 = sort_character_by_frequency(string1)
	print(ans1)

	string2 = "abcbab"
	ans2 = sort_character_by_frequency(string2)
	print(ans2)

