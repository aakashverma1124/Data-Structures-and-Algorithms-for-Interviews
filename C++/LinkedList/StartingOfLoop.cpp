/*
	@author
   	Aakash Verma
	
 	Start of a loop in a linked list.

 	Output:
 	5

*/


#include <iostream>
using namespace std;

/* creating a node structure in C/C++ */
struct Node {
   int data;
   struct Node *next;
};

/* defining head as null as there is no node in the list initially. */
struct Node* head = NULL;

void push(int data) {
	Node *temp;
	temp = head;

	/* creating a node and assigning data to it and make its next as null */
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
	new_node->data = data;
   	new_node->next = NULL;

   	/* check if it's empty make new_node as head */
	if(head == NULL) {
   		head = new_node;
	}
	/* otherwise move upto the last and then connect last node with the new_node */
	else { 
		while(temp->next != NULL) {
			temp = temp->next;
		}
   		temp->next = new_node;
	}
}

/* finding loop in a linked list. */
void startingOfLoop() {
	Node *slow, *fast;
	slow = fast = head;

	bool isLoopFound = false;

	if(head == NULL) {
		cout << "The list doesn't exist." << endl;
	}

	while(fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
		if(slow == fast) {
			isLoopFound = true;
			break;
		}
	}

	if(isLoopFound) {
		slow = head;
		while(slow != fast) {
			slow = slow->next;
			fast = fast->next;
		}
	}

	cout << slow->data << endl;
}

int main() {

	push(3);
	push(4);
	push(5);
	push(6);
	push(7);
	head->next->next->next->next->next = head->next->next;
	startingOfLoop();
	return 0;

}