import java.util.*;

class Innoskrit {
    public int[][] intervalIntersection(int[][] arr1, int[][] arr2) {
        List<int[]> ans = new ArrayList<>();
        
        int i = 0, j = 0;
        
        while(i < arr1.length && j < arr2.length) {
            int intersection[] = new int[2];
            intersection[0] = Math.max(arr1[i][0], arr2[j][0]);
            intersection[1] = Math.min(arr1[i][1], arr2[j][1]);
            
            if(intersection[0] <= intersection[1]) {
                ans.add(intersection);
            }
            
            if(arr1[i][1] < arr2[j][1]) {
                i += 1;
            } else {
                j += 1;
            }
        }
        return ans.toArray(new int[ans.size()][2]);
    }

    public static void main(String[] args) {
        int arr1[][] = new int[][]{{1, 3}, {5, 6}, {7, 9}};
        int arr2[][] = new int[][]{{2, 3}, {5, 7}};
        for (int[] interval : Innoskrit.intervalIntersection(arr1, arr2))
            System.out.print("[" + interval[0] + "," + interval[1] + "] ");
        System.out.println();
    }
}