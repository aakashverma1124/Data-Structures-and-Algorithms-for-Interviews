/*
	@author
	Aakash.Verma

	Problem: Given an array, print the Next Greater Element (NGE) for every element.
			 The Next Greater Element for an element x is the first greater element 
			 on the left side of x in array. Elements for which no greater element exist, 
			 consider next greater element as -1.
*/

import java.io.*; 
import java.util.*;

class NGEL {

	public ArrayList<Integer> nextGreaterElementToLeft(int arr[], int n) { 
	
		ArrayList<Integer> l = new ArrayList<>(); 
		Stack<Integer> s = new Stack<>();
		
		s.push(arr[0]);
		l.add(-1);

		for (int i = 1; i < n; i++) { 

			/* 	
			if stack is not empty, then pop an element from stack. 
				If the popped element is smaller than next, then 
				a) push element to the list 
				b) keep popping while elements are 
				smaller and stack is not empty 
			*/
			while (s.empty() == false && s.peek() < arr[i]) {		 
				s.pop(); 
			} 
			if(s.empty()) {
				l.add(-1);
			}
			else {
				l.add(s.peek());
			}

			/* push next to stack so that we can find 
			next greater for it */
			s.push(arr[i]); 
		} 
		return l;
	} 

	public static void main(String[] args) {
		NGEL ngel = new NGEL();
		int arr[] = {4, 5, 2, 25};
		int n = arr.length;
		ArrayList<Integer> list = ngel.nextGreaterElementToLeft(arr, n); 
		System.out.println(list.toString());
	}

}
