/*
*   @author
*   Aakash Verma
*
*   Output:
*   5
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


class LowestCommonAncestor {

    static Node root;
    LowestCommonAncestor() {
        root = null;
    }

    public static Node lowestCommonAncestor(Node root, Node p, Node q) {
        
        if(root == null) 
            return null;

        if(root.data == p.data || root.data == q.data) 
            return root;

        Node left = lowestCommonAncestor(root.left, p, q);
        Node right = lowestCommonAncestor(root.right, p, q);

        if(left != null && right != null) 
            return root;

        return left != null ? left : right;
    }

    public static void main (String[] args) {
        root = new Node(3);
        root.left = new Node(5);
        root.right = new Node(1);
        root.left.left = new Node(6);
        root.left.right = new Node(2);
        root.right.left = new Node(0);
        root.right.right = new Node(8);
        root.left.right.left = new Node(7);
        root.left.right.right = new Node(4);

        Node p = root.left;
        Node q = root.left.right.right;

        Node lca = lowestCommonAncestor(root, p, q);
        System.out.println(lca.data);
    }
}
