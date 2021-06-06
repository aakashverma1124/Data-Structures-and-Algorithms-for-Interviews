# @author
# Aakash Verma

# Output:


# Creating a structure for the node.
# Initializing the node's data upon calling its constructor.

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


# Defining class for the Binary Tree
class BST_Search:
    
    # Assigning root as null initially. So as soon as the object will be created 
    # of this BinaryTreeTraversal class, root will be set as null.
    def __init__(self): 
        self.root = None

    def bst_search(self, root, key):

        if root is None or root.data == key:
            return root

        elif root.data < key:
            return self.bst_search(root.right, key)
        
        else:
            return self.bst_search(root.left, key)
        
        
    
#main method
if __name__ == '__main__':
    tree = BST_Search()
    tree.root = Node(20)
    tree.root.left = Node(15)
    tree.root.right = Node(25)
    tree.root.left.left = Node(14)
    tree.root.left.right = Node(17)
    tree.root.right.left = Node(22)
    tree.root.right.right = Node(30)
    tree.root.right.left.right = Node(24)

    ans = tree.bst_search(tree.root, 24)
    if ans is None:
        print(False)
    else:
        print(True)

