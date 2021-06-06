/*
*   @author
*   Aakash Verma
*
*   Output:
*   6
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


class LevelOrderSuccessor {

    static Node root;
    LevelOrderSuccessor() {
        root = null;
    }

    public static Node levelOrderSuccessor(Node root, int key) {
        if(root == null) return null;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            Node current = queue.poll();
            if(current.left != null) 
                queue.offer(current.left);
            if(current.right != null)
                queue.offer(current.right);

            if(current.data == key) {
                break;
            }
        }
        return queue.poll();
    }

    public static void main (String[] args) {
        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        root.right.right.left = new Node(8);
        Node ans = levelOrderSuccessor(root, 4);
        System.out.println(ans.data);
    }
}