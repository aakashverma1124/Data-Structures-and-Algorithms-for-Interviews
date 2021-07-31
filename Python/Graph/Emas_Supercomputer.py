# @author
# Aakash Verma

# www.aboutaakash.in
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

# Problem Link: https://www.hackerrank.com/challenges/two-pluses/problem?h_r=internal-search
# Only functions are written in this code


def twoPluses(grid):
    
    temp = list()
    temp.append(['O'] * (m + 2))
    for i in range(n):
        temp.append(['O'] + list(grid[i]) + ['O'])
    temp.append(['O'] * (m + 2))
    
    # check temp grid
    # for i in range(n + 2):
    #     for j in range(m + 2):
    #         print(temp[i][j], end = " ")
    #     print()
    
    grid = temp
    answer = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            r = 0
            while grid[i + r][j] == 'G' and grid[i - r][j] == 'G' and grid[i][j + r] == 'G' and grid[i][j - r] == 'G':
                grid[i + r][j] = grid[i - r][j] = grid[i][j + r] = grid[i][j - r] = 'V'
                
                for I in range(1, n + 1):
                    for J in range(1, m + 1):
                        R = 0
                        while grid[I + R][J] == 'G' and grid[I - R][J] == 'G' and grid[I][J + R] == 'G' and grid[I][J - R] == 'G':
                            answer = max(answer, (4*r + 1) * (4*R + 1) )
                            R += 1
                r += 1
                
            r = 0
            while grid[i + r][j] == 'V' and grid[i - r][j] == 'V' and grid[i][j + r] == 'V' and grid[i][j - r] == 'V':
                grid[i + r][j] = grid[i - r][j] = grid[i][j + r] = grid[i][j - r] = 'G'
                r += 1
    return answer