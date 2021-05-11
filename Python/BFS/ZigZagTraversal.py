# @author
# Aakash Verma

# Output:
# [1]
# [3, 2]
# [4, 5, 6, 7] 

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class ZigZagTraversal:
    
    def __init__(self): 
        self.root = None

    def traverse(self, root):
        bfs = []
        left_to_right = True
        if root is None:
            return bfs
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            current_level = deque()
            for i in range(level_size):
                current = queue.popleft()
                
                if left_to_right:
                    current_level.append(current.data)
                else:
                    current_level.appendleft(current.data)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(current_level)
            left_to_right = not left_to_right
        return bfs
    
if __name__ == '__main__':
    tree = ZigZagTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    ans = tree.traverse(tree.root)
    for level in ans:
        print(list(level))