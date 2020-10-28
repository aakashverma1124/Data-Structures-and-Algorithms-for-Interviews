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


	Compile using: javac filename.java
	Run using: java classname
*/


public class QueueUsingArray {
  
	int SIZE = 10; 
  	int front, rear;
  	int queue[] = new int[SIZE];

  	/* assigning front & rear as -1 initially */
  	QueueUsingArray() {
    	front = -1;
    	rear = -1;
  	}

	/* Checking if the Queue is full */
	boolean isFull() {
		if (front == 0 && rear == SIZE - 1)
		  	return true;
		if (front == rear + 1)
		  	return true;
		return false;
	}

	/* Check if the Queue is empty */
	boolean isEmpty() {
		if (front == -1)
		  	return true;
		else
		  	return false;
	}

	// Adding an element
	void enQueue(int element) {
		if (isFull()) {
		  	System.out.println("Queue is full");
		} 
		else {
		  	if (front == -1)
		    	front = 0;
		  	rear = (rear + 1) % SIZE;
		  	queue[rear] = element;
		  	System.out.println("Inserted " + element);
		}
	}

	/* Deleting an element */
	int deQueue() {
		int element;
		if (isEmpty()) {
		  	System.out.println("Queue is empty");
		  	return (-1);
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
		  	System.out.println("Empty Queue");
		} 
		else {
		 	System.out.println("Front points to: " + front);
			System.out.print("Items in Queue: ");
			for (i = front; i != rear; i = (i + 1) % SIZE)
			System.out.print(queue[i] + " ");
			System.out.println(queue[i]);
			System.out.println("Rear points to: " + rear);
		}
	}

	public static void main(String[] args) {

		QueueUsingArray q = new QueueUsingArray();

	    /* Fails because front = -1 */
	    q.deQueue();

	    q.enQueue(1);
	    q.enQueue(2);
	    q.enQueue(3);
	    q.enQueue(4);
	    q.enQueue(5);

	    q.display();

	    int item = q.deQueue();

	    if (item != -1) {
	      System.out.println("Deleted Element is " + item);
	    }
	    q.display();
	    q.enQueue(7);
	    q.display();
	}

}



