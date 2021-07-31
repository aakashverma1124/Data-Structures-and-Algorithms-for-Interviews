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
		  	System.out.println("Enqueue Operation Done, rear is at " + element);
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

	int peek() {
	    if(isEmpty()) {
	        System.out.println("Queue is empty");
	        return -1;
	    }
	    else {
	        return queue[front];
	    }
	}

	public static void main(String[] args) {

		QueueUsingArray q = new QueueUsingArray();
	    q.enQueue(11);
	    q.enQueue(12);
	    q.enQueue(13);
	    int deleted = q.deQueue();
	    System.out.println("Deleted Element is: " + deleted);
	    System.out.println("Front Element is: " + q.peek());
	    
	}

}



