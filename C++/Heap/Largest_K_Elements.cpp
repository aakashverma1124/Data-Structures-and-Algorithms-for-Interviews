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

class Largest_K_Elements {
public:

    static vector<int> findKLargestNumbers(const vector<int> &nums, int k) {
        priority_queue<int, vector<int>, greater<>> minHeap;

        for(int i = 0; i < k; i++) {
            minHeap.push(nums[i]);
        }

        for(int i = k; i < nums.size(); i++) {
            if(nums[i] > minHeap.top()) {
                minHeap.pop();
                minHeap.push(nums[i]);
            }
        }
        vector<int> answer(k);
        for (int i = 0; i < k; i++) {
            answer[i] = minHeap.top();
            minHeap.pop();
        }
        return answer;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> result = Largest_K_Elements::findKLargestNumbers(vector<int>{3, 1, 5, 12, 2, 11}, 3);
    for(auto num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
