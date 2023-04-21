import java.io.*;

class Innoskrit {

    public static int countSubset(int arr[], int target) {
        int dp[][] = new int[arr.length + 1][target + 1];
        
        for(int col = 0; col < dp[0].length; col++) {
            dp[0][col] = 0;
        }
        
        for(int row = 0; row < dp.length; row++) {
            dp[row][0] = 1;
        }
        
        for(int i = 1; i < dp.length; i++) {
            for(int j = 1; j < dp[0].length; j++) {
                if(arr[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]];
                }
            }
        }
        return dp[arr.length][target];
    }
    public static void main(String[] args) {
        int arr[] = new int[]{1, 4, 6, 3, 9, 2};
        int target = 12;
        System.out.println(Innoskrit.countSubset(arr, target));
    }
}