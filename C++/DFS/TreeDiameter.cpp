/*
*   @author
*   Aakash Verma
*
*   Output:
*   8
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

int diameter = 0;

int findHeight(struct Node *root) {
    if(root == NULL) return 0;

    int leftHeight = findHeight(root->left);
    int rightHeight = findHeight(root->right);
    
    int currentDiameter = leftHeight + rightHeight + 1;

    diameter = max(currentDiameter, diameter);
    return max(leftHeight, rightHeight) + 1;

}

int findDiameter(struct Node *root) {
    findHeight(root);
    return diameter;
}
    
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->right->left = new Node(4);
    root->right->right = new Node(5);
    root->right->left->left = new Node(6);
    root->right->right->right = new Node(7);
    root->right->right->right->left = new Node(12);
    root->right->right->right->right = new Node(13);
    root->right->left->left->left = new Node(8);
    root->right->left->left->right = new Node(10);
    root->right->left->left->right->left = new Node(11);
    int ans = findDiameter(root);
    cout << ans << endl;
}
