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
*/


class S01_StackCreation {

	/* We are assuming that the size of our stack is 1000, you may take any size */
	static final int MAX = 1000;
	/* 
		this top variable plays an important role in stack. This variable tells us whether the stack 
		is empty or full. Also we always insert element at the top and delete element from the top.
	*/
	int top;
	int a[] = new int[MAX]; // we'll assume this array as a stack.

	/* As soon as the object of this class is created, top is assigned as -1. */
	S01_StackCreation() {
		top = -1;
	}

	/* It checks whether the stack is empty or not, obviously if top is -1, the stack will be empty. */
	boolean isEmpty() {
		if(top < 0) {
			return true;
		}
		return false;
	}

	/* It checks whether the stack is full or not, obviously if top is MAX - 1, the stack will be full. */
	boolean isFull() {
		if(top >= MAX - 1) {
			return true;
		}
		return false;
	}

	/* function to push an element in the stack. */
 	boolean push(int key) {
		/* 
			if top becomes equal to MAX-1, then it means the array is full and we can't insert any element.
			isFull() will return true, if stack is full.
		*/
		if(isFull()) {
			System.out.println("Stack Overflow");
			return false;
		}

		/* otherwise, increment top and add key to a[top], here top works as an index only. */
		top++;
		a[top] = key;
		System.out.println("The element is pushed and top points to => " + a[top]);
		return true;

	}

	/* function to delete an element in the stack, it returns the deleted element otherwise -1. */
	int pop() {
		/* if top is -1, it means there is no element to be deleted */
		if(isEmpty()) {
			System.out.println("Stack underflow");
			return -1;
		}

		/* otherwise, delete the element from the top and decrement top. */
		int deletedElement = a[top];
		top--;
		return deletedElement;
	}

	/* function through which we can see the element present at the top. */
	int peek() {
		if(isEmpty()) {
			System.out.println("There is no record in the stack.");
			return -1;
		}

		int peekElement = a[top];
		return peekElement;
 	}

	public static void main(String[] args) {
		S01_StackCreation stack = new S01_StackCreation();
		stack.push(10); // now top is 10
		stack.push(20); // now top is 20
		stack.push(30); // now top is 30
		int temp = stack.pop(); // after performing pop, top will point to 20 again.
		System.out.println("Deleted element is: " + temp);
		System.out.println("Top element is: " + stack.peek());
	}

}
