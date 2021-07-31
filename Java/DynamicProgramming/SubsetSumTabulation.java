import java.io.*;

class SubsetSum {
    
    public static boolean subsetSum(int sum, int arr[], int n) {
        boolean dp[][] = new boolean[n + 1][sum + 1];
        for(int i = 0; i <= sum; i++) {
            dp[0][i] = false;
        }
        for(int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= sum; j++) {
                if(arr[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j];
                }
                else {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
                }
            }
        }
        return dp[n][sum];

    }
    public static void main (String[] args) {
        int n = 5;
        int arr[] = {6, 19, 4, 10, 1};
        int sum = 11;
        boolean ans = subsetSum(sum, arr, n);
        System.out.println(ans);
    }
}