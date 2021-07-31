/*
*   @author
*   Aakash Verma
*
*   Output:
*   2
*   7 4 5
*   6 3
*   1 
*   0 8 
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


class BurningTree {

    static Node root;
    BurningTree() {
        root = null;
    }

    private static Queue<Node> queue = new LinkedList<>();

    private static int burningTree(Node root, int targetNode) {
        if(root == null)
            return 0;
        if(root.data == targetNode) {
            System.out.println(root.data);
            if(root.left != null)
                queue.offer(root.left);
            if(root.right != null)
                queue.offer(root.right);
            return 1;
        }

        int left = burningTree(root.left, targetNode);
        if(left == 1) {
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++) {
                Node current = queue.poll();
                System.out.print(current.data + " ");
                if(current.left != null)
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
            if(root.right != null) {
                queue.offer(root.right);
            }
            System.out.println(root.data);
            return 1;
        }

        int right = burningTree(root.right, targetNode);
        if(right == 1) {
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++) {
                Node current = queue.poll();
                System.out.print(current.data + " ");
                if(current.left != null)
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
            if(root.left != null) {
                queue.offer(root.left);
            }
            System.out.println(root.data);
            return 1;
        }
        return 0;
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
        burningTree(root, 2);
        while(!queue.isEmpty()) {
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++) {
                Node current = queue.poll();
                System.out.print(current.data + " ");
                if(current.left != null)
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
            System.out.println();
        }
    }
}