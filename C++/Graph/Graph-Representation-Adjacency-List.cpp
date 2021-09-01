/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * Adjacency List of Undirected Graph
 * |0| => 1 2 
 * |1| => 0 3 
 * |2| => 0 3 
 * |3| => 1 2 
 * 
 */

#include<bits/stdc++.h>
using namespace std;

const int vertices = 4; 
vector<int> adjacencyList[vertices]; 

void addEdge(int source, int destination) {
	adjacencyList[source].push_back(destination);
	adjacencyList[destination].push_back(source); // for directed graph comment this line
}

void printGraph() {
    cout << "Adjacency List of Undirected Graph" << endl;
    for (int i = 0; i < vertices; i++) {
        cout << "|" << i << "| => "; 
        for(auto nbr : adjacencyList[i]) {
        	cout << nbr << " ";
        }
        cout << endl;
    }
}

int main() {
	addEdge(0, 1);
	addEdge(0, 2);
	addEdge(1, 3);
	addEdge(2, 3);
	printGraph();
	return 0;
}
