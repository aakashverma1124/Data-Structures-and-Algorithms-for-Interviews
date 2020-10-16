/*
# @author
# Aakash.Verma

# Problem: Find the largest rectangular area possible in a given histogram where the largest 
# rectangle can be made of a number of contiguous bars. For simplicity, assume that 
# all bars have same width and the width is 1 unit.

# For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}.
# The largest possible rectangle possible is 12.
*/

#include <bits/stdc++.h>
using namespace std;

vector<int> nsel(vector<int> arr, int n) {
	vector<int> nselIndex;
	stack<pair<int, int>> s;

	for(int i = 0; i < n; i++) {
	    while(!s.empty() && s.top().first >= arr[i]) {
			s.pop();
		}
		if(s.empty()) {
		    nselIndex.push_back(-1);
		}
		else  {
		    nselIndex.push_back(s.top().second);
		}
		s.push({arr[i], i});
	}
	return nselIndex;
}

vector<int> nser(vector<int> arr, int n) {
	vector<int> nserIndex;
	stack<pair<int, int>> s;

	for(int i = n - 1; i >= 0; i--) {
	    while(!s.empty() && s.top().first >= arr[i]) {
			s.pop();
		}
		if(s.empty()) {
		    nserIndex.push_back(n);
		}
		else  {
		    nserIndex.push_back(s.top().second);
		}
		s.push({arr[i], i});
	}
	reverse(nserIndex.begin(), nserIndex.end());
	return nserIndex;
}

int maxAreaHistogram(vector<int> arr, int n) {
	vector<int> nselIndex = nsel(arr, n);
	vector<int> nserIndex = nser(arr, n);
	vector<int> ans;
	int max = INT_MIN;
	for(int i = 0; i < n; i++) {
		ans.push_back((nserIndex[i] - nselIndex[i] - 1) * arr[i]);
		if(max < ans[i]) {
			max = ans[i];
		}
	}
	return max;
}

int main() {
	vector<int> arr = {6, 2, 5, 4, 5, 1, 6};
	int ans = maxAreaHistogram(arr, arr.size());
	cout << ans << endl;
	
}