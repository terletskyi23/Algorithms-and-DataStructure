class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


class BFS(object):

    def bfs(self, start_node):
        queue = []

        queue.append(start_node)
        start_node.visited = True

        while queue:
            actual_node = queue.pop(0)
            print("Node name: %s" % actual_node.name)

            for node in actual_node.adjacency_list:
                if not node.visited:
                    node.visited = True
                    queue.append(node)


# ----

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node1.adjacency_list.append(node4)

node2.adjacency_list.append(node5)
node2.adjacency_list.append(node6)

node4.adjacency_list.append(node7)

node7.adjacency_list.append(node8)


bfs = BFS()
bfs.bfs(node1)
