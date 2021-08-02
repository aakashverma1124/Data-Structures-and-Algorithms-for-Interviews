/**
 * @author
 * aakash.verma
 *
 */

#include <bits/stdc++.h> 
using namespace std;

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorder;
        stack<TreeNode*> stack;
        if(root == NULL) {
            return inorder;
        }
        
        TreeNode *curr = root;
        while(curr != NULL || stack.size() != 0) {
            while(curr != NULL) {
                stack.push(curr);
                curr = curr->left;
            }
            curr = stack.top();
            stack.pop();
            inorder.push_back(curr->val);
            curr = curr->right;
        }
        return inorder;
    }
};

int main() {
    .
    .
    .
}