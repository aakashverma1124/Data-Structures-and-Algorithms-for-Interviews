/*
*
*   @author
*   Aakash Verma
*	
* 	Deletion in a Linked List
*
*	Output: 
*
*	The list is: 3 4 5 6 7 
*	After deletion the list is: 3 4 6 7 
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
class LinkedListDeletion {

	static Node head;

	LinkedListDeletion() {
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

	}

	/* Utility code for deleting a node out of the linked list. */
	void deleteNode(int key) {
		Node h = head, prev = null;
		if(h == null) {
			System.out.println("The list is empty, the node can't be deleted.");
			return;
		}
		if(h.data == key) {
			head = h.next;
			return;
		}
		while (h != null && h.data != key) {
			prev = h;
			h = h.next;
		}
		if(h == null) {
			System.out.println("The key is not present in the list.");
			return;
		}
		prev.next = h.next;

	}

	/* Main method. */
	public static void main(String args[]) {
		LinkedListDeletion list = new LinkedListDeletion();
		list.push(3);
		list.push(4);
		list.push(5);
		list.push(6);
		list.push(7);
		System.out.print("The list is: ");
		list.printList();
		System.out.println();
		list.deleteNode(5);
		System.out.print("After deletion the list is: ");
		list.printList();
		System.out.println();

	}

}
