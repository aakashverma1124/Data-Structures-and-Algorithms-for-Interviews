/*
	@author
	Aakash.Verma

	Problem: Given an array, print the Next Greater Element (NGE) for every element.
			 The Next Greater Element for an element x is the first greater element 
			 on the right side of x in array. Elements for which no greater element exist, 
			 consider next greater element as -1.
*/

#include <bits/stdc++.h> 
using namespace std; 

vector<int> nextGreaterElementToRight(int arr[], int n) { 
	
	vector<int> v;
	stack <int> s; 

	s.push(arr[0]); 

	for (int i = 1; i < n; i++) { 
		if (s.empty()) { 
			s.push(arr[i]); 
			continue; 
		} 

		/* 	
		if stack is not empty, then pop an element from stack. 
			If the popped element is smaller than next, then 
			a) push element to the vector 
			b) keep popping while elements are 
			smaller and stack is not empty 
		*/
		while (s.empty() == false && s.top() < arr[i]) {		 
			v.push_back(arr[i]);
			s.pop(); 
		} 

		/* push next to stack so that we can find 
		next greater for it */
		s.push(arr[i]); 
	} 

	while (s.empty() == false) { 
		v.push_back(-1);
		s.pop(); 
	} 
	return v;
} 

int main() { 

	int arr[] = {4, 5, 2, 25}; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	vector<int> v = nextGreaterElementToRight(arr, n); 
	for(int i: v) {
	    cout << i << endl;
	}
	return 0; 

}
