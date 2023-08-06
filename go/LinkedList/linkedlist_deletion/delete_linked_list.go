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

type LinkedListDeletion struct {
	head *Node
}

func (list *LinkedListDeletion) Print() {
	current := list.head
	for current != nil {
		fmt.Printf("%d ", current.Data)
		current = current.Next
	}
	fmt.Println()
}

func (list *LinkedListDeletion) DeleteFromStart() {
	if list.head == nil {
		log.Printf("Can't delete from Empty List")
		return
	}
	list.head = list.head.Next
}

func (list *LinkedListDeletion) DeleteAfterNode(nodeAfter int) {
	current := list.head
	prev := &Node{}
	for current != nil {
		if current.Data == nodeAfter { // If nodeAfterExist
			break
		}
		prev = current
		current = current.Next
	}
	if current == nil {
		log.Println("DeleteAfterNode operation can't perform as nodeAfter does not exist")
		return
	}
	prev.Next = current.Next
}

func (list *LinkedListDeletion) DeleteFromEnd() {
	current := list.head
	prev := &Node{}
	for current != nil && current.Next != nil { // traverse till last node
		prev = current
		current = current.Next
	}
	prev.Next = nil
}
