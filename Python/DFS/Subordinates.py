import sys
sys.setrecursionlimit(10**6)
 
def dfs(curr, prev, count, tree):
    count[curr] = 1
    for nbr in tree[curr]:
        dfs(nbr, curr, count, tree)
        count[curr] += count[nbr]
    
if __name__ == '__main__':
	n = int(input())
	tree = dict()
	for i in range(1, n + 1):
		tree[i] = []
	emp = list(map(int, input().split()))
	for i in range(n - 1):
		tree[emp[i]].append(i + 2)
	count = [0] * (n + 1)
	dfs(1, 0, count, tree)
	for i in range(1, n + 1):
	    print(count[i] - 1, end = " ")
	print()