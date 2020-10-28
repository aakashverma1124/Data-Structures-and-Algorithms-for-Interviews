# @author
# Aakash.Verma

# Queue is a FIFO/LILO data structures:
# FIFO stands for First In First Out 

# We can't access any element except front. Front is that element which has been inserted at first
# and will be retrieved first. Rear is that element which is inserted at last and will be deleted 
# at last.

# I am assuming that you are here after going through the theory of Queue and looking for implementation.

# Output: 	
# Queue is empty
# Inserted 1
# Inserted 2
# Inserted 3
# Inserted 4
# Inserted 5
# Front points to: 0
# Items in Queue: 1 2 3 4 5
# Rear points to: 4
# Deleted Element is 1
# Front points to: 1
# Items in Queue: 2 3 4 5
# Rear points to: 4
# Inserted 7
# Front points to: 1
# Items in Queue: 2 3 4 5 7
# Rear points to: 5

# Run using: python3 QueueUsingArray.py

class QueueUsingArray:
    # We are assuming that the size of our queue is 10, you may take any size
    SIZE = 10

    queue = []  # queue

    # As soon as the object of this class is created, front & rear is assigned as -1.
    def __init__(self):
        self.front = -1
        self.rear = -1

    # It checks whether the queue is empty or not, obviously if front is -1, the queue will be empty.
    def isEmpty(self):
        if (self.front == -1):
            return True
        return False

    # It checks whether the queue is full or not, for better explanation watch the video on YouTube (Innoskrit)
    def isFull(self):
        if (self.front == 0 and self.rear == self.SIZE - 1):
            return True
        if (self.front == self.rear + 1):
            return True
        return False

    def enQueue(self, element):
        if (self.isFull()):
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.SIZE
            self.queue.append(element)
            print("Inserted ", element)

    def deQueue(self):
        if (self.isEmpty()):
            print("Queue is empty")
            return -1
        else:
            element = self.queue[self.front]

            if (self.front == self.rear):
                self.front = -1
                self.rear = -1
            # Q has only one element, so we reset the queue after deleting it.

            else:
                self.front = (self.front + 1) % self.SIZE
            return element

    def display(self):
        if (self.isEmpty()):
            print("Empty Queue")
        else:
            print("Front points to: ", self.front)
            print("Items in Queue: ", end=" ")
            i = self.front
            while(i != self.rear):
                print(self.queue[i], end=" ")
                i = (i + 1) % self.SIZE
            print(self.queue[i])
            print("Rear points to: ", self.rear)


if __name__ == '__main__':

    q = QueueUsingArray()
    q.deQueue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)
    q.enQueue(5)

    q.display()

    item = q.deQueue()

    if (item != -1):
        print("Deleted Element is ", item)
    q.display()
    q.enQueue(7)
    q.display()



