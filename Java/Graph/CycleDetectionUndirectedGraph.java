/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * false 
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

    public boolean detectCycleUtil(int node, boolean[] visited, int parent) {
        visited[node] = true;
        for(int nbr : adjacencyList[node]) {
            if(!visited[nbr]) {
                boolean cycleFound = detectCycleUtil(nbr, visited, node);
                if(cycleFound) {
                    return true;
                }
            } else {
                if(nbr != parent) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean detectCycle() {
        boolean[] visited = new boolean[vertices];
        return detectCycleUtil(0, visited, -1); 
    }

    public static void main( String args[] ) {
        Graph g = new Graph(6);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(2, 4);
        g.addEdge(4, 5);
        boolean ans = g.detectCycle();
        System.out.println(ans);
    }

}