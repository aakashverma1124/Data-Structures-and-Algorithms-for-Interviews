/*
	@author
   	Aakash Verma
	
 	Given a Linked List, find the nth node from the end of a linked list.

 	Output:

	Original List is: 2 3 4 5 6 
	Middle of List is: 4
	Original List is: 2 3 4 5 6 7 
	Middle of List is: 5

	Note: In case of even number of nodes, we are printing the ((n/2)+1)th node. 
	If you want to print (n/2)th node you can customize your code as per your requirement.

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

/* Utility function to find the nth Node from the end. */
void findMiddle() {
	Node *slow, *fast;
	slow = head;
	fast = head;

	if(head == NULL) {
		cout << "The list doesn't exist." << endl;
		return;
	}

	/* 
		move one pointer one time & other pointer two times
		which will result fast pointer at the end and slow pointer in the middle of a list
	 
	*/
	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
	}

	/* finally printing data of middle of list */
	cout << slow->data << endl;

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
	cout<<"Middle of List is: ";
	findMiddle();

	push(7);

	cout<<"Original List is: ";
	printList();
	cout<<"Middle of List is: ";
	findMiddle();

	return 0;

}