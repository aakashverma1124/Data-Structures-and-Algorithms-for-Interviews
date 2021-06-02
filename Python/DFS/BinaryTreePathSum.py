# @author
# Aakash Verma

# Output:
# true

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class BinaryTreePathSum:
    
    def __init__(self): 
        self.root = None

    def hasPath(self, root, sum):
        if(root is None): return False

        if(root.data == sum and root.left is None and root.right is None):
            return True

        return self.hasPath(root.left, sum - root.data) or self.hasPath(root.right, sum - root.data)
        
if __name__ == '__main__':
    tree = BinaryTreePathSum()
    tree.root = Node(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(5)
    tree.root.left.left.left = Node(3)
    ans = tree.hasPath(tree.root, 23)
    print(ans)


