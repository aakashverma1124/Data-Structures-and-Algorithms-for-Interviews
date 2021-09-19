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

class KthLargestElement {

	public static int findKthLargestNumber(int[] nums, int k) {
		PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> a - b);
		for(int i = 0; i < k; i++) {
			minHeap.add(nums[i]);
		}

		for(int i = k; i < nums.length; i++) {
			if(nums[i] > minHeap.peek()) {
				minHeap.poll();
				minHeap.add(nums[i]);
			}
		}
		return minHeap.peek();
	}

	public static void main(String[] args) {
		int result = KthLargestElement.findKthLargestNumber(new int[] {3, 1, 5, 12, 2, 11}, 3);
		System.out.println(result);
	}
	
}