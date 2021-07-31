/*
*   @author
*   Aakash Verma
*
*   Output:
*   3 6 3 1 8 10 5 
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


class MergeTwoTrees {

    static Node root1, root2;
    MergeTwoTrees() {
        root1 = null;
        root2 = null;
    }

    public static void traverse(Node root) {
        if(root == null) {
            return;
        }
        System.out.print(root.data + " ");
        traverse(root.left);
        traverse(root.right);
    }

    public static Node merge(Node root1, Node root2) {
        if(root1 == null)
            return root2;
        if(root2 == null)
            return root1;

        root1.data += root2.data;

        root1.left = merge(root1.left, root2.left);
        root1.right = merge(root1.right, root2.right);
        return root1;
    }

    public static void main (String[] args) {
        root1 = new Node(1);
        root1.left = new Node(2);
        root1.right = new Node(3);
        root1.right.left = new Node(4);
        root1.right.right = new Node(5);

        root2 = new Node(2);
        root2.left = new Node(4);
        root2.right = new Node(5);
        root2.left.left = new Node(3);
        root2.left.right = new Node(1);
        root2.right.left = new Node(6);

        Node root = merge(root1, root2);
        traverse(root);

    }
}