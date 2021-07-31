/*
*   @author
*   Aakash Verma
*
*   Output:
*   42
*/

#include <bits/stdc++.h> 
using namespace std;

struct Node {
    int data;
    struct Node *left, *right;
    Node(int data) { 
        this->data = data; 
        left = right = NULL; 
    }
};

struct Node *root = NULL;

int maxSum = numeric_limits<int>::min();

int findMaxSum(struct Node *root) {
    if(root == NULL) return 0;

    int leftSum = findMaxSum(root->left);
    int rightSum = findMaxSum(root->right);

    leftSum = max(leftSum, 0);
    rightSum = max(rightSum, 0);
    
    int currentSum = leftSum + rightSum + root->data;

    maxSum = max(currentSum, maxSum);
    return max(leftSum, rightSum) + root->data;

}

int findMaximumPathSum(struct Node *root) {
    findMaxSum(root);
    return maxSum;
}
    
int main(int argc, char const *argv[]) {
    root = new Node(10);
    root->left = new Node(2);
    root->right = new Node(10);
    root->left->left = new Node(20);
    root->left->right = new Node(1);
    root->right->left = new Node(-25);
    root->right->left->left = new Node(3);
    root->right->left->right = new Node(4);
    int ans = findMaximumPathSum(root);
    cout << ans << endl;
}
