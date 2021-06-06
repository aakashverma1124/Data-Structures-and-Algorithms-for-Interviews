# @author
# Aakash Verma

# Output:
# 6

from collections import *

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class LevelOrderSuccessor:
    
    def __init__(self): 
        self.root = None

    def levelOrderSuccessor(self, root, key):
        if root is None:
            return None
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            current = queue.popleft()
            
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

            if current.data == key:
                break

        return queue.popleft()
    
if __name__ == '__main__':
    tree = LevelOrderSuccessor()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.left = Node(7)
    ans = tree.levelOrderSuccessor(tree.root, 4)
    print(ans.data)


