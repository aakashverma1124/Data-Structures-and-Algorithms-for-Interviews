# @author
# Aakash Verma

# Output:
# True


from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class SymmetricTree:
    
    def __init__(self): 
        self.root = None

    def findSymmetric(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.data == root2.data) and self.findSymmetric(root1.left, root2.right) and self.findSymmetric(root1.right, root2.left)

    def isSymmetric(self, root):
        
        return self.findSymmetric(root, root)

        
if __name__ == '__main__':
    tree = SymmetricTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(3)
    ans = tree.isSymmetric(tree.root)
    print(ans)
    

    