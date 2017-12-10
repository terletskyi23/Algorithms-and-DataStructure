class Node:

    def __init__(self, data):
        self.data = data;
        self.height = 0;
        self.leftChild = None;
        self.rightChild = None;


class AVL(object):

    def __init__(self):
        self.root = None;

    def _calcHeight(self, node):
        if not node:
            return -1;
        return node.height;

    # if it returns value > 1 it means it is a left heavy tree -> right rotation
    # if it returns value < -1 it means it is a right heavy tree -> left rotation
    def _calcBalance(self, node):
        if not node:
            return 0;
        return self._calcHeight(node.leftChild) - self._calcHeight(node.rightChild);

    def _getPredecessor(self, node):
        if node.rightChild:
            return self._getPredecessor(node.rightChild);
        return node;

    # Rotations
    def _rotateRight(self, node):
        print("Rotating on the right on node = %s" % node.data);
        tempLeftChild = node.leftChild;
        rcTlc = tempLeftChild.rightChild;

        tempLeftChild.rightChild = node;
        node.leftChild = rcTlc;

        node.height = max(self._calcHeight(node.leftChild), self._calcHeight(node.rightChild)) + 1;
        tempLeftChild.height = max(self._calcHeight(tempLeftChild.leftChild),
                                   self._calcHeight(tempLeftChild.rightChild)) + 1;

        return tempLeftChild;

    def _rotateLeft(self, node):
        print("Rotating on the left on node = %s" % node.data);
        tempRightChild = node.rightChild;
        lcTrc = tempRightChild.leftChild;

        tempRightChild.leftChild = node;
        node.rightChild = lcTrc;

        node.height = max(self._calcHeight(node.leftChild), self._calcHeight(node.rightChild)) + 1;
        tempRightChild.height = max(self._calcHeight(tempRightChild.leftChild),
                                   self._calcHeight(tempRightChild.rightChild)) + 1;

        return tempRightChild;

    # insert
    def insert(self, data):
        self.root = self._insertNode(data, self.root);

    def _insertNode(self, data, node):
        if not node:
            return Node(data);

        if data < node.data:
            node.leftChild = self._insertNode(data, node.leftChild);
        else:
            node.rightChild = self._insertNode(data, node.rightChild);

        node.height = max(self._calcHeight(node.leftChild), self._calcHeight(node.rightChild)) + 1;

        return self._settleViolation(data, node);

    def _settleViolation(self, data, node):
        balance = self._calcBalance(node);

        # case 1: left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print('Left left heavy situation.. -> right rotation');
            return self._rotateRight(node);

        # case 2: right right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print('Right right heavy situation.. -> left rotation');
            return self._rotateLeft(node);

        # case 3: left right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print('Left right heavy situation.. -> two rotations:\n\rleft child to the left and node to the right)');
            node.leftChild = self._rotateLeft(node.leftChild)
            return self._rotateRight(node);

        # case 4: right left heavy situation
        if balance < -1 and data < node.rightChild.data:
            print('Right left heavy situation.. -> two rotations:\n\rleft child to the left and node to the left)');
            node.rightChild = self._rotateRight(node.rightChild)
            return self._rotateLeft(node);

        # case 5: everything is OK! =)
        return node;

    # remove
    def remove(self, data):
        if self.root:
            self.root = self._removeNode(data, self.root);

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

        # BTS removing + ...

        # if tree had just single node
        if not node:
            return node;

        node.height = max(self._calcHeight(node.leftChild), self._calcHeight(node.rightChild)) + 1;
        balance = self._calcBalance(node);

        # case 1: double left heavy situation
        if balance > 1 and self._calcBalance(node.leftChild) >= 0:
            return self._rotateRight(node);

        # case 2: double right heavy situation
        if balance < -1 and self._calcBalance(node.leftChild) < 0:
            return self._rotateLeft(node);

        # case 3: left right heavy situation
        if balance > 1 and self._calcBalance(node.leftChild) <= 0:
            node.leftChild = self._rotateLeft(node.leftChild)
            return self._rotateRight(node);

        # case 4: right left heavy situation
        if balance < -1 and self._calcBalance(node.leftChild) > 0:
            node.rightChild = self._rotateRight(node.rightChild)
            return self._rotateLeft(node);

        # case 5: everything is OK! =)
        return node;

    # traverse
    def traverse(self):
         if self.root:
             self._traverseInOrder(self.root);

    def _traverseInOrder(self, node):
        if node.leftChild:
            self._traverseInOrder(node.leftChild);

        print("%s " % node.data);

        if node.rightChild:
            self._traverseInOrder(node.rightChild);

# ----

avl = AVL();

# # RR heavy situation
# avl.insert(10);
# avl.insert(20);
# avl.insert(30);

# LL heavy situation
# avl.insert(5);
# avl.insert(4);
# avl.insert(3);

# # LR heavy situation
# avl.insert(5);
# avl.insert(3);
# avl.insert(4);

# RL heavy situation
# avl.insert(3);
# avl.insert(5);
# avl.insert(4);

avl.insert(10);
avl.insert(20);
avl.insert(5);
avl.insert(4);
avl.insert(25);

avl.remove(5);
avl.remove(4);

avl.traverse();
