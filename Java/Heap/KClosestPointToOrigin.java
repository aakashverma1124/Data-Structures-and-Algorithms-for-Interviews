import java.util.*;

class Point {
    int x;
    int y;
    int d;
    public Point(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }
}

class KClosestPointToOrigin {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> maxHeap = new PriorityQueue<>((p1, p2) -> p2.d - p1.d);
        for(int point[] : points) {
            int x = point[0];
            int y = point[1];
            int dist = (x * x) + (y * y);
            Point p = new Point(x, y, dist);
            maxHeap.offer(point);
            if(maxHeap.size() > k) {
                maxHeap.poll();
            }
        }
        
        int ans[][] = new int[k][2];
        int i = 0;
        while(!maxHeap.isEmpty()) {
            Point p = maxHeap.poll();
            ans[i][0] = p.x;
            ans[i][1] = p.y;
            i += 1;
        }
        return ans;
    }
}