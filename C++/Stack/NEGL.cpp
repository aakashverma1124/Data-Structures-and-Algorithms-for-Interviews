/*
	@author
	Aakash.Verma

	Problem: Given an array, print the Next Greater Element (NGE) for every element.
			 The Next Greater Element for an element x is the first greater element 
			 on the left side of x in array. Elements for which no greater element exist, 
			 consider next greater element as -1.
*/

#include <bits/stdc++.h> 
using namespace std;

vector<int> nextGreaterElementToLeft(vector<int> arr, int n) { 

	vector<int> l;
	stack<int> s;
	
	s.push(arr[0]);
	l.push_back(-1);

	for (int i = 1; i < n; i++) { 

		/* 	
		if stack is not empty, then pop an element from stack. 
			If the popped element is smaller than next, then 
			a) push element to the list 
			b) keep popping while elements are 
			smaller and stack is not empty 
		*/
		while (s.empty() == false && s.top() < arr[i]) {		 
			s.pop(); 
		} 
		if(s.empty()) {
			l.push_back(-1);
		}
		else {
			l.push_back(s.top());
		}

		/* push next to stack so that we can find 
		next greater for it */
		s.push(arr[i]); 
	} 
	return l;
} 

int main(int argc, char const *argv[]) {
	vector<int> arr = {4, 5, 2, 25};
	vector<int> ans = nextGreaterElementToLeft(arr, arr.size()); 	
	for (int i: ans) {
		cout << i << " ";
	}
}

