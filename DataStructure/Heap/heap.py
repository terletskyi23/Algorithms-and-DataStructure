CAPACITY = 20

class Heap(object):

    def __init__(self):
        # init an array with capacity
        self.__heap = [0] * CAPACITY

        self.__heap_size = 0


    def insert(self, item):
        print("Inserting item %s" % item)

        if self.__heap_size == CAPACITY:
            print("Not enough free space")
            return

        self.__heap[self.__heap_size] = item
        self.__heap_size += 1

        self.__fix_up(self.__heap_size - 1)


    def get_max(self): # can be named peek
        return self.__heap[0]


    def poll(self):
        max = self.get_max()
        print("Removing max %s" % max)

        self.__swap(0, self.__heap_size - 1)
        self.__heap_size -= 1

        self.__fix_down(0)

        return max


    def sort(self):
        size = self.__heap_size

        for i in range(0, size):
            print(self.poll())

    def display(self):
        print(self.__heap)


    def __fix_up(self, index):
        parent_index = (index - 1) // 2

        child = self.__heap[index]
        parent = self.__heap[parent_index]

        if index > 0 and child > parent:
            print("Swap child = %s and parent = %s" % (child, parent))
            self.__swap(index, parent_index)
            self.__fix_up(parent_index)


    def __fix_down(self, index):
        index_largest = index

        index_left = 1 * index + 1
        index_right = 1 * index + 2

        if index_left < self.__heap_size and self.__heap[index_left] > self.__heap[index]:
            index_largest = index_left

        if index_right < self.__heap_size and self.__heap[index_right] > self.__heap[index_largest]:
            index_largest = index_right

        if index != index_largest:
            print("Swap child = %s and parent = %s" % (self.__heap[index_largest], self.__heap[index]))
            self.__swap(index, index_largest)
            self.__fix_down(index_largest)


    def __swap(self, index1, index2):
        self.__heap[index2], self.__heap[index1] = self.__heap[index1], self.__heap[index2]


# ----

heap = Heap()

heap.insert(23)
heap.insert(12)
heap.insert(17)
heap.display()

heap.insert(134)
heap.display()

heap.insert(129)
heap.insert(41)
heap.insert(8)

heap.display()

heap.sort()

heap.insert(121)
heap.insert(9)
heap.insert(61)
heap.insert(2)

heap.poll()
heap.display()
