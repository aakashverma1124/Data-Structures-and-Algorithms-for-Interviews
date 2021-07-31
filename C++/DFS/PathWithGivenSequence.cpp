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

bool findSequence(struct Node *root, vector<int> sequence, int index) {
    if(root == NULL) return false;

    if(index >= sequence.size() || root->data != sequence[index]) {
        return false;
    }

    if(root->left == NULL && root->right == NULL && index == sequence.size() - 1) {
        return true;
    }

    return findSequence(root->left, sequence, index + 1) || findSequence(root->right, sequence, index + 1);

}

bool hasPath(struct Node *root, vector<int> sequence) {
    if(root == NULL) return sequence.size() == 0;

    return findSequence(root, sequence, 0);
}
    
int main(int argc, char const *argv[]) {
    root = new Node(3);
    root->left = new Node(7);
    root->right = new Node(1);
    root->left->left = new Node(9);
    root->right->left = new Node(2);
    root->right->right = new Node(5);
    bool ans = hasPath(root, vector<int>{3, 1, 2});
    if(ans)
        cout << "true";
    else
        cout << "false";
    cout << endl;
}
