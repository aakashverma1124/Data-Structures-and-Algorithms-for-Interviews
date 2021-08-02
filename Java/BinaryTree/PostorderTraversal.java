/**
 * @author
 * aakash.verma
 *
 */

import java.util.*;

class PostorderTraversal {

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> postorder = new ArrayList<>();
        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        if(root == null) return postorder;
        stack1.push(root);
        while(stack1.size() != 0) {
            TreeNode current = stack1.pop();
            stack2.push(current);
            if(current.left != null) stack1.push(current.left);
            if(current.right != null) stack1.push(current.right);
        }
        while(stack2.size() != 0) {
            postorder.add(stack2.pop().val);
        }
        return postorder;
    }

    public static void main(String[] args) {
        .
        .
        .
    }
}