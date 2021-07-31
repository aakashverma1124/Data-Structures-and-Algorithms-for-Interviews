# @author
# Aakash Verma

# Output:
# 3

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class MinimumTreeDepth:
    
    def __init__(self): 
        self.root = None

    def traverse(self, root):
        minimum_depth = 0
        if root is None:
            return minimum_depth
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            minimum_depth += 1
            level_size = len(queue)
            for i in range(level_size):
                current = queue.popleft()
                
                if current.left is None and current.right is None:
                    return minimum_depth
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        return minimum_depth
    
if __name__ == '__main__':
    tree = MinimumTreeDepth()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.left = Node(7)
    ans = tree.traverse(tree.root)
    print(ans)


