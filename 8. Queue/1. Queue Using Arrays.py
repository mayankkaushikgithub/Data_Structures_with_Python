


class QueueUsingArray:

    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enQueue(self, data):
        self.__arr.append(data)         # enqueue the data at end
        self.__count += 1               # count no. of elements

    def deQueue(self):
        if self.__count == 0:           # if nothing is present in Queue
            return -1                   # you can't remove anything
        element = self.__arr[self.__front]  # store front element as element to be deleted is at front FIFO
        self.__front += 1               # shift the current front ptr to next ele
        self.__count -= 1
        return element              # this is the dequeued/deleted element

    def front(self):
        if self.__count == 0:
            return -1               # if no element is present in queue
        return self.__arr[self.__front]     # else return the first element

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0         # size() to check size of queue(list)

q = QueueUsingArray()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)


while (q.isEmpty() is False):       # traverse till the end
    print(q.front())                # print ele at front
    q.deQueue()                     # remove using FIFO

print(q.deQueue())                         # print -1 as no ele is present in Queue now we dequed them