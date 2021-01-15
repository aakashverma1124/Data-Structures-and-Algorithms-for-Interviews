# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

# Problem Link: https://leetcode.com/problems/number-of-islands/
# Only functions are written in this code



class Solution:
    
           
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        
        rows = len(grid)
        column = len(grid[0])
        count = 0
        visited = {}
        
        for i in range(rows):
            for j in range(column):
                if grid[i][j] == "1" and  
                    # print(grid)
                    Solution.dfs(grid,i,j, visited)
                    count += 1         
                    
        return count
    
    def dfs(arr, x, y, v):
        if x >= len(arr) or x < 0 or y >= len(arr[0]) or y < 0 or (x,y) in v:
            return

        if arr[x][y] == "0":
            return
        
        arr[x][y] = 0
        v[(x,y)] = "Y"
        Solution.dfs(arr, x-1, y,v)
        Solution.dfs(arr, x, y-1,v)
        Solution.dfs(arr, x+1, y,v)
        Solution.dfs(arr, x, y+1,v)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        