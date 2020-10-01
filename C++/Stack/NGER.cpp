/*
	@author
	Aakash.Verma

	Problem: Given an array, find an array of the Next Greater Elements (NGE) for every element.
			 The Next Greater Element for an element x is the first greater element 
			 on the right side of x in array. Elements for which no greater element exist, 
			 consider next greater element as -1.
*/

#include <bits/stdc++.h> 
using namespace std; 

vector<int> nextGreaterElementToRight(int arr[], int n) {
	stack<int> s;
	vector<int> v;

	for(int i = n - 1; i >= 0; i--) {
	    while(!s.empty() && s.top() < arr[i]) {
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
	reverse(v.begin(), v.end());
	return v;
}

int main(int argc, char const *argv[]) {
	
	int arr[] = {7, 8, 1, 4}; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	vector<int> ans = nextGreaterElementToRight(arr, n); 
	for (int a: ans) {
		cout << a << " ";
	}

}