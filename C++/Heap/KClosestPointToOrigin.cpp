/**
 * 
 * @author
 * aakash.verma
 * 
 * Instagram: https://www.instagram.com/aakashverma1102/
 * LinkedIn: https://www.linkedin.com/in/aakashverma1124/
 * 
 */

#include<bits/stdc++.h>
using namespace std;
class Point {
public:
    int x;
    int y;
    int d;
    Point(int x, int y, int d) {
        this->x = x;
        this->y = y;
        this->d = d;
    }
};

struct comparator {
    bool operator() (Point &a, Point &b) {
        return (b.d > a.d);
    }
};

class KClosestPointToOrigin {
public:

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<Point, vector<Point>, comparator> maxHeap;

        for(vector<int> point : points) {
            int x = point[0];
            int y = point[1];
            int dist = (x * x) + (y * y);
            maxHeap.push(Point(x, y, distance););
            if(maxHeap.size() > k) {
                maxHeap.pop();
            }
        }

        vector<vector<int>> ans(k,{0, 0});
        int i = 0;
        while(!maxHeap.empty()) {
            Point p = maxHeap.top();
            maxHeap.pop();
            ans[i][0] = p.x;
            ans[i][1] = p.y;
            i += 1;
        }
        return ans;

    }
};