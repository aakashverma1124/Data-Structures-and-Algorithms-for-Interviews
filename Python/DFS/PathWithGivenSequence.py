# @author
# Aakash Verma

# Output:
# true

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class PathWithGivenSequence:
    
    def __init__(self): 
        self.root = None

    def findSequence(self, root, sequence, index):
    	if root is None: return False

    	if index >= len(sequence) or root.data != sequence[index]:
    		return False

    	if(root.left is None and root.right is None and index == len(sequence) - 1):
    		return True

    	return self.findSequence(root.left, sequence, index + 1) or self.findSequence(root.right, sequence, index + 1)

    def hasPath(self, root, sequence):
        if root is None: return len(sequence) == 0

        return self.findSequence(root, sequence, 0)

        
        
if __name__ == '__main__':
    tree = PathWithGivenSequence()
    tree.root = Node(3)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(5)
    ans = tree.hasPath(tree.root, [3, 1, 2])
    print(ans)


