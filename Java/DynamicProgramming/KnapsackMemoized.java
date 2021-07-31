import java.io.*;

class MemoizedKnapsack {
    
    public static int knapsack(int W, int wt[], int val[], int n, int dp[][]) {
        
        if(n == 0 || W == 0) {
            return 0;
        }
        if(dp[n][W] != -1) {
            return dp[n][W];
        }
        if(wt[n - 1] > W) {
            return dp[n][W] = knapsack(W, wt, val, n - 1, dp);
        }
        return dp[n][W] = Math.max(val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1, dp), knapsack(W, wt, val, n -1, dp));
    }
	public static void main (String[] args) {
        int n = 4;
        int wt[] = {1, 3, 1, 2};
        int val[] = {10, 5, 30, 20};
        int W = 2;
        int dp[][] = new int[n + 1][W + 1];
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= W; j++) {
                dp[i][j] = -1;
            }
        }
        int profit = knapsack(W, wt, val, n, dp);
        System.out.println(profit);
	}
}