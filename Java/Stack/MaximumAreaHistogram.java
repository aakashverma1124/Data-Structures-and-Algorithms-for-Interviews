/*
# @author
# Aakash.Verma

# Problem: Find the largest rectangular area possible in a given histogram where the largest 
# rectangle can be made of a number of contiguous bars. For simplicity, assume that 
# all bars have same width and the width is 1 unit.

# For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}.
# The largest possible rectangle possible is 12.
*/

import java.util.*;


class MaximumAreaHistogram {

	public static ArrayList<Integer> nsel(int arr[], int n) {
		ArrayList<Integer> nselIndex = new ArrayList<>();
		Stack<ArrayList<Integer>> s = new Stack<>();

		for(int i = 0; i < n; i++) {
		    while(!s.empty() && s.peek().get(0) >= arr[i]) {
    			s.pop();
    		}
    		if(s.empty()) {
    		    nselIndex.add(-1);
    		}
    		else  {
    		    nselIndex.add(s.peek().get(1));
    		}

    		ArrayList<Integer> tempList = new ArrayList<>();
    		tempList.add(arr[i]);
    		tempList.add(i);
			s.push(tempList);
		}
		System.out.println(nselIndex.toString());
		return nselIndex;
	}

	public static ArrayList<Integer> nser(int arr[], int n) {
		ArrayList<Integer> nserIndex = new ArrayList<>();
		Stack<ArrayList<Integer>> s = new Stack<>();

		for(int i = n - 1; i >= 0; i--) {
		    while(!s.empty() && s.peek().get(0) >= arr[i]) {
    			s.pop();
    		}
    		if(s.empty()) {
    		    nserIndex.add(n);
    		}
    		else  {
    		    nserIndex.add(s.peek().get(1));
    		}

    		ArrayList<Integer> tempList = new ArrayList<>();
    		tempList.add(arr[i]);
    		tempList.add(i);
			s.push(tempList);
		}
		Collections.reverse(nserIndex);
		System.out.println(nserIndex.toString());
		return nserIndex;
	}

	public static int maxAreaHistogram(int arr[], int n) {
		ArrayList<Integer> nsel = nsel(arr, n);
		ArrayList<Integer> nser = nser(arr, n);
		ArrayList<Integer> ans = new ArrayList<>();
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < n; i++) {
			ans.add((nser.get(i) - nsel.get(i) - 1) * arr[i]);
			if(max < ans.get(i)) {
				max = ans.get(i);
			}
		}
		return max;
	}

	public static void main(String[] args) {

		int arr[] = {6, 2, 5, 4, 5, 1, 6};
		int ans = maxAreaHistogram(arr, arr.length);
		System.out.println(ans);


		
	}
}