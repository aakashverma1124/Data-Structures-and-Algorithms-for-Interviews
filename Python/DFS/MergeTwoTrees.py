# @author
# Aakash Verma

# Output:
# 3 6 3 1 8 10 5 


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class MergeTwoTrees:
    
    def __init__(self): 
        self.root1 = None
        self.root2 = None

    def traverse(self, root):
        if(root is None):
            return
        print(root.data, end = " ")
        self.traverse(root.left)
        self.traverse(root.right)

    def merge(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root1.data += root2.data

        root1.left = self.merge(root1.left, root2.left)
        root1.right = self.merge(root1.right, root2.right)

        return root1

        
if __name__ == '__main__':
    tree = MergeTwoTrees()
    tree.root1 = Node(1)
    tree.root1.left = Node(2)
    tree.root1.right = Node(3)
    tree.root1.right.left = Node(4)
    tree.root1.right.right = Node(5)

    tree.root2 = Node(2)
    tree.root2.left = Node(4)
    tree.root2.right = Node(5)
    tree.root2.left.left = Node(3)
    tree.root2.left.right = Node(1)
    tree.root2.right.left = Node(6)

    root = tree.merge(tree.root1, tree.root2)
    tree.traverse(root)
    

    