# @author
# Aakash Verma

# Output:
# 42

from collections import *
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class PathWithMaximumSum:

    def __init__(self): 
        self.root = None

    def findMaxSum(self, root):
        if root is None: return 0

        leftSum = self.findMaxSum(root.left)
        rightSum = self.findMaxSum(root.right)

        leftSum = max(leftSum, 0)
        rightSum = max(rightSum, 0)

        currentSum = leftSum + rightSum + root.data

        self.maxSum = max(currentSum, self.maxSum)

        return max(leftSum, rightSum) + root.data

    def findMaximumPathSum(self, root):
        self.maxSum = -math.inf
        self.findMaxSum(root)
        return self.maxSum
        
        
if __name__ == '__main__':
    tree = PathWithMaximumSum()
    tree.root = Node(10)
    tree.root.left = Node(2)
    tree.root.right = Node(10)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(1)
    tree.root.right.left = Node(-25)
    tree.root.right.left.left = Node(3)
    tree.root.right.left.right = Node(4)
    ans = tree.findMaximumPathSum(tree.root)
    print(ans)


