# @author
# Aakash Verma

# Output:
# 8

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class TreeDiameter:
    
    diameter = 0

    def __init__(self): 
        self.root = None

    def findHeight(self, root):
        if root is None: return 0

        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)

        currentDiameter = leftHeight + rightHeight + 1

        self.diameter = max(currentDiameter, self.diameter)

        return max(leftHeight, rightHeight) + 1

    def findDiameter(self, root):
        self.findHeight(root)
        return self.diameter
        
        
if __name__ == '__main__':
    tree = TreeDiameter()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.left.left = Node(6)
    tree.root.right.right.right = Node(7)
    tree.root.right.right.right.left = Node(12)
    tree.root.right.right.right.right = Node(13)
    tree.root.right.left.left.left = Node(8)
    tree.root.right.left.left.right = Node(10)
    tree.root.right.left.left.right.left = Node(11)
    ans = tree.findDiameter(tree.root)
    print(ans)


