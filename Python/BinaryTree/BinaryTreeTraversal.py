
# @author
# Aakash Verma

# Output:
# Pre Order Traversal is: 1 2 4 5 3 6 7 
# In Order Traversal is: 4 2 5 1 6 3 7 
# Post Order Traversal is: 4 5 2 6 7 3 1 


# Creating a structure for the node.
# Initializing the node's data upon calling its constructor.

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class BinaryTreeTraversal:
    
    # Assigning root as null initially. So as soon as the object will be created 
    # of this BinaryTreeTraversal class, root will be set as null.
    def __init__(self): 
        self.root = None
    
    # Pre Order Traversal
    def preOrder(self, root):
        if(root is None):
            return
        print(root.data, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)


    # In Order Traversal
    def inOrder(self, root):
        if(root is None):
            return
        self.inOrder(root.left)
        print(root.data, end = " ")
        self.inOrder(root.right)

    # Post Order Traversal */
    def postOrder(self, root):
        if(root is None):
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end = " ")
    
#main method
if __name__ == '__main__':
    tree = BinaryTreeTraversal()
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
    print("In Order Traversal is:", end = " ")
    tree.inOrder(tree.root)
    print()
    print("Post Order Traversal is:", end = " ")
    tree.postOrder(tree.root)
    print()
