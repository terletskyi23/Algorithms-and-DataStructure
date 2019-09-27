# Node
class Node(object):

    def __init__(self, data):
        self.data = data;
        self.nextNode = None;


# LinkedList
class LinkedList(object):

    def __init__(self):
        self.__head = None;
        self.__size = 0;

    # O(1)
    def insertStart(self, data):
        self.__size += 1;
        newNode = Node(data);

        if not self.__head:
            self.__head = newNode;
        else:
            newNode.nextNode = self.__head
            self.__head = newNode

    # O(N)
    def remove(self, data):
        if self.__head is None:
            return;

        self.__size -= 1;

        currentNode = self.__head;
        previousNode = None;

        while currentNode.data != data:
            previousNode = currentNode;
            currentNode = currentNode.nextNode;

        if previousNode is None:
            self.__head = currentNode.nextNode;
        else:
            previousNode.nextNode = currentNode.nextNode;

    # O(1)
    def size1(self):
        return self.__size

    # O(N)
    def size2(self):
        actualNode = self.__head;
        size = 0;

        while actualNode is not None:
            size += 1;
            actualNode = actualNode.nextNode;

        return size;

    # O(N)
    def insertEnd(self, data):
        self.__size += 1;
        newNode = Node(data);
        actualNode = self.__head;

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode;

        actualNode.nextNode = newNode;

    # O(N)
    def traverseList(self):
        actualNode = self.__head;
        while actualNode is not None:
            print("%d " % actualNode.data);
            actualNode = actualNode.nextNode;


# ----

linkedList = LinkedList();
linkedList.insertStart(12);
linkedList.insertStart(124);

linkedList.insertEnd(8);
linkedList.insertEnd(32);

linkedList.traverseList();
print(linkedList.size1());

linkedList.remove(12);
linkedList.remove(32);
linkedList.traverseList();
print(linkedList.size1());
