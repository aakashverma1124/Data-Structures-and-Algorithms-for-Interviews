#
# @author
# Aakash Verma
#
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from heapq import *

def sort_characters_by_frequency(string):
	frequency_map = dict()

	for char in string:
		frequency_map[char] = frequency_map.get(char, 0) + 1

	max_heap = []

	for char, frequency in frequency_map.items():
		heappush(max_heap, (-frequency, char))

	sorted_string = []

	while max_heap:
		frequency, char = heappop(max_heap)
		for i in range(-frequency):
			sorted_string.append(char)

	return ''.join(sorted_string)

if __name__ == '__main__':
	
	string = "tree"
	result = sort_characters_by_frequency(string)
	print(result)

