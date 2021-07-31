/*
	@author
	Aakash.Verma

	Problem: Given an array, print the Next Smaller Element (NSE) for every element.
			 The Next Smaller Element for an element x is the first smaller element 
			 on the left side of x in array. Elements for which no smaller element exist, 
			 consider next smaller element as -1.
*/

import java.util.*; 

class NSEL {

	public static ArrayList<Integer> nextSmallerElementToLeft(int arr[], int n) {
		ArrayList<Integer> v = new ArrayList<>();
		Stack<Integer> s = new Stack<>();

		for(int i = 0; i < n; i++) {
		    while(!s.empty() && s.peek() >= arr[i]) {
    			s.pop();
    		}
    		if(s.empty()) {
    		    v.add(-1);
    		}
    		else  {
    		    v.add(s.peek());
    		}
			s.push(arr[i]);
		}
		return v;
	}

	public static void main(String[] args) {
		
		int arr[] = {7, 8, 1, 4}; 
		ArrayList<Integer> ans = nextSmallerElementToLeft(arr, arr.length); 
		System.out.println(ans.toString());

	}
}