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


class PathWithGivenSequence {

    static Node root;
    PathWithGivenSequence() {
        root = null;
    }

    private static boolean findSequence(Node root, int[] sequence, int index) {
        if(root == null) return false;

        if(index >= sequence.length || root.data != sequence[index]) {
            return false;
        }

        if(root.left == null && root.right == null && index == sequence.length - 1) {
            return true;
        }

        return findSequence(root.left, sequence, index + 1) || findSequence(root.right, sequence, index + 1);
    }

    public static boolean hasPath(Node root, int[] sequence) {
        if(root == null) return sequence.length == 0;

        return findSequence(root, sequence, 0);
    }

    public static void main (String[] args) {
        root = new Node(3);
        root.left = new Node(7);
        root.right = new Node(1);
        root.left.left = new Node(9);
        root.right.left = new Node(2);
        root.right.right = new Node(5);
        boolean ans = hasPath(root, new int[] {3, 1, 2});
        System.out.println(ans);
    }
}