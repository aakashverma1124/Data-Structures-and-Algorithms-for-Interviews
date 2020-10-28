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
	Queue is empty
	Inserted 1
	Inserted 2
	Inserted 3
	Inserted 4
	Inserted 5
	Front points to: 0
	Items in Queue: 1 2 3 4 5
	Rear points to: 4
	Deleted Element is 1
	Front points to: 1
	Items in Queue: 2 3 4 5
	Rear points to: 4
	Inserted 7
	Front points to: 1
	Items in Queue: 2 3 4 5 7
	Rear points to: 5

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
	  	cout << "Inserted " << element << endl;
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

void display() {

	/* Function to display status of Circular Queue */
	int i;
	if (isEmpty()) {
	  	cout << "Empty Queue" << endl;
	} 
	else {
	 	cout << "Front points to: " << front << endl;
		cout << "Items in Queue: ";
		for (i = front; i != rear; i = (i + 1) % SIZE)
			cout << queue[i] << " ";
		cout << queue[i] << endl;
		cout << "Rear points to: " << rear << endl;
	}
}

int main(int argc, char const *argv[]) {
	/* Fails because front = -1 */
    deQueue();

    enQueue(1);
    enQueue(2);
    enQueue(3);
    enQueue(4);
    enQueue(5);

    display();

    int item = deQueue();

    if (item != -1) {
      cout << "Deleted Element is " << item << endl;
    }
    display();
    enQueue(7);
    display();
	return 0;
}


	    



