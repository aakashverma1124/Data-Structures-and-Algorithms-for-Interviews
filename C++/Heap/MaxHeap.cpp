#include <bits/stdc++.h>
using namespace std;

class Innoskrit {
public:

    vector<int> maxHeap;
    
    void swap(int index, int largestIndex) {
        int temp = maxHeap[index];
        maxHeap[index] = maxHeap[largestIndex];
        maxHeap[largestIndex] = temp;
    }

    void heapify(int index) {
        int size = maxHeap.size();
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        
        int largestIndex = index;

        if(left < size && maxHeap[left] > maxHeap[largestIndex]) {
            largestIndex = left;
        }
        if(right < size && maxHeap[right] > maxHeap[largestIndex]) {
            largestIndex = right;
        }

        if(largestIndex != index) {
            swap(index, largestIndex);
            heapify(largestIndex);
        }
    }

    void insert(int data) {
        maxHeap.push_back(data);
        int size = maxHeap.size();
        int index = size - 1;
        int parent = (index - 1)/2;
        while(parent >= 0 && maxHeap[index] > maxHeap[parent]) {
            swap(index, parent);
            index = parent;
            parent = (index - 1)/2;
        }
    }

    int deleteElement() {
        int size = maxHeap.size();
        if(size == 0)
            return -1;
        int element = maxHeap[0];
        maxHeap[0] = maxHeap[size - 1];
        maxHeap.pop_back();
        heapify(0);
        return element;
    }
    
    void printHeap() {
        cout << "[";
        for(int i = 0; i < maxHeap.size(); i++) {
            cout << maxHeap[i];
            if(i != maxHeap.size() - 1) {
                cout << ", ";
            }
        }
            
        cout << "]" << endl;
    }
    
};

int main() {
    Innoskrit obj;
    obj.insert(98);
    obj.insert(87);
    obj.insert(86);
    obj.insert(44);
    obj.insert(40);
    obj.insert(32);
    obj.insert(33);
    obj.insert(20);
    obj.insert(21);
    cout << obj.deleteElement() << endl;
    obj.printHeap();
    obj.insert(100);
    obj.printHeap();
} 