/*
	@author
   	Aakash Verma
	
 	Insertions in Linked List

 	Output:

	After Inserting at Beginning: 1 
	After Inserting at Beginning: 7 1 
	After Inserting at End: 7 1 14 
	After Inserting after node 7: 7 15 1 14 
	After Inserting after node 1: 7 15 1 20 14 


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

/* inserting at the beginning */
void insertAtBeginning(int data) {

	/* this line creates a memory block of type node in the memory */
   	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

   	/* assigning data to new node*/
   	new_node->data = data;
   	new_node->next = head;
   	head = new_node;
}

void insertAfter(int nodeAfter, int data) {
	struct Node* temp;
	temp = head;

	if(head == NULL) {
		cout << "The node can't be inserted in this case as the list doesn't exist." << endl;
	}
	else {
		while(temp->data != nodeAfter) {
			temp = temp->next;
		}
		if(temp == NULL) {
			cout << "The node can't be inserted." << endl;
			return;
		}
		struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
		new_node->data = data;
		new_node->next = temp->next;
		temp->next = new_node;
	}
}

void insertAtEnd(int data) {
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

   insertAtBeginning(1);
   cout<<"After Inserting at Beginning: ";
   printList();

   insertAtBeginning(7);
   cout<<"After Inserting at Beginning: ";
   printList();

   insertAtEnd(14);
   cout<<"After Inserting at End: ";
   printList();

   insertAfter(7, 15);
   cout<<"After Inserting after node 7: ";
   printList();

   insertAfter(1, 20);
   cout<<"After Inserting after node 1: ";
   printList();
   return 0;

}