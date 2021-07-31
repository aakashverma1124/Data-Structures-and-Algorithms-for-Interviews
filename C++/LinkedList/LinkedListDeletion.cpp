/*
	@author
   	Aakash Verma
	
 	Deletion in Linked List

 	Output:

	Original List is: 2 3 4 5 6 
	After Deletion: 2 3 4 6 


	Compile using:  g++ filename.cpp
	Run using: ./a.out filename.cpp

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

void deletNode(int data) {
	Node *temp, *prev;
	temp = head;
	prev = NULL;

	if(temp == NULL) {
		cout << "The list is empty, the node can't be deleted." << endl;
		return;
	}

	if(temp->data == data) {
		head = temp->next;
		return;
	}

	while(temp != NULL && temp->data != data) {
		prev = temp;
		temp = temp->next;
	}

	if(temp == NULL) {
		cout << "The key is not present in the list." << endl;
		return;
	}
	prev->next = temp->next;
}

/* for printing a ist */
void printList() {

   	struct Node* ptr;
   	ptr = head;
   	
   	while (ptr != NULL) {
      	cout<< ptr->data <<" ";  // use printf() for C
      	ptr = ptr->next;
   	}
   	cout<<endl;
}

int main() {

	push(2);
	push(3);
	push(4);
	push(5);
	push(6);
	cout<<"Original List is: ";
	printList();
	deletNode(5);
	cout<<"After Deletion: ";
	printList();

	return 0;

}