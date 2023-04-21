import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Pair {
    int node;
    int distance;

    public Pair(int node, int distance) {
        this.node = node;
        this.distance = distance;
    }
}

public class PrimsAlgorithm {

    private static List<List<Pair>> buildGraph(int n, int[][] edges) {
        List<List<Pair>> graph = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for(int[] edge : edges) {
            graph.get(edge[0]).add(new Pair(edge[1], edge[2]));
            graph.get(edge[1]).add(new Pair(edge[0], edge[2]));
        }
        return graph;
    }

    private static int[] minCost(int[][] edges, int n) {
        List<List<Pair>> graph = buildGraph(n, edges);
        PriorityQueue<Pair> minHeap = new PriorityQueue<>((p1, p2) -> p1.distance - p2.distance);

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        int[] parent = new int[n];
        boolean[] mstSet = new boolean[n];

        distance[0] = 0;
        parent[0] = -1;
        minHeap.offer(new Pair(0, 0));

        while(!minHeap.isEmpty()) {
            Pair pair = minHeap.poll();
            int currNode = pair.node;

            if(mstSet[currNode]) continue;
            mstSet[currNode] = true;

            for(Pair nbrPair : graph.get(currNode)) {
                if(mstSet[nbrPair.node] == false && nbrPair.distance < distance[nbrPair.node]) {
                    distance[nbrPair.node] = nbrPair.distance;
                    parent[nbrPair.node] = currNode;
                    minHeap.offer(new Pair(nbrPair.node, nbrPair.distance));
                }
            }
        }

        int cost = 0;
        for(int d : distance) {
            cost += d;
        }

        return parent;
    }
    public static void main(String[] args) {
        int[][] edges = new int[][] {
            {0, 1, 4}, {0, 7, 8}, 
            {1, 2, 8}, {1, 7, 11},
            {2, 3, 7}, {2, 5, 4}, {2, 8, 2}, 
            {3, 4, 9}, {3, 5, 14},
            {4, 5, 10},
            {5, 6, 2},
            {6, 7, 1}, {6, 8, 6},
            {7, 8, 7}
        }; 
        int n = 9;
        int parent[] = PrimsAlgorithm.minCost(edges, n);   
        for(int i = 0; i < n; i++) {
            System.out.println(parent[i] + " ---> " + i);
        }
    }
}
