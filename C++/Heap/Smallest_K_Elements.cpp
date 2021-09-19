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

class Smallest_K_Elements {
public:

    static vector<int> findKSmallestNumbers(const vector<int> &nums, int k) {
        priority_queue<int, vector<int>> maxHeap;

        for(int i = 0; i < k; i++) {
            maxHeap.push(nums[i]);
        }

        for(int i = k; i < nums.size(); i++) {
            if(nums[i] < maxHeap.top()) {
                maxHeap.pop();
                maxHeap.push(nums[i]);
            }
        }
        vector<int> answer(k);
        for (int i = 0; i < k; i++) {
            answer[i] = maxHeap.top();
            maxHeap.pop();
        }
        return answer;
    }
};

int main(int argc, char const *argv[]) {
    vector<int> result = Smallest_K_Elements::findKSmallestNumbers(vector<int>{3, 1, 5, 12, 2, 11}, 3);
    for(auto num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
