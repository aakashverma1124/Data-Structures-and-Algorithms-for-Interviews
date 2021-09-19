import java.util.*;
import java.io.*;

class AlienDictionary {

    public static String alienOrder(String[] words) {
        if(words == null || words.length == 0) {
			return "";
		}

		StringBuilder sortedOrder = new StringBuilder();
		HashMap<Character, Integer> inDegree = new HashMap<>();
		HashMap<Character, ArrayList<Character>> graph = new HashMap<>();

		for(String word : words) {
			for(char ch : word.toCharArray()) {
				inDegree.put(ch, 0);
				graph.put(ch, new ArrayList<>());
			}
		}

		for(int i = 0; i < words.length - 1; i++) {
			String word1 = words[i];
			String word2 = words[i + 1];
            if(word2.length() < word1.length() && word1.startsWith(word2)) {
                return "";
            }
			for(int j = 0; j < Math.min(word1.length(), word2.length()); j++) {
				char parent = word1.charAt(j);
				char child = word2.charAt(j);
				if(parent != child) {
					graph.get(parent).add(child);
                    inDegree.put(child, inDegree.get(child) + 1);
					break;
				}
			}
		}

		// processing all valid starting nodes
		Queue<Character> queue = new LinkedList<>();
		for(Map.Entry<Character, Integer> entry : inDegree.entrySet()) {
			if(entry.getValue() == 0) {
				queue.offer(entry.getKey());
			}
		}

		while(!queue.isEmpty()) {
			char vertex = queue.poll();
			sortedOrder.append(vertex);
			ArrayList<Character> children = graph.get(vertex);
			for(char child : children) {
				inDegree.put(child, inDegree.get(child) - 1);
				if(inDegree.get(child) == 0) {
					queue.offer(child);
				}
			}
		}

		if(sortedOrder.length() != inDegree.size()) {
			return "";
		}

		return sortedOrder.toString();
    }

	public static void main(String[] args) {
		// String words[] = {"ywx", "wz", "xww", "xz", "zyy", "zwz"};
		String words[] = {"zy", "zx"};
		String languageOrder = alienOrder(words);
		System.out.println(languageOrder);
	}
}