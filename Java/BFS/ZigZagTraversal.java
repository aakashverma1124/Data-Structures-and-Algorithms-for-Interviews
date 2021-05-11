/*
*   @author
*   Aakash Verma
*
*   Output:
*   [1]
*   [3, 2]
*   [4, 5, 6, 7]
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


class LevelOrderTraversal {

    static Node root;
    LevelOrderTraversal() {
        root = null;
    }

    public static List<List<Integer>> zigZagTraversal(Node root) {
        List<List<Integer>> bfs = new ArrayList<>();
        boolean leftToRight = true;
        if(root == null) return bfs;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new LinkedList<>();
            for(int i = 0; i < levelSize; i++) {
                Node current = queue.poll();
                if(leftToRight)
                    currentLevel.add(current.data);
                else
                    currentLevel.add(0, current.data);

                if(current.left != null) 
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
            bfs.add(currentLevel);
            leftToRight = !leftToRight;
        }
        return bfs;
    }

    public static void main (String[] args) {
        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        List<List<Integer>> ans = zigZagTraversal(root);
        for(List<Integer> level : ans) {
            System.out.println(level.toString());
        }
    }
}