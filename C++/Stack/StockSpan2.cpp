/*
	@author
	Aakash.Verma

	Problem: The stock span problem is a financial problem where we have a 
	series of n daily price quotes for a stock and we need to calculate span 
	of stock’s price for all n days.
	The span Si of the stock’s price on a given day i is defined as the 
	maximum number of consecutive days just before the given day, for which 
	the price of the stock on the current day is less than or equal to its 
	price on the given day.

	Output: 1 1 1 2 1 4 6 
*/

#include <bits/stdc++.h> 
using namespace std; 

vector<int> stockSpan(int arr[], int n) {
	stack<pair<int, int>> s;
	vector<int> v;
	vector<int> span;

	for(int i = 0; i < n; i++) {
	    while(!s.empty() && s.top().first < arr[i]) {
			s.pop();
		}
		if(s.empty()) {
		    v.push_back(-1);
		}
		else  {
		    v.push_back(s.top().second);
		}
		s.push({arr[i], i});
	}
	for(int i = 0; i < n; i++) {
		span.push_back(i - v[i]);
	}
	return span;
}

int main(int argc, char const *argv[]) {
	
	int arr[] = {100, 80, 60, 70, 60, 75, 85}; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	vector<int> ans = stockSpan(arr, n); 
	for (int a: ans) {
		cout << a << " ";
	}

}