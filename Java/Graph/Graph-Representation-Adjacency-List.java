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

import java.util.*;

class Graph {

	int vertices; 
    LinkedList<Integer> adjacencyList[]; 
    
    @SuppressWarnings("unchecked")
    public Graph(int vertices) {
        this.vertices = vertices;
        adjacencyList = new LinkedList[vertices];

        for (int i = 0; i < vertices; i++) {
            adjacencyList[i] = new LinkedList<>();
        }
    }

    public void addEdge(int source, int destination) {
    	this.adjacencyList[source].add(destination);
    	this.adjacencyList[destination].add(source); // for directed graph comment this line
    }

    public void printGraph() {
        System.out.println("Adjacency List of Undirected Graph");
        for (int i = 0; i < vertices; i++) {
        	System.out.print("|" + i + "| => ");
            for(int nbr : adjacencyList[i]) {
            	System.out.print(nbr + " ");
            }
            System.out.println();
        }
    }

    public static void main( String args[] ) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 3);

        g.printGraph();
    }

}