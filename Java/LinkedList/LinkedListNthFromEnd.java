/*
*
*   @author
*   Aakash Verma
*	
* 	Nth Node from the Last of a Linked List
*
*	Output: 
*
*	The list is: 3 4 5 6 7 
*	5
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

/* Creating a class for implementing the code for Deletion in a Linked List. */
class LinkedListNthFromEnd {

	static Node head;

	LinkedListNthFromEnd() {
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

	/* Utility code for getting nth node from last of the linked list. */
	void nthNodeFromEnd(int nthNode) {
		Node prev, curr;
		prev = curr = head;

		if(head == null) {
			System.out.println("The list doesn't exist");
			return;
		}
		/* curr pointer is being moved ahead n times. */
		for(int i = 0; i < nthNode; i++) {
			if(curr != null) {
				curr = curr.next;
			}
			else {
				System.out.println("Enough nodes are not present in the linked list.");
				return;
			}
		}
		/* 	Now the difference between prev and curr pointer is n
		 	now we'll move prev and curr pointer both until curr becomes null 
		 	and finally prev will be at n from last */
		while(curr != null) {
			prev = prev.next;
			curr = curr.next;
		}
		/* finally printing data of nth node from last */
		System.out.println(prev.data);

	}

	/* Main method. */
	public static void main(String args[]) {
		LinkedListNthFromEnd list = new LinkedListNthFromEnd();
		list.push(3);
		list.push(4);
		list.push(5);
		list.push(6);
		list.push(7);
		System.out.print("The list is: ");
		list.printList();
		list.nthNodeFromEnd(3);
		System.out.println();

	}

}
