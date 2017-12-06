class Node(object):

    def __init__(self, data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;


class BinarySearchTree:

    def __init__(self):
        self.root = None;

    # O(logN) if the tree is balanced !!!!!!!!!!! --> it can reduce to O(N) --> AVL RBT are needed !!!
    def _insertNode(self, data, node):
        newNode = Node(data);
        if data < node.data:
            if node.leftChild:
                self._insertNode(data, node.leftChild);
            else:
                node.leftChild = newNode;
        elif data > node.data:
             if node.rightChild:
                 self._insertNode(data, node.rightChild);
             else:
                 node.rightChild = newNode;
        else:
            print('already inserted');

    def _getMax(self, node):
        if node.rightChild:
            return self._getMax(node.rightChild);
        return node.data;

    def _getMin(self, node):
        if node.leftChild:
            return self._getMin(node.leftChild);
        return node.data;

    def _traverseInOrder(self, node):
        if node.leftChild:
            self._traverseInOrder(node.leftChild);

        print("%s " % node.data);

        if node.rightChild:
            self._traverseInOrder(node.rightChild);

    def _removeNode(self, data, node):
        if not node:
            return node;

        if data < node.data:
            node.leftChild = self._removeNode(data, node.leftChild);
        elif data > node.data:
            node.rightChild = self._removeNode(data, node.rightChild);
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
            tempNode = self._getPredecessor(node.leftChild);
            node.data = tempNode.data;
            node.leftChild = self._removeNode(tempNode.data, node.leftChild);

        return node;

    def _getPredecessor(self, node):
        if node.rightChild:
            return self._getPredecessor(node.rightChild);
        return node;

    # O(logN)
    def insert(self, data):
        if not self.root:
            self.root = Node(data);
        else:
            self._insertNode(data, self.root);

    # O(logN)
    def getMaxValue(self):
        if self.root:
            return self._getMax(self.root);
        return None;

    # O(logN)
    def getMinValue(self):
        if self.root:
            return self._getMin(self.root);
        return None;

    # O(N)
    def traverse(self):
        if self.root:
            self._traverseInOrder(self.root);
        return None;

    # O(logN)
    def remove(self, data):
        if self.root:
            self.root = self._removeNode(data, self.root);


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
