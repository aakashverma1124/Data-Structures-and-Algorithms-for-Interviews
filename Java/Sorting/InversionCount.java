/*
*   @author
*   Aakash Verma
*
*   Output:
*   10
*
*/

class InversionCount {

    static int inversion_count = 0;
    public static void merge(int arr[], int low, int mid, int high) {
        int temp[] = new int[high - low + 1];
        int i = low;
        int j = mid + 1;
        int k = 0;
        while(i <= mid && j <= high) {
            if(arr[i] <= arr[j]) {
                temp[k] = arr[i];
                i += 1;
            }
            else {
                temp[k] = arr[j];
                j += 1;
                inversion_count += (mid - i + 1);
            }
            k += 1;
        }
        while(i <= mid) {
            temp[k] = arr[i];
            i += 1;
            k += 1;
        }
        while(j <= high) {
            temp[k] = arr[j];
            j += 1;
            k += 1;
        }
        for(int p = low; p <= high; p++) {
            arr[p] = temp[p - low];
        }
    }
    
    public static void mergeSort(int arr[], int low, int high) {
        if(low < high) {
            int mid = low + (high - low)/2;
            mergeSort(arr, low, mid);
            mergeSort(arr, mid + 1, high);
            merge(arr, low, mid, high);
        }
    }
    public static void main (String[] args) {
        int arr[] = {5, 4, 3, 2, 1};
        int n = 5;
        mergeSort(arr, 0, n - 1);
        System.out.println(inversion_count);
    }
}