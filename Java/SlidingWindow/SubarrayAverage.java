package abes.slidingwindow;

public class AverageSubarray {

    public static double[] averageSubarray(int arr[], int k) {
        double ans[] = new double[arr.length - k + 1];
        int windowStart = 0;
        int windowSum = 0;
        for(int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            windowSum += arr[windowEnd];
            if(windowEnd >= k - 1) {
                ans[windowStart] = (double) windowSum/k;
                windowSum -= arr[windowStart];
                windowStart += 1;
            }
        }
        return ans;
    }

    public static int maxSubarraySum(int arr[], int k) {
        int windowStart = 0;
        int windowSum = 0;
        int maxSum = Integer.MIN_VALUE;
        for(int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            windowSum += arr[windowEnd];
            if(windowEnd >= k - 1) {
                maxSum = Math.max(maxSum, windowSum);
                windowSum -= arr[windowStart];
                windowStart += 1;
            }
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int arr[] = new int[]{1, 2, 3, 4, 5, 6};
        int k = 3;
        double ans[] = AverageSubarray.averageSubarray(arr, k);
        for(double a : ans) {
            System.out.print(a + " ");
        }
        System.out.println();
        int maxSum = AverageSubarray.maxSubarraySum(arr, k);
        System.out.println(maxSum);
    }
}
