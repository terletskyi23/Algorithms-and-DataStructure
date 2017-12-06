class Queue:

    def __init__(self):
        self.queue = [];

    def isEmpty(self):
        return self.queue == [];

    def enqueue(self, data):
        self.queue.append(data);

    def dequeue(self):
        data = self.queue[0];
        del self.queue[0];
        return data;

    def peek(self):
        return self.queue[0];

    def sizeQueue(self):
        return len(self.queue);


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
