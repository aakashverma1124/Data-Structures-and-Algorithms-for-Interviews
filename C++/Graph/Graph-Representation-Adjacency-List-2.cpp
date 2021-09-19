/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * Adjacency List of Undirected Graph
 * |Delhi| => Mumbai Bangalore 
 * |Mumbai| => Delhi Hyderabad Bangalore 
 * |Bangalore| => Delhi Mumbai 
 * |Hyderabad| => Mumbai
 * 
 */

#include<bits/stdc++.h>
using namespace std;

class Graph {
	vector<string> cities;
	unordered_map<string, vector<string>> adjacencyList;

public:
	Graph(vector<string> c) {
		cities = c;
		for(auto city : cities) {
		    vector<string> v;
			adjacencyList[city] = v;
		}
	}

	void addEdge(string source, string destination) {
		adjacencyList[source].push_back(destination);
		adjacencyList[destination].push_back(source); // for directed graph comment this line
	}

	void printGraph() {
	    cout << "Adjacency List of Undirected Graph" << endl;
	    for (auto city : cities) {
	        cout << "|" << city << "| => "; 
	        for(auto nbrCity : adjacencyList[city]) {
	        	cout << nbrCity << " ";
	        }
	        cout << endl;
	    }
	}
};

int main() {
	vector<string> cities = {"Delhi", "Mumbai", "Bangalore", "Hyderabad"};
	Graph g(cities);
	g.addEdge("Delhi", "Mumbai");
    g.addEdge("Delhi", "Bangalore");
    g.addEdge("Mumbai", "Hyderabad");
    g.addEdge("Mumbai", "Bangalore");
	g.printGraph();
	return 0;

}