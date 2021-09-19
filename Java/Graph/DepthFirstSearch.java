/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Output:
 * 0 1 2 3 4 5 
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

    public void dfsUtil(int node, boolean[] visited, List<Integer> dfs) {
        dfs.add(node);
        visited[node] = true;
        for(int child : adjacencyList[node]) {
            if(!visited[child]) {
                dfsUtil(child, visited, dfs);
                visited[child] = true;
            }
        }
    }

    public List<Integer> depthFirstSearch(int source) {
        List<Integer> dfs = new ArrayList<>();
        boolean[] visited = new boolean[vertices];
        dfsUtil(source, visited, dfs);
        return dfs;
    }

    public static void main( String args[] ) {
        Graph g = new Graph(6);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(2, 4);
        g.addEdge(4, 5);
        List<Integer> ans = g.depthFirstSearch(0);
        for(int ele : ans) {
            System.out.print(ele + " ");
        }
    }

}