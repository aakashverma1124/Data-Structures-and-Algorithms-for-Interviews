/*
*   @author
*   Aakash Verma
*
*   Output:
*   3
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

int findMinimumDepth(struct Node *root) {
    int minimumDepth = 0;
    bool leftToRight = true;
    if(root == NULL)
        return minimumDepth;
    queue<Node *> queue;
    queue.push(root);
    while(!queue.empty()) {
        minimumDepth++;
        int levelSize = queue.size();
        for(int i = 0; i < levelSize; i++) {
            Node *current = queue.front();
            queue.pop();
            
            if(current->left == NULL && current->right == NULL) {
                return minimumDepth;
            }

            if(current->left != NULL)
                queue.push(current->left);
            if(current->right != NULL)
                queue.push(current->right);
        }
    }
    return minimumDepth;
}
    
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    root->right->right->left = new Node(8);
    int ans = findMinimumDepth(root);
    cout << ans << endl;
}
