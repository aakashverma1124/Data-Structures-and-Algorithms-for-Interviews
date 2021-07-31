/*
*
*   @author
*   Aakash Verma
*	
* 	Middle in a Linked List
*
*	Output: 
*	true
*		
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

/* Creating a class for implementing the code for Middle in a Linked List. */
class MiddleOfLinkedList {

	static Node head;

	MiddleOfLinkedList() {
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

	/* Utility code for traversing the linked list. */
	void printList() {
		Node h = head;
		while(h != null) {
			System.out.print(h.data + " ");
			h = h.next;
		}
		System.out.println();
	}

	/* Utility code for getting middle of the linked list. */
	void findMiddle() {
		Node fast, slow;
		fast = slow = head;

		if(head == null) {
			System.out.println("The list doesn't exist");
			return;
		}

		/* 
			move one pointer one time & other pointer two times
			which will result fast pointer at the end and slow pointer in the middle of a list
		*/
		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}

		/* finally printing data of middle of list */
		System.out.println(slow.data);

	}

	/* Main method. */
	public static void main(String args[]) {
		MiddleOfLinkedList list = new MiddleOfLinkedList();
		list.push(3);
		list.push(4);
		list.push(5);
		list.push(6);
		list.push(7);
		System.out.print("The list is: ");
		list.printList();
		System.out.print("Middle Of List is: ");
		list.findMiddle();

		list.push(8);

		System.out.print("The list is: ");
		list.printList();
		System.out.print("Middle Of List is: ");
		list.findMiddle();


		System.out.println();

	}

}
