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
        char operator()(pair<char, int> &x, pair<char, int> &y) {
            return y.second > x.second;
        }
    };
    
    string reorganizeString(string s) {
        
        unordered_map<char, int> hash_map;
        for(char ch : s) {
            hash_map[ch]++;
        }
        priority_queue<pair<char, int>, vector<pair<char, int>>, valueCompare> max_heap;
        for(auto entry : hash_map) {
            max_heap.push(entry);
        }
        pair<char, int> prev(-1, -1);
        string res = "";
        while(!max_heap.empty()) {
            pair<char, int> entry = max_heap.top();
            max_heap.pop();
            res += entry.first;
            if(prev.second > 0) {
                max_heap.push(prev);
            }   
            prev = entry;
            prev.second--;
            
        }
        
        if(res.length() == s.length()) {
            return res;
        }
        else {
            return "";
        }
    }
};