/**
 * @author
 * aakash.verma
 *
 */

#include <bits/stdc++.h> 
using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> postorder;
        stack<TreeNode*> stack1;
        stack<TreeNode*> stack2;
        if(root == NULL) return postorder;
        stack1.push(root);
        while(!stack1.empty()) {
            TreeNode *current = stack1.top();
            stack1.pop();
            stack2.push(current);
            if(current->left != NULL) stack1.push(current->left);
            if(current->right != NULL) stack1.push(current->right);
        }
        while(stack2.size() != 0) {
            postorder.push_back(stack2.top()->val);
            stack2.pop();
        }
        return postorder;
    }
};

int main() {
    .
    .
    .
}