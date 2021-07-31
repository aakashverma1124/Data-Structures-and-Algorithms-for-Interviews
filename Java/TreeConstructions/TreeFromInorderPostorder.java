/**
 * 
 * @author 
 * aakash.verma
 * 
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    /*  LeetCode Code
        Line 25 - 44
    */
    
    int postIndex;
    HashMap<Integer, Integer> inorderMap = new HashMap<>();

    private TreeNode solve(int[] postorder, int left, int right) {
        if(left > right) return null;
        int rootValue = postorder[postIndex--];
        int index = inorderMap.get(rootValue);
        TreeNode root = new TreeNode(rootValue);
        root.right = solve(postorder, index + 1, right);
        root.left = solve(postorder, left, index - 1);
        return root;
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        for(int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }
        postIndex = postorder.length - 1;
        return solve(postorder, 0, postorder.length - 1);
    }



    public static void main(String[] args) {
        int inorder[] = new int[]{};
        int postorder[] = new int[]{};
        TreeNode root = Solution.buildTree(inorder, postorder);
        /**
         * We can write the code for BFS traversal to check the formed tree.
         */
    }
}