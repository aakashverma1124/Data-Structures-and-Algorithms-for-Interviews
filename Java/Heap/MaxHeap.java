import java.util.*;

class Innoskrit {

    static List<Integer> maxHeap = new ArrayList<>();

    public static void swap(int index, int largestIndex) {
        int temp = maxHeap.get(index);
        maxHeap.set(index, maxHeap.get(largestIndex));
        maxHeap.set(largestIndex, temp);
    }

    public static void heapify(int index) {
        int size = maxHeap.size();
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        
        int largestIndex = index;

        if(left < size && maxHeap.get(left) > maxHeap.get(largestIndex)) {
            largestIndex = left;
        }
        if(right < size && maxHeap.get(right) > maxHeap.get(largestIndex)) {
            largestIndex = right;
        }

        if(largestIndex != index) {
            swap(index, largestIndex);
            heapify(largestIndex);
        }
    }

    public static void insert(int data) {
        maxHeap.add(data);
        int size = maxHeap.size();
        int index = size - 1;
        int parent = (index-1)/2;
        while(parent >= 0 && maxHeap.get(index) > maxHeap.get(parent)) {
            swap(index, parent);
            index = parent;
            parent = (index-1)/2;
        }
    }

    public static int delete() {
        int size = maxHeap.size();
        if(size == 0)
            return -1;
        int element = maxHeap.get(0);
        maxHeap.set(0, maxHeap.get(size - 1));
        maxHeap.remove(size - 1);
        heapify(0);
        return element;
    }
    
    public static void printHeap() {
        System.out.println(maxHeap);
    }

    public static void main(String[] args) {
        Innoskrit.insert(98);
        Innoskrit.insert(87);
        Innoskrit.insert(86);
        Innoskrit.insert(44);
        Innoskrit.insert(40);
        Innoskrit.insert(32);
        Innoskrit.insert(33);
        Innoskrit.insert(20);
        Innoskrit.insert(21);
        System.out.println(Innoskrit.delete());
        Innoskrit.printHeap();
        Innoskrit.insert(100);
        Innoskrit.printHeap();
    }
}