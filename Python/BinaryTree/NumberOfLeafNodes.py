# @author
# Aakash Verma

# Output:
# Pre Order Traversal is: 1 2 4 5 3 6 7 
# Number Of non-Leaf Nodes: 3


# Creating a structure for the node.
# Initializing the node's data upon calling its constructor.

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class NumberOfLeafNodes:
    
    # Assigning root as null initially. So as soon as the object will be created 
    # of this NumberOfLeafNodes class, root will be set as null.
    def __init__(self): 
        self.root = None
    
    # Pre Order Traversal
    def preOrder(self, root):
        if root is None:
            return
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def numLeafNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1;
        return self.numLeafNodes(root.left) + self.numLeafNodes(root.right)
    
# main method
if __name__ == '__main__':
    tree = NumberOfLeafNodes()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print("Pre Order Traversal is:",  end = " ")
    tree.preOrder(tree.root)
    print()
    print("Number Of Leaf Nodes:", end = " ")
    print(tree.numLeafNodes(tree.root))
    
 