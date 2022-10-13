#include <bits/stdc++.h>
using namespace std;

class Innoskrit {
public:
    static vector<vector<int>> intervalIntersection(vector<vector<int>>& arr1, vector<vector<int>>& arr2) {
        int i = 0, j = 0;
        vector<vector<int>> ans;
        
        while(i < arr1.size() && j < arr2.size()) {
            vector<int> intersection;
            intersection.push_back(max(arr1[i][0], arr2[j][0]));
            intersection.push_back(min(arr1[i][1], arr2[j][1]));
            
            if(intersection[0] <= intersection[1]) {
                ans.push_back(intersection);
            }
            
            if(arr1[i][1] < arr2[j][1]) {
                i += 1;
            } else {
                j += 1;
            }
        }
        return ans;
    }
};

int main() {
    vector<vector<int>> arr1 = {{1, 3}, {5, 6}, {7, 9}};
    vector<vector<int>> arr2 = {{2, 3}, {5, 7}};
    for (auto interval : Innoskrit::intervalIntersection(arr1, arr2)) {
        cout << "[" << interval[0] << ", " << interval[1] << "] ";
    }
    cout << endl;
} 