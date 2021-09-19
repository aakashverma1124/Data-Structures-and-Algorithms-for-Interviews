/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * 2 0 1 3
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

    public List<Integer> breadthFirstSearch(int source) {
        List<Integer> bfs = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[vertices];
        q.offer(source);
        visited[source] = true;
        while(!q.isEmpty()) {
            int curr = q.poll();
            bfs.add(curr);
            for(int nbr : adjacencyList[curr]) {
                if(visited[nbr] == false) {
                    q.offer(nbr);
                    visited[nbr] = true;
                }
            }
        }
        return bfs;
    }

    public static void main( String args[] ) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        List<Integer> ans = g.breadthFirstSearch(2);
        for(int ele : ans) {
            System.out.print(ele + " ");
        }
    }

}