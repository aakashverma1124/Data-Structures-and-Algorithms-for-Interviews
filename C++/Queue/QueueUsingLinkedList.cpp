/*	
	@author
	Aakash.Verma

	Queue is a FIFO/LILO data structures:
	FIFO stands for First In First Out 
	
	We can't access any element except front. Front is that element which has been inserted at first
	and will be retrieved first. Rear is that element which is inserted at last and will be deleted 
	at last.

	I am assuming that you are here after going through the theory of Queue and looking for implementation.

	Output: 	
	Enqueue Operation Done, rear is at 11
	Enqueue Operation Done, rear is at 12
	Enqueue Operation Done, rear is at 13
	Deleted Element is: 11
	Front element is: 12

	Compile using:  g++ filename.cpp
	Run using: ./a.out filename.cpp
*/


#include <bits/stdc++.h> 
using namespace std; 

struct Node { 
	int data; 
	struct Node* next; 
}; 

struct Node *front = NULL;
struct Node *rear = NULL;

void enqueue(int item) { 
	struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
	new_node->data = item;
   	new_node->next = NULL;
	
	if (rear == NULL) { 
		front = rear = new_node; 
		cout << "Enqueue Operation Done, rear is at " << rear->data << endl;
		return; 
	} 

	rear->next = new_node; 
	rear = new_node; 
	cout << "Enqueue Operation Done, rear is at " << rear->data << endl;
} 

int dequeue() { 
	if (front == NULL) 
		return -1; 
	
	struct Node* temp = front; 
	front = front->next; 

	if (front == NULL) 
		rear = NULL;

	return temp->data;
}  

int peek() {

	if (front == NULL) 
		return -1; 

	return front->data;
}

int main() { 

	enqueue(11);
	enqueue(12);
	enqueue(13); 
	int del = dequeue();
	cout << "Deleted Element is: " << del << endl;
	cout << "Front element is: " << peek() << endl;
	return 0; 
} 