/*
*   @author
*   Aakash Verma
*
*   Output:
*   42
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


class PathWithMaximumSum {

    static Node root;
    PathWithMaximumSum() {
        root = null;
    }

    private static int maxSum;

    private static int findMaxSum(Node root) {
        if(root == null) return 0;

        int leftSum = findMaxSum(root.left);
        int rightSum = findMaxSum(root.right);

        leftSum = Math.max(leftSum, 0);
        rightSum = Math.max(rightSum, 0);
        
        int currentSum = leftSum + rightSum + root.data;

        maxSum = Math.max(currentSum, maxSum);
        return Math.max(leftSum, rightSum) + root.data;
    }

    public static int findMaximumPathSum(Node root) {
        maxSum = Integer.MIN_VALUE;
        findMaxSum(root);
        return maxSum;
    }

    public static void main (String[] args) {
        root = new Node(10);
        root.left = new Node(2);
        root.right = new Node(10);
        root.left.left = new Node(20);
        root.left.right = new Node(1);
        root.right.left = new Node(-25);
        root.right.left.left = new Node(3);
        root.right.left.right = new Node(4);
        int ans = findMaximumPathSum(root);
        System.out.println(ans);
    }
}