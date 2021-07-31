# @author
# Aakash Verma

# Output:
# 1008

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class BinaryTreePathSum:
    
    def __init__(self): 
        self.root = None

    def findPathSum(self, root, pathSum):
        if root is None:
            return 0

        pathSum = 10 * pathSum + root.data

        if root.left is None and root.right is None:
            return pathSum

        return self.findPathSum(root.left, pathSum) + self.findPathSum(root.right, pathSum)

    def findSumPathNumbers(self, root):
        return self.findPathSum(root, 0)
        
if __name__ == '__main__':
    tree = BinaryTreePathSum()
    tree.root = Node(3)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    ans = tree.findSumPathNumbers(tree.root)
    print(ans)


