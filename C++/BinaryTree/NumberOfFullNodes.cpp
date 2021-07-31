/*
*
*   @author
*   Aakash Verma
*   
*   Problem: Given a Binary Tree, count the total number of full nodes present in BT.
*   
*   Output: 
*   Traversal is: 1 2 4 5 3 6 7 
*   Number Of Full Nodes: 3
*
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
    if(root == NULL)
        return;
    cout << root->data << " ";
    preOrder(root->left);
    preOrder(root->right);
}


/* Counting number Of Full Nodes */
int numFullNodes(struct Node *root) {
    if(root == NULL)
        return 0;
    if(root->left == NULL && root->right == NULL)
        return 0;
    return numFullNodes(root->left) + numFullNodes(root->right) + (((root->left != NULL) && (root->right != NULL)) ? 1 : 0);
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
    cout << "Number Of Full Nodes: " << numFullNodes(root);
}
