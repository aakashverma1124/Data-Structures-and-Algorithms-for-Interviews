/*
*   @author
*   Aakash Verma
*
*   Output:
*   8
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


class TreeDiameter {

    static Node root;
    TreeDiameter() {
        root = null;
    }

    static int diameter = 0;

    private static int findHeight(Node root) {
        if(root == null) return 0;

        int leftHeight = findHeight(root.left);
        int rightHeight = findHeight(root.right);
        
        int currentDiameter = leftHeight + rightHeight + 1;

        diameter = Math.max(currentDiameter, diameter);
        return Math.max(leftHeight, rightHeight) + 1;
    }

    public static int findDiameter(Node root) {
        findHeight(root);
        return diameter;
    }

    public static void main (String[] args) {
        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.right.left = new Node(4);
        root.right.right = new Node(5);
        root.right.left.left = new Node(6);
        root.right.right.right = new Node(7);
        root.right.right.right.left = new Node(12);
        root.right.right.right.right = new Node(13);
        root.right.left.left.left = new Node(8);
        root.right.left.left.right = new Node(10);
        root.right.left.left.right.left = new Node(11);
        int ans = findDiameter(root);
        System.out.println(ans);
    }
}