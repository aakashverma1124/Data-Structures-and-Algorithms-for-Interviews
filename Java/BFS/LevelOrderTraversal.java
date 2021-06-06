/*
*   @author
*   Aakash Verma
*
*   Output:
*   [1]
*   [2, 3]
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

    public static List<List<Integer>> traverse(Node root) {
        List<List<Integer>> bfs = new ArrayList<>();
        if(root == null) return bfs;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>();
            for(int i = 0; i < levelSize; i++) {
                Node current = queue.poll();
                currentLevel.add(current.data);
                if(current.left != null) 
                    queue.offer(current.left);
                if(current.right != null)
                    queue.offer(current.right);
            }
            bfs.add(currentLevel);
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
        List<List<Integer>> ans = traverse(root);
        for(List<Integer> level : ans) {
            System.out.println(level.toString());
        }
    }
}