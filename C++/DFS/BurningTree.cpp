/*
*   @author
*   Aakash Verma
*
*   Output:
*   2
*   7 4 5
*   6 3
*   1 
*   0 8 
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

queue<Node*> que;

int burningTree(struct Node *root, int targetNode) {
    
    if(root == NULL) 
        return 0;

    if(root->data == targetNode) {
        cout << targetNode << endl;
        if(root->left != NULL)
            que.push(root->left);
        if(root->right != NULL)
            que.push(root->right);
        return 1;
    } 

    int left = burningTree(root->left, targetNode);
    if(left == 1) {
        int queueSize = que.size();
        for(int i = 0; i < queueSize; i++) {
            struct Node *current = que.front();
            que.pop();
            cout << current->data << " ";
            if(current-> left != NULL)
                que.push(current->left);
            if(current->right != NULL)
                que.push(current->right);
        }
        if(root->right != NULL)
            que.push(root->right);
        cout << root->data << endl;
        return 1;
    }
     
    int right = burningTree(root->right, targetNode);
    if(right == 1) {
        int queueSize = que.size();
        for(int i = 0; i < queueSize; i++) {
            struct Node *current = que.front();
            que.pop();
            cout << current->data << " ";
            if(current-> left != NULL)
                que.push(current->left);
            if(current->right != NULL)
                que.push(current->right);
        }
        if(root->left != NULL)
            que.push(root->left);
        cout << root->data << endl;
        return 1;
    }   
    return 0;
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
    
    burningTree(root, 2);
    while(!que.empty()) {
        int queueSize = que.size();
        for(int i = 0; i < queueSize; i++) {
            struct Node *current = que.front();
            que.pop();
            cout << current->data << " ";
            if(current-> left != NULL)
                que.push(current->left);
            if(current->right != NULL)
                que.push(current->right);
        }
        cout << endl;
    }
    
}
