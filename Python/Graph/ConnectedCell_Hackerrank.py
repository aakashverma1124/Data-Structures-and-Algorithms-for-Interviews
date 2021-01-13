# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

# Problem Link: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
# Only functions are written in this code

def getMaxRegion(matrix, row, col):
    if (row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0])):
        return 0
    if matrix[row][col] == 0:
        return 0
    matrix[row][col] = 0 # this is because, we don't want to infinite recursive calls.
    size = 1 # because we have visited one 1 and that's why we are in this function
    for r in range(row - 1, row + 2):  # because we have to from row - 1 to row + 1
        for c in range(col - 1, col + 2):
            if (r != row or c != col):
                size += getMaxRegion(matrix, r, c)
                
    return size
    
# Complete the connectedCell function below.
def connectedCell(matrix):
    maxRegion = 0
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if (matrix[i][j] == 1):
                size = getMaxRegion(matrix, i, j)
                maxRegion = max(size, maxRegion)
    return maxRegion


# main method
# ...
# ...
# ...