class Queue:

    def __init__(self):
        self.__queue = [];

    def isEmpty(self):
        return self.__queue == [];

    def enqueue(self, data):
        self.__queue.append(data);

    def dequeue(self):
        data = self.__queue[0];
        del self.__queue[0];
        return data;

    def peek(self):
        return self.__queue[0];

    def sizeQueue(self):
        return len(self.__queue);


# ----

queue = Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);

print(queue.sizeQueue());
print("Dequeue %s" % queue.dequeue());
print("Dequeue %s" % queue.dequeue());
print(queue.sizeQueue());
print(queue.peek());
