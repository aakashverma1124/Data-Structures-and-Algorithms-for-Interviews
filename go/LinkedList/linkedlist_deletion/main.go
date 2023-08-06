package main

import "fmt"

/*
*
*   @author
*   Md Hasnain
*
* 	Deletion from Linked List
*
*	Output:
*
*	Initial list is: 1 2 3 4 5
* 	After Deleting at the Beginning, list is: 2 3 4 5
* 	After Deleting at the End, list is: 2 3 4
*	After Inserting after given node, list is: 2 4
*
*
*
 */

func main() {
	list := LinkedListDeletion{}

	list.head = NewNode(1)
	current := list.head
	for i := 2; i <= 5; i++ {
		// if current == nil {
		// 	current = NewNode(i)
		// } else {
		current.Next = NewNode(i)
		// }
		current = current.Next
	}

	fmt.Print("Initial List: ")
	list.Print()
	list.DeleteFromStart()
	fmt.Print("List after deleting at beginning: ")
	list.Print()
	list.DeleteFromEnd()
	fmt.Print("List after deleting at end: ")
	list.Print()
	list.DeleteAfterNode(3)
	fmt.Print("List after deleting given node: ")
	list.Print()
}
