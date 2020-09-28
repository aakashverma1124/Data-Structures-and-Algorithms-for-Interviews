/*	
	@author
	Aakash.Verma

	In this code, we'll implement the Stack using Linked List. 
	In the previous code, there was a problem that the stack using array is of fixed size which means
	we can't increase the size of the stack as per the requirement. 
	But in case of linked list, we'll create nodes dynamically as per our need and the size of stack will
	grow as per the requirement.

	Output:

	The element is pushed and top points to => 10
	The element is pushed and top points to => 20
	The element is pushed and top points to => 30
	Deleted Element: 30
	Top element is: 20

*/


#include <bits/stdc++.h> 
using namespace std;

/* creating a node structure in C/C++ */
struct Node {
   int data;
   struct Node *next;
};

/* defining root as null as there is no node in the stack initially. */
struct Node* root = NULL;

/* if root doesn't point to anything, then stack is obviously empty and it will return true. */
bool isEmpty() {
	if(root == NULL) {
		return 1;
	}
	return 0;
}

void push(int data) {

	/* creating a node and assigning data to it and make its next as null */
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
	new_node->data = data;
   	new_node->next = NULL;

	/* 	IMPORTANT
		Let's suppose: initially we have 10 in the stack and root points to 10 only.
		root => 10

		Now, we'll push one more node to the stack, so it should be like this:
		10 -> 20 (and acc. to us, root still should point to 10, because it's a root node)
		But Stack is a LIFO data structure and the element which is added at last should be
		deleted first.

		We can do it so by iterating everytime till the last node and delete it in pop() function.
		But this will be time taking process everytime.
		For example: 
		10 -> 20 -> 30 -> 40 -> 50
		So, 50 is the last node and should be deleted it when pop() will be called.
		Same problem will be to find the top element by using peek()
		We'll have to iterate everytime.

		So, we can do some changes while pushing element in the stack.
		What we are doing is: if 10 is already there in the linked list and I want to add 20.
		So my list should be like this: 10 <- 20 and root will point to 20 
		instead of 10 -> 20 and root points to 10

		the idea is if initially root was poining to 10.
		then I store root into tempNode
		I make node as root
		and I add node.next to tempNode.
		which turns my list as 20 -> 10

	*/
	new_node->next = root;
	root = new_node; 
	cout << "The element is pushed and top points to => "<< root->data <<  endl;

}

/* 
	If isEmpty() returns true, we can't delete element.
	Otherwise we return root.data because everytime root points to last added element, 
	so we directly return root.data and we make root = root.next;
*/
int pop() {
	int deletedElement = INT_MIN;
	if(isEmpty()) {
		cout << "Stack Underflow" << endl;
	}
	else {
		deletedElement = root->data;
		root = root->next;
	}
	return deletedElement;
}

/* simply returns the root.data */
int peek() {
	int topElement = INT_MIN;
	if(isEmpty()) {
		cout << "Stack Underflow" << endl;	
	}
	else {
		topElement = root->data;
	}
	return topElement;
}

int main(int argc, char const *argv[]) {
	push(10);
	push(20);
	push(30);
	int deletedElement = pop();
	cout << "Deleted Element: " << deletedElement << endl;
	cout << "Top element is: " << peek() << endl;
}