import java.util.*;
import java.io.*;

public class ArticulationPoint {

    public static Map<Integer, List<Integer>> buildGraph(int edges[][], int v) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int i = 1; i <= v; i++) {
            graph.put(i, new ArrayList<>());
        }

        for(int edge[] : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        return graph;
    }
    private static void dfs(int node, int parent, int[] discoveryTime, int[] lowestTime, boolean[] visited, Map<Integer, List<Integer>> graph, boolean[] articulationPoints, int time) {
        visited[node] = true;
        discoveryTime[node] = time;
        lowestTime[node] = time;

        for(int nbr : graph.get(node)) {
            if(nbr == parent) continue;

            if(visited[nbr]) {
                lowestTime[node] = Math.min(lowestTime[node], discoveryTime[nbr]);
            } else {
                ArticulationPoint.dfs(nbr, node, discoveryTime, lowestTime, visited, graph, articulationPoints, time + 1);
                lowestTime[node] = Math.min(lowestTime[node], lowestTime[nbr]);
                if(lowestTime[nbr] >= discoveryTime[node]) {
                    articulationPoints[node] = true;
                }
            }
        }
    }
    private static boolean[] findArticulationPoint(int[][] edges, int v) {
        Map<Integer, List<Integer>> graph = ArticulationPoint.buildGraph(edges, v);
        boolean visited[] = new boolean[v + 1];
        int discoveryTime[] = new int[v + 1];
        int lowestTime[] = new int[v + 1];
        boolean articulationPoints[] = new boolean[v + 1];
        int time = 0;
        int parent = -1;
        for (int i = 1; i <= v; i++) {
            if (visited[i] == false) {
                ArticulationPoint.dfs(i, parent, discoveryTime, lowestTime, visited, graph, articulationPoints, time);
            }
        }
        return articulationPoints;
    }

    public static void main(String args[]) {
        int edges[][] = {{1, 3}, {1, 5}, {1, 6}, {1, 9}, {2, 4}, {2, 6}, {2, 8}, {3, 5}, {3, 6}, {3, 7}, {3, 8}, {4, 10}, {5, 7}, {9, 11}, {9, 12}, {11, 12}};
        int v = 12;
        boolean articulationPoints[] = ArticulationPoint.findArticulationPoint(edges, v);
        for(int i = 1; i <= v; i++) {
            System.out.println(i + " - " + articulationPoints[i]);
        }


    }
}
