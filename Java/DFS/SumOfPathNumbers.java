/*
*   @author
*   Aakash Verma
*
*   Output:
*   1008
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

    private static int findPathSum(Node root, int pathSum) {
        if(root == null) return 0;

        pathSum = pathSum * 10 + root.data;

        if(root.left == null && root.right == null) {
            return pathSum;
        }

        return findPathSum(root.left, pathSum) + findPathSum(root.right, pathSum);
    }

    public static int findSumPathNumbers(Node root) {
        return findPathSum(root, 0);
    }

    public static void main (String[] args) {
        root = new Node(3);
        root.left = new Node(7);
        root.right = new Node(1);
        root.left.left = new Node(9);
        root.right.left = new Node(4);
        root.right.right = new Node(5);
        int ans = findSumPathNumbers(root);
        System.out.println(ans);
    }
}