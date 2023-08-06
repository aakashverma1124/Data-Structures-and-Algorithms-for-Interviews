package main

import "fmt"

/*
*
*   @author
*   Md Hasnain
*
* 	Insertion in Linked List
*
*	Output:
*
*	Initial list is: 1 2 3
* 	After Inserting at the Beginning, list is: 4 1 2 3
* 	After Inserting at the End, list is: 4 1 2 3 5
*	After Inserting after given node, list is: 4 1 2 3 7 5
*
*
*
 */

func main() {
	list := LinkedListInsertion{}

	list.head = NewNode(1)
	list.head.Next = NewNode(2)
	list.head.Next.Next = NewNode(3)
	fmt.Print("Initial List: ")
	list.Print()
	list.InsertAtBeggining(4)
	fmt.Print("List after inserting at beginning: ")
	list.Print()
	list.InsertAtEnd(5)
	fmt.Print("List after inserting at end: ")
	list.Print()
	list.InsertAfterNode(7, 3)
	fmt.Print("List after inserting at after given node: ")
	list.Print()
}
