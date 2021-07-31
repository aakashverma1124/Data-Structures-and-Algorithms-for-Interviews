/*
*
*   @author
*   Aakash Verma
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

/* main method */
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
}
