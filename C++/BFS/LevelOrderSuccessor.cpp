/*
*   @author
*   Aakash Verma
*
*   Output:
*   6
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

Node* levelOrderSuccessor(struct Node *root, int key) {
    if(root == NULL)
        return NULL;
    queue<Node *> queue;
    queue.push(root);
    while(!queue.empty()) {
        Node *current = queue.front();
        queue.pop();

        if(current->left != NULL)
            queue.push(current->left);
        if(current->right != NULL)
            queue.push(current->right);
        
        if(current->data == key) {
            break;
        }
    }
    return queue.front();
}
    
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    root->right->right->left = new Node(8);
    Node *ans = levelOrderSuccessor(root, 4);
    cout << ans->data << endl;
}
