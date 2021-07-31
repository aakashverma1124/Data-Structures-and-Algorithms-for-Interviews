/*
*   @author
*   Aakash Verma
*
*   Output:
*   True
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

struct Node *root = NULL;

bool findSymmetric(struct Node *root1, struct Node *root2) {
    if(root1 == NULL && root2 == NULL)
        return true;
    if(root1 == NULL || root2 ==NULL)
        return false;
    return (root1->data == root2->data) && 
            findSymmetric(root1->left, root2->right) && 
            findSymmetric(root1->right, root2->left);
}

bool isSymmetric(struct Node *root) {
    return findSymmetric(root, root);
}
    
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(2);
    root->left->left = new Node(3);
    root->left->right = new Node(4);
    root->right->left = new Node(4);
    root->right->right = new Node(3);

    bool ans = isSymmetric(root);
    if(ans)
        cout << "True" << endl;
    else
        cout << "False" << endl;
    
}
