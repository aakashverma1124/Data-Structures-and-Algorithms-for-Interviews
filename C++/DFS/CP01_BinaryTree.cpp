/*
*   @author
*   Aakash Verma
*
*/

#include <bits/stdc++.h> 
using namespace std;

vector<int> bfs(int n, int source, map<int, vector<int>> tree) {
	vector<int> distance(n + 1, 0);
	queue<int> q;
	q.push(source);
	while(!q.empty()) {
		int current = q.front();
		q.pop();
		for(auto child : tree[current]) {
			distance[child] = distance[current] + 1;
			q.push(child);
		}
	}
	return distance;
}

int main(int argc, char const *argv[]) {
	
	int t;
	cin >> t;

	while(t--) {
		int n;
		cin >> n;
		map<int, vector<int>> tree;
		for(int i = 0; i < (n - 1); i++) {
			int a, b;
			cin >> a >> b;
			tree[a].push_back(b);	
		}
		vector<int> distance = bfs(n, 1, tree);

		for(int i = 1; i <= n; i++) {
			cout << distance[i] << " ";
		}
		cout << endl;
	}
	return 0;
}