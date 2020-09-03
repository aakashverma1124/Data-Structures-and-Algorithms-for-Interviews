/*
*
*   @author
*   Aakash Verma
*	
* 	Detecting Loop in a Linked List.
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

/* Creating a class for implementing the code for Detecting a Loop in a Linked List. */
class LoopDetection {

	static Node head;

	LoopDetection() {
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

	/* finding loop in the list. */
	boolean isLoopFound() {
		Node fast, slow;
		fast = slow = head;

		if(head == null) {
			System.out.println("The list doesn't exists.");
			return false;
		}

		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
			if(slow == fast) {
				return true;
			}
		}

		return false;

	}

	/* Main method. */
	public static void main(String args[]) {
		LoopDetection list = new LoopDetection();
		list.push(3);
		list.push(4);
		list.push(5);
		list.push(6);
		list.push(7);
		list.head.next.next.next.next.next = list.head.next.next;
		boolean loopFound = list.isLoopFound();
		System.out.println(loopFound);
		System.out.println();

	}

}
