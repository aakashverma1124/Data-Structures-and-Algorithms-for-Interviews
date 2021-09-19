/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * 2 0 1 3 
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

	vector<int> breadthFirstSearch(int source) {
		vector<int> bfs;
		queue<int> q;
		bool *visited = new bool[vertices]{false};
		q.push(source);
		visited[source] = true;
		while(!q.empty()) {
			int curr = q.front();
			q.pop();
			bfs.push_back(curr);
			for(auto nbr : adjacencyList[curr]) {
				if(visited[nbr] == false) {
					q.push(nbr);
					visited[nbr] = true;
				}
			}
		}
		return bfs;
	}
};

int main() {
	Graph g(4);
	g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
	vector<int> ans = g.breadthFirstSearch(2);
	for(auto ele : ans) {
		cout << ele << " ";
	}
	return 0;
}
