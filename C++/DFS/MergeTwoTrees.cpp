/*
*   @author
*   Aakash Verma
*
*   Output:
*   3 6 3 1 8 10 5
*
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

struct Node *root1 = NULL;
struct Node *root2 = NULL;

void traverse(struct Node *root) {
    if(root == NULL) {
        return;
    }
    cout << root->data << " ";
    traverse(root->left);
    traverse(root->right);
}

struct Node* merge(struct Node *root1, struct Node *root2) {
    if(root1 == NULL) return root2;
    if(root2 == NULL) return root1;

    root1->data += root2->data;
    root1->left = merge(root1->left, root2->left);
    root1->right = merge(root1->right, root2->right);
    
    return root1;
}
    
int main(int argc, char const *argv[]) {
    root1 = new Node(1);
    root1->left = new Node(2);
    root1->right = new Node(3);
    root1->right->left = new Node(4);
    root1->right->right = new Node(5);


    root2 = new Node(2);
    root2->left = new Node(4);
    root2->right = new Node(5);
    root2->left->left = new Node(3);
    root2->left->right = new Node(1);
    root2->right->left = new Node(6);

    struct Node *root = merge(root1, root2);
    traverse(root);
    
}
