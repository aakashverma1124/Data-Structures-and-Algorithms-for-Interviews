#include <bits/stdc++.h>
using namespace std;

class Innoskrit {
public:
    static vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int i = 0;
        vector<vector<int>> ans;
        
        while(i < intervals.size() && intervals[i][1] < newInterval[0]) {
            ans.push_back(intervals[i]);
            i += 1;
        }

        while(i < intervals.size() && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i += 1;
        }
        ans.push_back(newInterval);
        
        while(i < intervals.size()) {
            ans.push_back(intervals[i]);
            i += 1;
        }
        
        return ans; 
    }
};

int main() {
    vector<vector<int>> intervals = {{1, 3}, {5, 7}, {8, 12}};
    vector<int> newInterval = {4, 6};
    for (auto interval : Innoskrit::insert(intervals, newInterval)) {
        cout << "[" << interval[0] << "," << interval[1] << "] ";
    }
    cout << endl;
} 