/*
*   @author
*   Aakash Verma
*
*/

import java.util.*;
import java.lang.*;
import java.io.*;

class CP01_BinaryTree {

	public static int[] bfs(int n, int source, HashMap<Integer, ArrayList<Integer>> tree) {
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(source);
		int distance[] = new int[n + 1];
		while(!queue.isEmpty()) {
			int current = queue.poll();
			for(int neighbour : tree.get(current)) {
				queue.offer(neighbour);
				distance[neighbour] = distance[current] + 1;
			}
		}
		return distance;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(reader.readLine());
		while(t-- > 0) {
			int n = Integer.parseInt(reader.readLine());
			HashMap<Integer, ArrayList<Integer>> tree = new HashMap<>();
			for(int i = 1; i <= n; i++) {
				tree.put(i, new ArrayList<>());
			}
			for(int i = 0; i < n - 1; i++) {
				String[] st = reader.readLine().trim().split("\\s+");
				int a = Integer.parseInt(st[0]);
				int b = Integer.parseInt(st[1]);
				tree.get(a).add(b);
				tree.put(a, tree.get(a));
			}
			int distance[] = bfs(n, 1, tree);
			for(int i = 1; i <= n; i++) {
				System.out.print(distance[i] + " ");
			}
			System.out.println();
		}
	}
}