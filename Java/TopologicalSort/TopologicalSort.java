/*
*   @author
*   Aakash Verma
*
*   Output:
*   5 6 3 4 0 2 1 
*
*/

import java.util.*;

class TopologicalSort {

	public static List<Integer> topologicalSort(int edges[][], int vertices) {
		List<Integer> sortedOrder = new ArrayList<>();
		if(vertices < 0) {
			return sortedOrder;
		}

		HashMap<Integer, Integer> inDegree = new HashMap<>();
		HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();

		// intializing the graph
		for(int i = 0; i < vertices; i++) {
			inDegree.put(i, 0);
			graph.put(i, new ArrayList<>());
		}

		// building the graph
		for(int i = 0; i < edges.length; i++) {
			int parent = edges[i][0];
			int child = edges[i][1];
			graph.get(parent).add(child);
			inDegree.put(child, inDegree.get(child) + 1);
		}

		// processing all valid starting nodes
		Queue<Integer> queue = new LinkedList<>();
		for(Map.Entry<Integer, Integer> entry : inDegree.entrySet()) {
			if(entry.getValue() == 0) {
				queue.offer(entry.getKey());
			}
		}

		while(!queue.isEmpty()) {
			int vertex = queue.poll();
			sortedOrder.add(vertex);
			List<Integer> children = graph.get(vertex);
			for(int child : children) {
				inDegree.put(child, inDegree.get(child) - 1);
				if(inDegree.get(child) == 0) {
					queue.offer(child);
				}
			}
		}

		if(sortedOrder.size() != vertices) {
			return new ArrayList<>();
		}

		return sortedOrder;

	}

	public static void main(String[] args) {
		int edges[][] = new int[][] {{6, 4}, {6, 2}, {5, 3}, {5, 4}, {3, 0}, {3, 1}, {3, 2}, {4, 1}};
		List<Integer> ans = topologicalSort(edges, 7);
		for(int a : ans) {
			System.out.print(a + " ");
		}
	}
}