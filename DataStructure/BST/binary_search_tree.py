class Node(object):

    def __init__(self, data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;


class BinarySearchTree:

    def __init__(self):
        self.__root = None;

    # O(logN) if the tree is balanced !!!!!!!!!!! --> it can reduce to O(N) --> AVL RBT are needed !!!
    def __insertNode(self, data, node):
        newNode = Node(data);
        if data < node.data:
            if node.leftChild:
                self.__insertNode(data, node.leftChild);
            else:
                node.leftChild = newNode;
        elif data > node.data:
             if node.rightChild:
                 self.__insertNode(data, node.rightChild);
             else:
                 node.rightChild = newNode;
        else:
            print('already inserted');

    def __getMax(self, node):
        if node.rightChild:
            return self.__getMax(node.rightChild);
        return node.data;

    def __getMin(self, node):
        if node.leftChild:
            return self.__getMin(node.leftChild);
        return node.data;

    def __traverseInOrder(self, node):
        if node.leftChild:
            self.__traverseInOrder(node.leftChild);

        print("%s " % node.data);

        if node.rightChild:
            self.__traverseInOrder(node.rightChild);

    def __removeNode(self, data, node):
        if not node:
            return node;

        if data < node.data:
            node.leftChild = self.__removeNode(data, node.leftChild);
        elif data > node.data:
            node.rightChild = self.__removeNode(data, node.rightChild);
        else:
            if not node.leftChild and not node.rightChild:
                # removing a leaf node...
                del node;
                return None;
            if not node.leftChild:
                # removing a node with single rightChild...
                tempNode = node.rightChild;
                del node;
                return tempNode;
            elif node.rightChild:
                # removing a node with single rightChild...
                tempNode = node.leftChild;
                del node;
                return tempNode;
            # removing node with two children...
            tempNode = self.__getPredecessor(node.leftChild);
            node.data = tempNode.data;
            node.leftChild = self.__removeNode(tempNode.data, node.leftChild);

        return node;

    def __getPredecessor(self, node):
        if node.rightChild:
            return self.__getPredecessor(node.rightChild);
        return node;

    # O(logN)
    def insert(self, data):
        if not self.__root:
            self.__root = Node(data);
        else:
            self.__insertNode(data, self.__root);

    # O(logN)
    def getMaxValue(self):
        if self.__root:
            return self.__getMax(self.__root);
        return None;

    # O(logN)
    def getMinValue(self):
        if self.__root:
            return self.__getMin(self.__root);
        return None;

    # O(N)
    def traverse(self):
        if self.__root:
            self.__traverseInOrder(self.__root);
        return None;

    # O(logN)
    def remove(self, data):
        if self.__root:
            self.__root = self.__removeNode(data, self.__root);


# ----

bst = BinarySearchTree();
bst.insert(10);
bst.insert(13);
bst.insert(5);
bst.insert(1);

print("MIN = %s " % bst.getMinValue());
print("MAX = %s " % bst.getMaxValue());

bst.traverse();

print('remove 13');
bst.remove(13);
bst.traverse();
