/*
*
*   @author
*   Aakash Verma
*
*/


/*  
    Creating a structure for the node.
    Initializing the node's data upon calling its constructor.
*/
class Node {
    int data;
    Node left, right;
    
    public Node(int key) {
        data = key;
        left = right = null;
    }
}


class BinaryTree {

	/* Creating a root node for the Tree */
    static Node root;
    
    /* 
        Assigning root as null initially. So as soon as the object will be created 
        of this BinaryTreeTraversal class, root will be set as null.
    */
    BinaryTree() {
        root = null;
    }

	/* main method */
    public static void main (String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);
}