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

#include <iostream>
using namespace std;

const int MAX = 100;
int queue[MAX]; 
int front = 0;
int rear = -1;


void enqueue(int item) {
	if(rear >= MAX - 1) {
		cout << "Queue is Full" << endl;
	}
	else if (front == -1 && rear == -1) {
		front = 0;
		rear = 0;
		queue[rear] = item;
		cout << "Enqueue Operation Done, rear is at " << queue[rear] << endl;
	}
	else {
		queue[++rear] = item;
		cout << "Enqueue Operation Done, rear is at " << queue[rear] << endl;
	}
}

int dequeue() {
	if(front == -1 || front > rear) {
		cout << "Queue is empty." << endl;
		return -1; /* Assuming the queue will have positive numbers. */
	}
	else {
		int deletedItem = queue[front];
		if(rear == front) {
			rear = -1;
			front = -1;
		}
		else {
			front++;
		}
		return deletedItem;
	}
}

int peek() {
	if(front == -1 || front > rear) {
		cout << "Queue is empty." << endl;
		return -1; /* Assuming the queue will have positive numbers. */
	}
	else {
		int frontItem = queue[front];
		return frontItem;
	}
}

int main(int argc, char const *argv[])
{
	enqueue(11);
	enqueue(12);
	enqueue(13);
	int del = dequeue();
	cout << "Deleted Element is: " << del << endl;
	cout << "Front element is: " << peek() << endl;
	return 0;
}