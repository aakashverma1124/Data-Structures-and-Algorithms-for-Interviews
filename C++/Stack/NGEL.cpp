/*
	@author
	Aakash.Verma

	Problem: Given an array, find an array of the Next Greater Elements (NGE) for every element.
			 The Next Greater Element for an element x is the first greater element 
			 on the left side of x in array. Elements for which no greater element exist, 
			 consider next greater element as -1.
*/

#include <bits/stdc++.h> 
using namespace std; 

vector<int> nextGreaterElementToLeft(int arr[], int n) {
	stack<int> s;
	vector<int> v;

	for(int i = 0; i < n; i++) {
	    while(!s.empty() && s.top() <= arr[i]) {
			s.pop();
		}
		if(s.empty()) {
		    v.push_back(-1);
		}
		else  {
		    v.push_back(s.top());
		}
		s.push(arr[i]);
	}
	return v;
}

int main(int argc, char const *argv[]) {
	
	int arr[] = {4, 5, 2, 25}; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	vector<int> ans = nextGreaterElementToLeft(arr, n); 
	for (int a: ans) {
		cout << a << " ";
	}

}