/**
 * 
 * @author 
 * aakash.verma
 * 
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {

    /*  LeetCode Code
        Line 24 - 46
    */

public:
    int postIndex;
    map<int, int> inorder_map;

    TreeNode* solve(vector<int>& postorder, int start, int end){
        if(start > end)
            return NULL;
        int rootValue = postorder[postIndex];
        int index = inorder_map[rootValue];
        postIndex--;
        TreeNode* root = new TreeNode(rootValue);        
        root->right = solve(postorder, index + 1, end);
        root->left = solve(postorder, start, index - 1);        
        return root;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        postIndex = postorder.size()-1;
        for(int i = 0; i < inorder.size(); i++)
            inorder_map[inorder[i]] = i;
        return solve(postorder, 0, postorder.size() - 1);
    }
};

int main(int argc, char const *argv[])
{
    vector<int> inorder = {};
    vector<int> postorder = {};
    TreeNode* root = buildTree(inorder, postorder);
    /**
     * We can write the code for BFS traversal to check the formed tree.
     * 
     */
}