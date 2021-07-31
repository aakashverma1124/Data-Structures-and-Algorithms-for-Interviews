import java.io.*;

class KnapsackTabulation {
    
    public static int knapsack(int W, int wt[], int val[], int n) {
        int dp[][] = new int[n + 1][W + 1];
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= W; j++) {
                if(i == 0 || j == 0) {
                    dp[i][j] = 0;
                }
                else if(wt[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j];
                }
                else {
                    dp[i][j] = Math.max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]]);
                }
            }
        }
        return dp[n][W];

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