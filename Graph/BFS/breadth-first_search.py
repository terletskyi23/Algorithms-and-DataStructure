class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacenciList = []
        self.visited = False
        self.predecessor = None


class BFS(object):

    def bfs(self, startNode):
        queue = []

        queue.append(startNode)
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print("Node name: %s" % actualNode.name)

            for n in actualNode.adjacenciList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


# ----

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacenciList.append(node2)
node1.adjacenciList.append(node3)
node1.adjacenciList.append(node4)

node2.adjacenciList.append(node5)
node2.adjacenciList.append(node6)

node4.adjacenciList.append(node7)

node7.adjacenciList.append(node8)


bfs = BFS()
bfs.bfs(node1)
