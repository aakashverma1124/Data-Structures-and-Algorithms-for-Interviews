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

class DijkstrasAlgorithm {

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

    private static int[] shortestPath(int n, int[][] edges, int src) {
        List<List<Pair>> graph = buildGraph(n, edges);
        PriorityQueue<Pair> minHeap = new PriorityQueue<>((p1, p2) -> p1.distance - p2.distance);

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        boolean[] visited = new boolean[n];

        distance[src] = 0;
        minHeap.offer(new Pair(src, distance[src]));

        while(!minHeap.isEmpty()) {
            Pair currPair = minHeap.poll();
            int currNode = currPair.node;
            int currDistance = currPair.distance;

            if(visited[currNode]) continue;
            visited[currNode] = true;

            for(Pair nbrPair : graph.get(currNode)) {
                int newDistance = currDistance + nbrPair.distance;
                if(newDistance < distance[nbrPair.node]) {
                    minHeap.offer(new Pair(nbrPair.node, newDistance));
                    distance[nbrPair.node] = newDistance;
                }
            }
        }
        return distance;

    }
    public static void main(String[] args) {
        int[][] edges = new int[][]{{0, 1, 4} ,{0, 3, 5}, {0, 4, 2}, {1, 2, 4}, {1, 3, 2}, {2, 3, 2}, {3, 4, 1}};
        int n = 5;
        int src = 0;
        int ans[] = DijkstrasAlgorithm.shortestPath(n, edges, src);
        for(int a : ans) {
            System.out.print(a + " ");
        }

    }
}