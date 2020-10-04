/*
*
*   @author
*   Aakash Verma
*
*   Output:
*   Pre Order Traversal is: 1 2 4 5 3 6 7 
*   In Order Traversal is: 4 2 5 1 6 3 7 
*   Post Order Traversal is: 4 5 2 6 7 3 1 
*/


/*  
    Creating a structure for the node.
    Initializing the node's data upon calling its constructor.
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




/* Creating a root node for the Tree and setting it as null */
struct Node *root = NULL;

/* Pre Order Traversal */
void preOrder(struct Node *root) {
    if(root == NULL) {
        return;
    }
    cout << root->data << " ";
    preOrder(root->left);
    preOrder(root->right);
}


/* In Order Traversal */
void inOrder(struct Node *root) {
    if(root == NULL) {
        return;
    }
    inOrder(root->left);
    cout << root->data << " ";
    inOrder(root->right);
}

/* Post Order Traversal */
void postOrder(struct Node *root) {
    if(root == NULL) {
        return;
    }
    postOrder(root->left);
    postOrder(root->right);
    cout << root->data << " ";
}
    
    /* main method */
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    cout << "Pre Order Traversal is: ";
    preOrder(root);
    cout << endl;
    cout << "In Order Traversal is: ";
    inOrder(root);
    cout << endl;
    cout << "Post Order Traversal is: ";
    postOrder(root);
    cout << endl;
}
