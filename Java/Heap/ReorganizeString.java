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

class Solution {
    public String reorganizeString(String string) {
        
        Map<Character, Integer> map = new HashMap<>();
        for(char ch : string.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<Map.Entry<Character, Integer>>((e1, e2) -> e2.getValue() - e1.getValue());
    
        maxHeap.addAll(map.entrySet());
        
        Map.Entry<Character, Integer> first = null;
        StringBuilder ans = new StringBuilder("");
        while(!maxHeap.isEmpty()) {   
            Map.Entry<Character, Integer> second = maxHeap.poll();
            if(first != null && first.getValue() > 0) {
                maxHeap.offer(first);
            }
            ans.append(second.getKey());
            second.setValue(second.getValue() - 1);
            first = second;
        }
        
        if(ans.length() == string.length()) {
            return ans.toString();
        }
        else {
            return "";
        } 
    }
}