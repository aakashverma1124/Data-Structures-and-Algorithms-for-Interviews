/*
*   @author
*   Aakash Verma
*
*   Output:
*   true
*
*/

import java.util.*;

class Node {
    int data;
    Node left, right;
    public Node(int key) {
        data = key;
        left = right = null;
    }
}


class SymmetricTree {

    static Node root;
    SymmetricTree() {
        root = null;
    }

    public static boolean findSymmetric(Node root1, Node root2) {
        if(root1 == null && root2 == null) 
            return true;
        
        if(root1 == null || root2 == null) 
            return false;
        
        return (root1.data == root2.data) && 
                findSymmetric(root1.left, root2.right) && 
                findSymmetric(root1.right, root2.left);
    }

    public static boolean isSymmetric(Node root) {
        return findSymmetric(root, root);
    }

    public static void main (String[] args) {
        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(2);
        root.left.left = new Node(3);
        root.left.right = new Node(4);
        root.right.left = new Node(4);
        root.right.right = new Node(3);
        boolean ans = isSymmetric(root);
        System.out.println(ans);

    }
}