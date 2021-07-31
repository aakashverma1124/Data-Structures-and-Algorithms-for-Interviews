import java.io.*;

class SubsetSum {
    
    public static boolean subsetSum(int sum, int arr[], int n) {
        if(sum == 0) {
            return true;
        }
        if(n == 0) {
            return false;
        }
        if(arr[n - 1] > sum) {
            return subsetSum(sum, arr, n - 1);
        }
        return subsetSum(sum - arr[n - 1], arr, n - 1) || subsetSum(sum, arr, n - 1);
    }
	public static void main (String[] args) {
        int n = 5;
        int arr[] = {6, 19, 4, 10, 1};
        int sum = 11;
        boolean ans = subsetSum(sum, arr, n);
        System.out.println(ans);
	}
}