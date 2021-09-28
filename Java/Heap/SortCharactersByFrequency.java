/**
 * 
 * @author
 * aakash.verma
 * 
 * Instagram: https://www.instagram.com/aakashverma1102/
 * LinkedIn: https://www.linkedin.com/in/aakashverma1124/
 * 
 */

import java.util.*;

class SortCharactersByFrequency {

	public static String sortCharactersByFrequency(String s) {
		HashMap<Character, Integer> frequencyMap = new HashMap<>();
		for(char ch : s.toCharArray()) {
			frequencyMap.put(ch, frequencyMap.getOrDefault(ch, 0) + 1);
		}

		PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
		for(Map.Entry<Character, Integer> entry : frequencyMap.entrySet()) {
			maxHeap.offer(entry);
		}
		StringBuilder sortedString = new StringBuilder();
		while(!maxHeap.isEmpty()) {
			Map.Entry<Character, Integer> entry = maxHeap.poll();
			for(int i = 0; i < entry.getValue(); i++) {
				sortedString.append(entry.getKey());
			}
		} 
		return sortedString.toString();
	}

	public static void main(String[] args) {
		String result = SortCharactersByFrequency.sortCharactersByFrequency("tree");
		System.out.println(result);
	}
	
}