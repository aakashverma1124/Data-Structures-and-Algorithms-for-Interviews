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

class KthSmallestElement {
public:

    static int findKthSmallestNumber(const vector<int> &nums, int k) {
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
        return maxHeap.top();
    }
};

int main(int argc, char const *argv[])
{
    int result = KthSmallestElement::findKthSmallestNumber(vector<int>{3, 1, 5, 12, 2, 11}, 3);
    cout << result;
    return 0;
}
