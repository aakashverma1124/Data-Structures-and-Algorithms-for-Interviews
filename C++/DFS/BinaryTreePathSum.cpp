/*
*   @author
*   Aakash Verma
*
*   Output:
*   true
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

bool hasPath(struct Node *root, int sum) {
    if(root == NULL) return false;
    
    if(root->data == sum && root->left == NULL && root->right == NULL) {
        return true;
    }

    return hasPath(root->left, sum - root->data) || hasPath(root->right, sum - root->data);

}
    
int main(int argc, char const *argv[]) {
    root = new Node(12);
    root->left = new Node(7);
    root->right = new Node(1);
    root->left->left = new Node(9);
    root->right->left = new Node(10);
    root->right->right = new Node(5);
    root->left->left->left = new Node(3);
    bool ans = hasPath(root, 23);
    if(ans)
        cout << "true";
    else
        cout << "false";
    cout << endl;
}
