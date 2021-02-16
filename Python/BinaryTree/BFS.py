# @author
# Aakash Verma

# Output:


# Creating a structure for the node.
# Initializing the node's data upon calling its constructor.

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class BFS:
    
    # Assigning root as null initially. So as soon as the object will be created 
    # of this BinaryTreeTraversal class, root will be set as null.
    def __init__(self): 
        self.root = None

    def bfs(self, root): 
        if root is None:
            return None  

        queue = deque()
        bfs = []

        queue.append(root)

        itr = 1
        while len(queue) != 0:
            levelSize = len(queue)
            temp = []
            for i in range(levelSize):
                curr = queue.popleft()
                temp.append(curr.data)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)

            if itr % 2 == 0:
                temp.reverse()
            itr += 1
            bfs.append(temp)

        return bfs

#main method
if __name__ == '__main__':
    tree = BFS()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    ans = tree.bfs(tree.root)
    print(ans)

