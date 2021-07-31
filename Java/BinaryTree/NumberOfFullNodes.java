/*
*
*   @author
*   Aakash Verma
* 	
*	Problem: Given a Binary Tree, count the total number of full nodes present in BT.
*	
* 	Output: 
*	Traversal is: 1 2 4 5 3 6 7 
*	Number Of Full Nodes: 3
*
*/

/* Creating a structure for the node.
   Initializing the nodes datas upon calling its constructor. */
class Node {
	int data;
	Node left;
	Node right;

	public Node(int key) {
		data = key;
		left = null;
		right = null;
	}
}

/* Defining class for the Binary Tree */
class NumberOfFullNodes {

    /* Creating a root node for the Tree. */
    static Node root;
    

    /* Assigning root as null initially. */
    NumberOfFullNodes() {
        root = null;
    }

    /* Counting number Of full Nodes */
    int numFullNodes(Node root) {
    	if(root == null)
    		return 0;
        if(root.left == null && root.right == null)
            return 0;
    	return numFullNodes(root.left) + numFullNodes(root.right) + ((root.left != null) && (root.right != null) ? 1 : 0);
    }
    
	
    /* Pre Order Traversal */
    void preOrder(Node root) {
        if(root == null)
            return;
        System.out.print(root.data + " ");
        preOrder(root.left);
        preOrder(root.right);
    }
    
    /* main method */
    public static void main (String[] args) {
        NumberOfFullNodes tree = new NumberOfFullNodes();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);
        System.out.print("Traversal is: ");
        tree.preOrder(root);
        System.out.println();
        System.out.print("Number Of Full Nodes: " + tree.numFullNodes(root));
        System.out.println();
    }
}
