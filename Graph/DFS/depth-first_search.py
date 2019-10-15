class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


class DFS(object):

    def dfs(self, node):
        node.visited = True
        print("Node name: %s" % node.name)

        # we can use STACK, or like here, recursive method
        for adjacency_node in node.adjacency_list:
            if not adjacency_node.visited:
                self.dfs(adjacency_node)


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


dfs = DFS()
dfs.dfs(node1)
