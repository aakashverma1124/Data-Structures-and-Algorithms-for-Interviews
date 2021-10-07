import java.util.*;

class Point {
    int x;
    int y;
    int distance;
    public Point(int x, int y, int distance) {
        this.x = x;
        this.y = y;
        this.distance = distance;
    }
}

class KClosestPointToOrigin {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> maxHeap = new PriorityQueue<>((p1, p2) -> p2.distance - p1.distance);
        for(int i = 0; i < k; i++) {
            int x = points[i][0];
            int y = points[i][1];
            int distance = x*x + y*y;
            Point p = new Point(x, y, distance);
            maxHeap.add(p);
        }
        
        for(int i = k; i < points.length; i++) {
            int x = points[i][0];
            int y = points[i][1];
            int distance = x*x + y*y;
            if(distance < maxHeap.peek().distance) {
                maxHeap.poll();
                maxHeap.add(new Point(x, y, distance));
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