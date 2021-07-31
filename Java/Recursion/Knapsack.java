import java.io.*;

class Knapsack {
    
    public static int knapsack(int W, int wt[], int val[], int n) {
        if(n == 0 || W == 0) {
            return 0;
        }
        if(wt[n - 1] > W) {
            return knapsack(W, wt, val, n - 1);
        }
        return Math.max(val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1), knapsack(W, wt, val, n -1));
    }
	public static void main (String[] args) {
        int n = 4;
        int wt[] = {1, 3, 1, 2};
        int val[] = {10, 5, 30, 20};
        int W = 2;
        int profit = knapsack(W, wt, val, n);
        System.out.println(profit);
	}
}