/*
*   @author
*   Aakash Verma
*
*   Output:
*   5 6 3 4 0 2 1 
*/

#include <bits/stdc++.h> 
using namespace std;

vector<int> topologicalSort(vector<vector<int>> edges, int vertices) {
	vector<int> sortedOrder;
	if(vertices <= 0) {
		return sortedOrder;
	}

	map<int, int> inDegree;
	map<int, vector<int>> graph;

	// intializing the graph
	for(int i = 0; i < vertices; i++) {
		inDegree[i] = 0;
		vector<int> v;
		graph[i] = v;
	}

	// building the graph
	for(int i = 0; i < edges.size(); i++) {
		int parent = edges[i][0];
		int child = edges[i][1];
		graph[parent].push_back(child);
		inDegree[child] += 1;
	}

	// processing all valid starting nodes
	queue<int> q;
	for(auto entry : inDegree) {
		if(entry.second == 0) {
			q.push(entry.first);
		}
	}

	while(!q.empty()) {
		int vertex = q.front();
		q.pop();
		sortedOrder.push_back(vertex);
		vector<int> children = graph[vertex];
		for(auto child : children) {
			inDegree[child] -= 1;
			if(inDegree[child] == 0) {
				q.push(child);
			}
		}
	}

	if(sortedOrder.size() != vertices) {
	    vector<int> v;
		return v;
	}

	return sortedOrder;

}

int main(int argc, char const *argv[]) {
	vector<vector<int>> edges {{6, 4}, {6, 2}, {5, 3}, {5, 4}, {3, 0}, {3, 1}, {3, 2}, {4, 1}};
	vector<int> ans = topologicalSort(edges, 7);
	for(auto a : ans) {
		cout << a << " ";
	}
	return 0;
}