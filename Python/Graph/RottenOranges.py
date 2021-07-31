# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

# Problem Link: https://leetcode.com/problems/rotting-oranges/
# Only functions are written in this code


from collections import deque

class Node:

	def __init__(self, time, x, y):
		self.time = time
		self.x = x
		self.y = y

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        queue = deque([])
        ans = 0
        for i in range(row):
            for j in range(col):
                if(grid[i][j] == 2):
                    node = Node(0, i, j)
                    queue.append(node)

        while(len(queue) != 0):
            current_node = queue.popleft()

            curr_time = current_node.time
            curr_x = current_node.x
            curr_y = current_node.y

            if (curr_x - 1 >= 0):
                if(grid[curr_x - 1][curr_y] == 1):
                    new_node = Node(curr_time + 1, curr_x - 1, curr_y)
                    grid[curr_x - 1][curr_y] = 2
                    queue.append(new_node)
                    ans = new_node.time

            if (curr_x + 1 <= row - 1):
                if(grid[curr_x + 1][curr_y] == 1):
                    new_node = Node(curr_time + 1, curr_x + 1, curr_y)
                    grid[curr_x + 1][curr_y] = 2
                    queue.append(new_node)
                    ans = new_node.time

            if (curr_y - 1 >= 0):
                if(grid[curr_x][curr_y - 1] == 1):
                    new_node = Node(curr_time + 1, curr_x, curr_y - 1)
                    grid[curr_x][curr_y - 1] = 2
                    queue.append(new_node)
                    ans = new_node.time

            if (curr_y + 1 <= col - 1):
                if(grid[curr_x][curr_y + 1] == 1):
                    new_node = Node(curr_time + 1, curr_x, curr_y + 1)
                    grid[curr_x][curr_y + 1] = 2
                    queue.append(new_node)
                    ans = new_node.time
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return ans