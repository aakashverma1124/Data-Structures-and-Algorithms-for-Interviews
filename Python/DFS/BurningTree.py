# @author
# Aakash Verma

# Output:
# 2
# 7 4 5
# 6 3
# 1 
# 0 8 

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class BurningTree:
    
    def __init__(self): 
        self.root = None

    queue = deque([])

    def burningTree(self, root, targetNode):
        if root is None:
            return 0
        if root.data == targetNode:
            print(root.data)
            if root.left is not None:
                self.queue.append(root.left)
            if root.right is not None:
                self.queue.append(root.right)
            return 1

        left = self.burningTree(root.left, targetNode)
        if(left == 1):
            queueSize = len(self.queue)
            for i in range(queueSize):
                current = self.queue.popleft()
                print(current.data, end = " ")
                if current.left is not None:
                    self.queue.append(self.current.left)
                if current.right is not None:
                    self.queue.append(self.current.right)

            if root.right is not None:
                self.queue.append(root.right)
            print(root.data)
            return 1

        right = self.burningTree(root.right, targetNode)
        if(right == 1):
            queueSize = len(self.queue)
            for i in range(queueSize):
                current = self.queue.popleft()
                print(current.data, end = " ")
                if current.left is not None:
                    self.queue.append(self.current.left)
                if current.right is not None:
                    self.queue.append(self.current.right)

            if root.left is not None:
                self.queue.append(root.left)
            print(root.data)
            return 1

        
if __name__ == '__main__':
    tree = BurningTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(1)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(8)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)

    tree.burningTree(tree.root, 2)
    while tree.queue:
        queueSize = len(tree.queue)
        for i in range(queueSize):
            current = tree.queue.popleft()
            print(current.data, end = " ")
            if current.left is not None:
                tree.queue.append(current.left)
            if current.right is not None:
                tree.queue.append(current.right)
        print()

    

    