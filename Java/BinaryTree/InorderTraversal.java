/**
 * @author
 * aakash.verma
 *
 */

import java.util.*;

class InorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorder = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        if(root == null) {
            return inorder;
        }
        
        TreeNode curr = root;
        while(curr != null || stack.size() != 0) {
            while(curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            inorder.add(curr.val);
            curr = curr.right;
        }
        return inorder;
    }

    public static void main(String[] args) {
        .
        .
        .
    }
}