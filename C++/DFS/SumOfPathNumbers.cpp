/*
*   @author
*   Aakash Verma
*
*   Output:
*   1008
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

int findPathSum(struct Node *root, int pathSum) {
    if(root == NULL) return 0;

    pathSum = 10 * pathSum + root->data;
    
    if(root->left == NULL && root->right == NULL) {
        return pathSum;
    }

    return findPathSum(root->left, pathSum) + findPathSum(root->right, pathSum);
}

int findSumPathNumbers(struct Node *root) {
    return findPathSum(root, 0);
}
    
int main(int argc, char const *argv[]) {
    root = new Node(3);
    root->left = new Node(7);
    root->right = new Node(1);
    root->left->left = new Node(9);
    root->right->left = new Node(4);
    root->right->right = new Node(5);
    int ans = findSumPathNumbers(root);
    cout << ans << endl;
}
