# @author
# Aakash Verma

# Output:
# [1]
# [2, 3]
# [4, 5, 6, 7] 

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class LevelOrderTraversal:
    
    def __init__(self): 
        self.root = None

    def traverse(self, root):
        bfs = []
        if root is None:
            return bfs
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.data)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(current_level)
        return bfs
    
if __name__ == '__main__':
    tree = LevelOrderTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    ans = tree.traverse(tree.root)
    for level in ans:
        print(level)


