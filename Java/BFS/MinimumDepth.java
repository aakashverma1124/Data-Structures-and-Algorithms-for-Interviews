/*
*   @author
*   Aakash Verma
*
*   Output:
*   3
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


class MinimumTreeDepth {

    static Node root;
    MinimumTreeDepth() {
        root = null;
    }

    public static int findMinimumDepth(Node root) {
        int minimumDepth = 0;
        if(root == null) return minimumDepth;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            minimumDepth++;
            int levelSize = queue.size();
            for(int i = 0; i < levelSize; i++) {
                Node current = queue.poll();
                
                if(current.left == null && current.right == null) {
                    return minimumDepth;
                }

                if(current.left != null) 
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
        }
        return minimumDepth;
    }

    public static void main (String[] args) {
        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        root.right.right.left = new Node(8);
        int ans = findMinimumDepth(root);
        System.out.println(ans);
    }
}