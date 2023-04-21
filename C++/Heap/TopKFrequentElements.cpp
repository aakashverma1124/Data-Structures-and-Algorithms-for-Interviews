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

class Solution {
public:
    
    struct valueCompare {
        char operator()(pair<int, int> &x, pair<int, int> &y) {
            return y.second < x.second;
        }
    };
    
    string topKFrequentElements(vector<int> v, int k) {
        
        unordered_map<int, int> hash_map;
        for(int a : s) {
            hash_map[a]++;
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, valueCompare> min_heap;
        
        for(auto entry : hash_map) {
            min_heap.push(entry);
            if(min_heap.size() == k + 1) {
                min_heap.pop();
            }
        }
    }
};