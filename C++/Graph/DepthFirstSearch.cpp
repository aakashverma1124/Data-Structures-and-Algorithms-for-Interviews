/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * 0 1 2 3 4 5
 * 
 */

#include<bits/stdc++.h>
using namespace std;

class Graph {
	int vertices;
	vector<int> *adjacencyList;

public:
	Graph(int v) {
		vertices = v;
		adjacencyList = new vector<int>[vertices];
	}

	void addEdge(int source, int destination) {
		adjacencyList[source].push_back(destination);
		adjacencyList[destination].push_back(source); // for directed graph comment this line
	}

	void dfsUtil(int node, bool *visited, vector<int> &dfs) {
		dfs.push_back(node);
		visited[node] = true;
		for(auto child : adjacencyList[node]) {
			if(!visited[child]) {
				visited[child] = true;
				dfsUtil(child, visited, dfs);
			}
		}
	}

	vector<int> depthFirstSearch(int source) {
		vector<int> dfs;
		bool *visited = new bool[vertices]{false};
		dfsUtil(source, visited, dfs);
		return dfs;
	}
};

int main() {
	Graph g(6);
	g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(2, 4);
    g.addEdge(4, 5);
	vector<int> ans = g.depthFirstSearch(0);
	for(auto ele : ans) {
		cout << ele << " ";
	}
	return 0;
}
