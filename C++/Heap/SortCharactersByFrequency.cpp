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

class SortCharactersByFrequency {
public:
    
    struct comparator {
        bool operator() (pair<char, int> &x, pair<char, int> &y) {
            return y.second > x.second;
        }
    };

    static string sortCharactersByFrequency(const string s) {

        unordered_map<char, int> frequencyMap;
        for(char c : s) {
            frequencyMap[c]++;
        }

        priority_queue<pair<char, int>, vector<pair<char, int>>, comparator> maxHeap;

        for(auto entry : frequencyMap) {
            maxHeap.push(entry);
        }

        string sortedString = "";
        while(!maxHeap.empty()) {
            auto entry = maxHeap.top();
            maxHeap.pop();
            for(int i = 0; i < entry.second; i++) {
                sortedString += entry.first;
            }
        }
        return sortedString;
    }
};

int main(int argc, char const *argv[]) {
    string result = SortCharactersByFrequency::sortCharactersByFrequency("tree");
    cout << result;
    return 0;
}
