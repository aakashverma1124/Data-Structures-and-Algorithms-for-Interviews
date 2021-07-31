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


class BinaryTreePathSum {

    static Node root;
    BinaryTreePathSum() {
        root = null;
    }

    public static boolean hasPath(Node root, int sum) {
        if(root == null) return false;

        if(root.data == sum && root.left == null && root.right == null)
            return true;

        return hasPath(root.left, sum - root.data) || hasPath(root.right, sum - root.data);
    }

    public static void main (String[] args) {
        root = new Node(12);
        root.left = new Node(7);
        root.right = new Node(1);
        root.left.left = new Node(9);
        root.right.left = new Node(10);
        root.right.right = new Node(5);
        root.left.left.left = new Node(3);
        boolean ans = hasPath(root, 23);
        System.out.println(ans);
    }
}