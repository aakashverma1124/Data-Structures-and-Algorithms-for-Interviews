/*	
	@author
	Aakash.Verma

	Stack is a LIFO data structures:
	LIFO stands for Last In First Out 
	
	We can't access any element except top. Top is that element which has been inserted at last
	and can be retrieved first.

	I am assuming that you are here after going through the theory of Stack and looking for implementation.
	
	Output:
	The element is pushed and top points to => 10
	The element is pushed and top points to => 20
	The element is pushed and top points to => 30
	Deleted element is: 30
	Top element is: 20

	Compile using:  g++ filename.cpp
	Run using: ./a.out filename.cpp
*/

#include <iostream>
using namespace std;

/* defining size of stack */
const int MAX = 100;

/* declaring stack */
int stack[MAX];

/* 
	this top variable plays an important role in stack. This variable tells us whether the stack 
	is empty or full. Also we always insert element at the top and delete element from the top.
*/
int top = -1;

/* It checks whether the stack is empty or not, obviously if top is -1, the stack will be empty. */
bool isEmpty() {
	if(top < 0) {
		return 1;
	}
	return 0;
}

/* It checks whether the stack is full or not, obviously if top is MAX - 1, the stack will be full. */
bool isFull() {
	if(top >= MAX - 1) {
		return 1;
	}
	return 0;
}


/* function to push an element in the stack. */
int push(int key) {
/* 
	if top becomes equal to MAX-1, then it means the array is full and we can't insert any element.
	isFull() will return true, if stack is full.
*/
	if(isFull()) {
		cout << "Stack Overflow" << endl;
		return 0;
	}

	/* otherwise, increment top and add key to stack[top], here top works as an index only. */
	stack[++top] = key;
	cout << "The element is pushed and top points to => " <<  stack[top] << endl;
	return 1;

}

/* function to delete an element in the stack, it returns the deleted element otherwise -1. */
int pop() {
	/* if top is -1, it means there is no element to be deleted */
	if(isEmpty()) {
		cout << "Stack underflow" << endl;
		return -1;
	}

	/* otherwise, delete the element from the top and decrement top. */
	int deletedElement = stack[top];
	top--;
	return deletedElement;
}

/* function through which we can see the element present at the top. */
int peek() {
	if(isEmpty()) {
		cout << "There is no record in the stack." << endl;
		return -1;
	}

	int peekElement = stack[top];
	return peekElement;
}



int main(int argc, char const *argv[]) {
	push(10);
	push(20);
	push(30);
	int temp = pop(); // after performing pop, top will point to 20 again.
	cout << "Deleted element is: " << temp << endl;
	cout << "Top element is: " << peek() << endl;
	return 0;
}