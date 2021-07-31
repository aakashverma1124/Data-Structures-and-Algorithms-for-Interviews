/*
*
*   @author
*   Aakash Verma
*	
* 	Start of the Loop
*
*	Output: 
*	5
* 	
*
*/


/* Below is the structute of a node which is used to create a new node every time. */
class Node {
	int data;
	Node next;

	public Node(int key) {
		data = key;
		next = null;
	}
}

/* Creating a class for implementing the code for Starting of a loop in a Linked List. */
class StartingOfLoop {

	static Node head;

	StartingOfLoop() {
		head = null;
	}

	/* Utility code for inserting into the linked list. */
	void push(int key) {
		Node h = head;
		if(h == null) {
			Node temp = new Node(key);
			temp.next = null;
			head = temp;
		}
		else {
			while(h.next != null) {
				h = h.next;
			}
			Node temp = new Node(key);
			temp.next = null;
			h.next = temp;

		}
	}

	/* starting of a loop in the list. */
	void startingOfLoop() {
		Node fast, slow;
		fast = slow = head;
		boolean isLoopFound = false;
		if(head == null) {
			System.out.println("The list doesn't exists.");
			return;
		}

		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
			if(slow == fast) {
				isLoopFound = true;
				break;
			}
		}

		if(isLoopFound) {
			slow = head;
			while(slow != fast) {
				slow = slow.next;
				fast = fast.next;
			}
		}

		System.out.println(slow.data + " ");

	}

	/* Main method. */
	public static void main(String args[]) {
		StartingOfLoop list = new StartingOfLoop();
		list.push(3);
		list.push(4);
		list.push(5);
		list.push(6);
		list.push(7);
		list.head.next.next.next.next.next = list.head.next.next;
		list.startingOfLoop();
		System.out.println();

	}

}
