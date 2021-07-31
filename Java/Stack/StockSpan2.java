/*
	@author
	Aakash.Verma

	Problem: The stock span problem is a financial problem where we have a 
	series of n daily price quotes for a stock and we need to calculate span 
	of stock’s price for all n days.
	The span Si of the stock’s price on a given day i is defined as the 
	maximum number of consecutive days just before the given day, for which 
	the price of the stock on the current day is less than or equal to its 
	price on the given day.

	Output: [1, 1, 1, 2, 1, 4, 6] 
*/

import java.util.*; 

class StockSpan {

	public static ArrayList<Integer> stockSpan(int arr[], int n) {
		ArrayList<Integer> v = new ArrayList<>();
		ArrayList<Integer> span = new ArrayList<>();
		Stack<ArrayList<Integer>> s = new Stack<>();

		for(int i = 0; i < n; i++) {
		    while(!s.empty() && s.peek().get(0) <= arr[i]) {
    			s.pop();
    		}
    		if(s.empty()) {
    		    v.add(-1);
    		}
    		else  {
    		    v.add(s.peek().get(1));
    		}

    		ArrayList<Integer> tempList = new ArrayList<>();
    		tempList.add(arr[i]);
    		tempList.add(i);
			s.push(tempList);
		}
		for(int i = 0; i < n; i++) {
			span.add(i - v.get(i));
		}
		return span;
	}

	public static void main(String[] args) {
		
		int arr[] = {100, 80, 60, 70, 60, 75, 85}; 
		ArrayList<Integer> ans = stockSpan(arr, arr.length); 
		System.out.println(ans.toString());

	}
}