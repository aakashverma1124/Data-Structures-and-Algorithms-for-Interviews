package main

import (
	"fmt"
	"log"
)

type Node struct {
	Data int
	Next *Node
}

func NewNode(data int) *Node { // create New Node
	return &Node{
		Data: data,
		Next: nil,
	}
}

type LinkedListInsertion struct {
	head *Node
}

func (list *LinkedListInsertion) Print() {
	current := list.head
	for current != nil {
		fmt.Printf("%d ", current.Data)
		current = current.Next
	}
	fmt.Println()
}

func (list *LinkedListInsertion) InsertAtBeggining(key int) {
	newNode := NewNode(key)
	newNode.Next = list.head
	list.head = newNode
}

func (list *LinkedListInsertion) InsertAfterNode(key, nodeAfter int) {
	current := list.head
	for current != nil {
		if current.Data == nodeAfter { // If nodeAfterExist
			break
		}
		current = current.Next
	}
	if current == nil {
		log.Println("InsertAfterNode operation can't perform as nodeAfter does not exist")
		return
	}
	temp := current.Next
	newNode := NewNode(key)
	current.Next = newNode
	newNode.Next = temp
}

func (list *LinkedListInsertion) InsertAtEnd(key int) {
	current := list.head
	for current != nil && current.Next != nil { // traverse till last node
		current = current.Next
	}

	newNode := NewNode(key)
	current.Next = newNode
}
