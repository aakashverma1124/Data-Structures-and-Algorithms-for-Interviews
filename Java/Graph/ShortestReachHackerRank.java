/** 
 * 
 * @author 
 * aakash.verma
 * 
 * Problem Link: https://www.hackerrank.com/challenges/bfsshortreach/problem
 * Note: I have completed the function only.
 * 
 */
 
public static List<Integer> bfs(int n, int m, List<List<Integer>> edges, int s) {
    List<Integer> distance = new ArrayList<>(n + 1);
    Queue<Integer> q = new LinkedList<>();
    boolean visited[] = new boolean[n + 1];
    q.offer(s);
    visited[s] = true;
    distance[]
    distance.set(s, 0);

    @SuppressWarnings("unchecked")
    LinkedList<Integer> adjacencyList[] = new LinkedList[n + 1];
    for(List<Integer> edge : edges) {
        adjacencyList[edge.get(0)].add(edge.get(1));
        adjacencyList[edge.get(1)].add(edge.get(0));
    }

    while(!q.isEmpty()) {
        int curr = q.poll();
        for(int nbr : adjacencyList[curr]) {
            if(visited[nbr] == false) {
                q.offer(nbr);
                visited[nbr] = true;
                distance.set(nbr, distance.get(curr) + 6);
            }
        }
    }
    return distance;
}
