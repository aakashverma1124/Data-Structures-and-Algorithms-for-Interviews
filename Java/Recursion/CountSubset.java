class CountSubset {

    public static int solve(int arr[], int target, int n) {
        if(target == 0) return 1;
        if(n == 0) return 0;

        if(arr[n - 1] > target) {
            return solve(arr, target, n - 1);
        }

        return solve(arr, target - arr[n - 1], n - 1) + solve(arr, target, n - 1);

    }

    public static int countSubset(int arr[], int target) {
        return solve(arr, target, arr.length);
    }
    public static void main(String[] args) {
        int arr[] = new int[]{1, 4, 6, 3, 9, 2};
        int target = 12;
        System.out.println(CountSubset.countSubset(arr, target));
    }
}