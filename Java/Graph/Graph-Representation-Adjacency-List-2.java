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

import java.util.*;

class Graph {

    List<String> cities;
    HashMap<String, ArrayList<String>> adjacencyList; 
    
    public Graph(List<String> cities) {
        this.cities = cities;
        adjacencyList = new HashMap<>();

        for (String city : this.cities) {
            adjacencyList.put(city, new ArrayList<>());
        }
    }

    public void addEdge(String source, String destination) {
        this.adjacencyList.get(source).add(destination);
        this.adjacencyList.get(destination).add(source); // for directed graph comment this line
    }

    public void printGraph() {
        System.out.println("Adjacency List of Undirected Graph");
        for (String city : this.cities) {
            System.out.print("|" + city + "| => ");
            for(String nbrCity : adjacencyList.get(city)) {
                System.out.print(nbrCity + " ");
            }
            System.out.println();
        }
    }

    public static void main( String args[] ) {
        List<String> cities = new ArrayList<>();
        cities.add("Delhi");
        cities.add("Mumbai");
        cities.add("Bangalore");
        cities.add("Hyderabad");
        Graph g = new Graph(cities);
        g.addEdge("Delhi", "Mumbai");
        g.addEdge("Delhi", "Bangalore");
        g.addEdge("Mumbai", "Hyderabad");
        g.addEdge("Mumbai", "Bangalore");

        g.printGraph();
    }

}