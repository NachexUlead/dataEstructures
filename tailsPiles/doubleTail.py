class DoubleQueue:
    def __init__(self, size):
        self.data = [None] * size  # fixed-size list
        self.head1 = 0             # front index of Queue 1
        self.tail1 = 0             # rear index of Queue 1
        self.qty1 = 0              # number of elements in Queue 1
        
        self.head2 = size // 2     # front index of Queue 2
        self.tail2 = size // 2     # rear index of Queue 2
        self.qty2 = 0              # number of elements in Queue 2
        
        self.queueSize = (size // 2) - 1  # maximum size per queue

    def enqueue(self, queueNum, element):
        if queueNum == 1:  # insert into Queue 1
            if self.qty1 > self.queueSize:
                raise Exception("queue 1 is full")
            self.data[self.tail1] = element
            self.tail1 += 1
            self.qty1 += 1
        elif queueNum == 2:  # insert into Queue 2
            if self.qty2 > self.queueSize:
                raise Exception("queue 2 is full")
            self.data[self.tail2] = element
            self.tail2 += 1
            self.qty2 += 1
        else:
            raise ValueError("invalid queue number, must be 1 or 2")

    def dequeue(self, queueNum):
        if queueNum == 1:  # remove from Queue 1
            if self.qty1 == 0:
                raise Exception("queue 1 is empty")
            element = self.data[self.head1]
            self.data[self.head1] = None  # clear space
            self.head1 += 1
            self.qty1 -= 1
            return element
        elif queueNum == 2:  # remove from Queue 2
            if self.qty2 == 0:
                raise Exception("queue 2 is empty")
            element = self.data[self.head2]
            self.data[self.head2] = None  # clear space
            self.head2 += 1
            self.qty2 -= 1
            return element
        else:
            raise ValueError("invalid queue number, must be 1 or 2")

    def __str__(self):
        return f"queue 1: {self.data[:self.tail1]} | queue 2: {self.data[self.head2:self.tail2]}"

queue = DoubleQueue(10)  # total size of the list is 10
queue.enqueue(1, 5)
queue.enqueue(1, 10)
queue.enqueue(2, 99)
queue.enqueue(2, 77)

print(queue)  # displays the current state of both queues

print(queue.dequeue(1))  # removes the first element from Queue 1
print(queue.dequeue(2))  # removes the first element from Queue 2

print(queue)  # displays the state after removals
