# @author
# Aakash Verma

# Output:
# true

from collections import *
from itertools import count

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class CountPathsForASum:
    
    def __init__(self): 
        self.root = None

    def countAllPaths(self, root, target, current_path):
        if root is None:
            return 0
        
        current_path.append(root.data)
        path_sum = 0
        path_count = 0

        for i in range(len(current_path) - 1, -1, -1):
            path_sum += current_path[i]
            if path_sum == target:
                path_count += 1

        left_count = self.countAllPaths(root.left, target, current_path)
        right_count = self.countAllPaths(root.right, target, current_path)
        path_count += (left_count + right_count)

        del current_path[-1]

        return path_count


    def countPaths(self, root, target):
        current_path = []
        return self.countAllPaths(root, target, current_path)
        
if __name__ == '__main__':
    tree = CountPathsForASum()
    tree.root = Node(1)
    tree.root.left = Node(7)
    tree.root.right = Node(9)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(3)
    ans = tree.countPaths(tree.root, 12)
    print(ans)


