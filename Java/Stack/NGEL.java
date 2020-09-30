/*
	@author
	Aakash.Verma

	Problem: Given an array, print the Next Greater Element (NGE) for every element.
			 The Next Greater Element for an element x is the first greater element 
			 on the left side of x in array. Elements for which no greater element exist, 
			 consider next greater element as -1.
*/

import java.util.*; 

class NGEL {

	public static ArrayList<Integer> nextGreaterElementToLeft(int arr[], int n) {
		ArrayList<Integer> v = new ArrayList<>();
		Stack<Integer> s = new Stack<>();

		s.push(arr[0]);
		v.add(-1);

		for(int i = 1; i < n; i++) {

			if(s.size() == 0) {
				v.add(-1);
			}
			else if(s.peek() > arr[i]) {
			    v.add(s.peek());
			    s.push(arr[i]);
			}
			else {
			    while(!s.empty() && s.peek() < arr[i]) {
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
		}
		return v;
	}

	public static void main(String[] args) {
		
		int arr[] = {7, 8, 1, 4}; 
		ArrayList<Integer> ans = nextGreaterElementToLeft(arr, arr.length); 
		System.out.println(ans.toString());

	}
}