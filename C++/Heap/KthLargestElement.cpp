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

class KthLargestElement {
public:

    static int findKthLargestNumber(const vector<int> &nums, int k) {
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
        return minHeap.top();
    }
};

int main(int argc, char const *argv[])
{
    int result = KthLargestElement::findKthLargestNumber(vector<int>{3, 1, 5, 12, 2, 11}, 3);
    cout << result;
    return 0;
}
