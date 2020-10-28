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

	Compile using:  javac filename.java
	Run using: java filename
*/


/* A simple Node Structure */
class Node {
	int data;
	Node next;

	public Node(int key) {
		data = key;
		next = null;
	}
}

class QueueUsingLinkedList {

	/* declaring node */
	static Node front;
	static Node rear;
	/* defining node as null upon creation of the object. */
	QueueUsingLinkedList() {
		front = null;
		rear = null;
	}

	public void enqueue(int item) { 
		Node new_node = new Node(item);
		new_node.data = item;
		
		if (rear == null) { 
			front = rear = new_node; 
			System.out.println("Enqueue Operation Done, rear is at " + rear.data);
			return; 
		} 

		rear.next = new_node; 
		rear = new_node; 
		System.out.println("Enqueue Operation Done, rear is at " + rear.data);
	} 

	public int dequeue() {
		if (front == null) 
		return -1; 
	
		Node temp = front; 
		front = front.next; 

		if (front == null) 
			rear = null;

		return temp.data;
	}

	int peek() {
		if (front == null) 
			return -1; 
		return front.data;
	}

	public static void main(String[] args) {
		QueueUsingLinkedList q = new QueueUsingLinkedList();
		q.enqueue(11);
		q.enqueue(12);
		q.enqueue(13); 
		int del = q.dequeue();
		System.out.println("Deleted Element is: " + del);
		System.out.println("Front element is: " + q.peek());
	}
}