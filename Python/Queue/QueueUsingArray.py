# @author
# Aakash.Verma

# Queue is a FIFO/LILO data structures:
# FIFO stands for First In First Out 

# We can't access any element except front. Front is that element which has been inserted at first
# and will be retrieved first. Rear is that element which is inserted at last and will be deleted 
# at last.

# I am assuming that you are here after going through the theory of Queue and looking for implementation.

# Output: 

# Enqueue Operation Done, rear is at  11
# Enqueue Operation Done, rear is at  12
# Enqueue Operation Done, rear is at  13
# Deleted Element is:  11
# Front element is:  12

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
            print("Enqueue Operation Done, rear is at ", element)

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

    def peek(self):
    	if(self.isEmpty()):
    		print("Queue is empty")
    		return -1
    	else :
    		return self.queue[self.front]


if __name__ == '__main__':

    q = QueueUsingArray()
    q.enQueue(11)
    q.enQueue(12)
    q.enQueue(13)
	deleted = q.dequeue()
	print("Deleted Element is: ", deleted)
	print("Front element is: ", q.peek())



