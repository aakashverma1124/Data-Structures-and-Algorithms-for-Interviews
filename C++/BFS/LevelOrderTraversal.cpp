/*
*   @author
*   Aakash Verma
*
*   Output:
*   1
*   2 3
*   4 5 6 7
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

vector<vector<int>> traverse(struct Node *root) {
    vector<vector<int>> bfs;
    if(root == NULL)
        return bfs;
    queue<Node *> queue;
    queue.push(root);
    while(!queue.empty()) {
        int levelSize = queue.size();
        vector<int> currentLevel;
        for(int i = 0; i < levelSize; i++) {
            Node *current = queue.front();
            queue.pop();
            currentLevel.push_back(current->data);
            if(current->left != NULL)
                queue.push(current->left);
            if(current->right != NULL)
                queue.push(current->right);
        }
        bfs.push_back(currentLevel);
    }
    return bfs;
}
    
int main(int argc, char const *argv[]) {
    root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    vector<vector<int>> ans = traverse(root);
    for(auto level : ans) {
        for(auto num : level) {
            cout << num << " ";
        }
        cout << endl;
    }
}
