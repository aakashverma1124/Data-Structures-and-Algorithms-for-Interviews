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

	Enqueue Operation Done, rear is at  11
	Enqueue Operation Done, rear is at  12
	Enqueue Operation Done, rear is at  13
	Deleted Element is:  11
	Front element is:  12

	Compile using:  g++ filename.cpp
	Run using: ./a.out filename.cpp 
*/


#include <iostream>
using namespace std;

  
const int SIZE = 10; 
int front = -1;
int rear = -1;
int queue[SIZE];

/* Checking if the Queue is full */
bool isFull() {
	if (front == 0 && rear == SIZE - 1)
	  	return true;
	if (front == rear + 1)
	  	return true;
	return false;
}

/* Check if the Queue is empty */
bool isEmpty() {
	if (front == -1)
	  	return true;
	else
	  	return false;
}

// Adding an element
void enQueue(int element) {
	if (isFull()) {
	  	cout << "Queue is full" << endl;
	} 
	else {
	  	if (front == -1)
	    	front = 0;
	  	rear = (rear + 1) % SIZE;
	  	queue[rear] = element;
	  	cout << "Enqueue Operation Done, rear is at " << element << endl;
	}
}

/* Deleting an element */
int deQueue() {
	int element;
	if (isEmpty()) {
	  	cout << "Queue is empty" << endl;
	  	return -1;
	} 
	else {
	 	element = queue[front];
	  	if (front == rear) {
	    	front = -1;
	    	rear = -1;
	  	} /* Q has only one element, so we reset the queue after deleting it. */
	  	else {
	    	front = (front + 1) % SIZE;
	  	}
	  	return element;
	}
}

int peek() {
	if (isEmpty()) {
	  	cout << "Queue is empty." << endl;
	  	return -1;
	} 
	else {
	 	return queue[front];
	}
}

int main(int argc, char const *argv[]) {
    enQueue(11);
    enQueue(12);
    enQueue(13);
    int deleted = deQueue();
    cout << "Deleted Element is: " << deleted << endl;
    cout << "Front Element is: " << peek() << endl;
    
	return 0;
}


	    



