/*
*   @author
*   Aakash Verma
*
*   Output:
*   12 1 5 3
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


class RightView {

    static Node root;
    RightView() {
        root = null;
    }

    public static List<Integer> rightView(Node root) {
        List<Integer> result = new ArrayList<>();
        if(root == null) return result;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int levelSize = queue.size();
            for(int i = 0; i < levelSize; i++) {
                Node current = queue.poll();
                
                if(i == levelSize - 1) {
                    result.add(current.data);
                }

                if(current.left != null) 
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
        }
        return result;
    }

    public static void main (String[] args) {
        root = new Node(12);
        root.left = new Node(7);
        root.right = new Node(1);
        root.left.left = new Node(9);
        root.right.left = new Node(10);
        root.right.right = new Node(5);
        root.left.left.left = new Node(3);
        List<Integer> ans = rightView(root);
        for(int node : ans) {
            System.out.print(node + " ");
        }
        System.out.println();
    }
}