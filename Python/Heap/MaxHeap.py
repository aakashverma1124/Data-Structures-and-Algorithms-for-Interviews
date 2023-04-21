class Innoskrit:

    maxHeap = []

    def swap(index, largestIndex):
        temp = Innoskrit.maxHeap[index]
        Innoskrit.maxHeap[index] = Innoskrit.maxHeap[largestIndex]
        Innoskrit.maxHeap[largestIndex] = temp

    def heapify(index):
        size = len(Innoskrit.maxHeap)
        left = 2 * index + 1
        right = 2 * index + 2
        
        largestIndex = index

        if left < size and Innoskrit.maxHeap[left] > Innoskrit.maxHeap[largestIndex]:
            largestIndex = left

        if right < size and Innoskrit.maxHeap[right] > Innoskrit.maxHeap[largestIndex]:
            largestIndex = right

        if largestIndex != index:
            Innoskrit.swap(index, largestIndex)
            Innoskrit.heapify(largestIndex)

    def insert(data):
        Innoskrit.maxHeap.append(data)
        size = len(Innoskrit.maxHeap)
        index = size - 1
        parent = (index - 1)//2
        while parent >= 0 and Innoskrit.maxHeap[index] > Innoskrit.maxHeap[parent]:
            Innoskrit.swap(index, parent)
            index = parent
            parent = (index - 1)//2

    def delete():
        size = len(Innoskrit.maxHeap)
        if size == 0:
            return -1
        element = Innoskrit.maxHeap[0]
        Innoskrit.maxHeap[0] = Innoskrit.maxHeap[size - 1]
        Innoskrit.maxHeap.pop()
        Innoskrit.heapify(0)
        return element
    
    def printHeap():
        print(Innoskrit.maxHeap)

if __name__ == "__main__":
    Innoskrit.insert(98)
    Innoskrit.insert(87)
    Innoskrit.insert(86)
    Innoskrit.insert(44)
    Innoskrit.insert(40)
    Innoskrit.insert(32)
    Innoskrit.insert(33)
    Innoskrit.insert(20)
    Innoskrit.insert(21)
    print(Innoskrit.delete())
    Innoskrit.printHeap()
    Innoskrit.insert(100)
    Innoskrit.printHeap()