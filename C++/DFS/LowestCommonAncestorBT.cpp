/*
*   @author
*   Aakash Verma
*
*   Output:
*   5
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

struct Node* lowestCommonAncestor(struct Node *root, struct Node *p, struct Node *q) {
    
    if(root == NULL) 
        return NULL;

    if(root->data == p->data || root->data == q->data) 
        return root;

    struct Node *left = lowestCommonAncestor(root->left, p, q);
    struct Node *right = lowestCommonAncestor(root->right, p, q);

    if(left != NULL && right != NULL) 
        return root;

    return left != NULL ? left : right;

}
    
int main(int argc, char const *argv[]) {
    root = new Node(3);
    root->left = new Node(5);
    root->right = new Node(1);
    root->left->left = new Node(6);
    root->left->right = new Node(2);
    root->right->left = new Node(0);
    root->right->right = new Node(8);
    root->left->right->left = new Node(7);
    root->left->right->right = new Node(4);
    
    struct Node *p = root->left;
    struct Node *q = root->left->right->right;
    
    struct Node *lca = lowestCommonAncestor(root, p, q);
    cout << lca->data << endl;
    
}
