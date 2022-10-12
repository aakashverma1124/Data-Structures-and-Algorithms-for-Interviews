import java.util.*;

class Innoskrit {
    public static int[][] insert(int[][] intervals, int[] newInterval) {
        
        int i = 0;
        List<int[]> ans = new ArrayList<>();
        while(i < intervals.length && intervals[i][1] < newInterval[0]) {
            ans.add(intervals[i]);
            i += 1;
        }
        
        while(i < intervals.length && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i += 1;
        }
        ans.add(newInterval);
        
        while(i < intervals.length) {
            ans.add(intervals[i]);
            i += 1;
        }
        
        return ans.toArray(new int[ans.size()][2]);
    }

    public static void main(String[] args) {
        int intervals[][] = new int[][]{{1, 3}, {5, 7}, {8, 12}};
        int newInterval[] = new int[]{4, 6};
        for (int[] interval : Innoskrit.insert(intervals, newInterval))
            System.out.print("[" + interval[0] + "," + interval[1] + "] ");
        System.out.println();
    }
    
}