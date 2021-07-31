# @author
# Aakash Verma

# Output:
# 5

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class LowestCommonAncestor:
    
    def __init__(self): 
        self.root = None

    def lowestCommonAncestor(self, root, p, q):

        if(root is None): 
            return None

        if root.data == p.data or root.data == q.data:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        return left if left is not None else right
        
if __name__ == '__main__':
    tree = LowestCommonAncestor()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(1)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(8)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)

    p = tree.root.left
    q = tree.root.left.right.right

    lca = tree.lowestCommonAncestor(tree.root, p, q)
    print(lca.data)

    