#include <bits/stdc++.h> 
using namespace std;

vector<int> tree[200001];

void dfs(int curr, int prev, int count[]) {
	count[curr] = 1;
	for(auto nbr : tree[curr]) {
		dfs(nbr, curr, count);
		count[curr] += count[nbr];
	}
}


int main(int argc, char const *argv[]) {
	int n;
	cin >> n;
	int emp[n - 1];
	for(int i = 0; i < n - 1; i++) {
		cin >> emp[i];
		tree[emp[i]].push_back(i + 2);	
	}
	int count[n + 1];
	dfs(1, 0, count);
	for(int i = 1; i <= n; i++) {
		cout << count[i] - 1 <<  " ";
	}
	cout << endl;
	return 0;
}