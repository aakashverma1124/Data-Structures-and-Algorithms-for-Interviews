/*
	@author
	Aakash.Verma

	Problem:
	The stock span problem is a financial problem where we have a series of
	n daily price quotes for a stock and we need to calculate span of stock’s 
	price for all n days.
	The span Si of the stock’s price on a given day i is defined as the maximum 
	number of consecutive days just before the given day, for which the price 
	of the stock on the current day is less than or equal to its price on the 
	given day.
*/

import java.util.*;

class StockSpan {

	public static ArrayList<Integer> getSpanArray(int arr[]) {

		ArrayList<Integer> ans = new ArrayList<>();
		
		/* Creating Stack to put span & price */
		Stack<Integer> prices = new Stack<>();
		Stack<Integer> span = new Stack<>();
		prices.push(arr[0]);
		span.push(1);
		ans.add(1);

		for(int i = 1; i < arr.length; i++) {
			int count = 1;
			while(!prices.empty() && prices.peek() < arr[i]) {
				count += span.peek();
				prices.pop();
				span.pop();
			}
			span.push(count);
			prices.push(arr[i]); 
			ans.add(count);
		}
		return ans;
	}

	public static void main(String[] args) {
		int arr[] = {10, 4, 5, 90, 120, 80};
		ArrayList<Integer> ans = getSpanArray(arr);
		System.out.println(ans.toString());
	}
}