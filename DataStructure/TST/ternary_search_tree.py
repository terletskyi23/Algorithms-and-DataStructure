class Node(object):

    def __init__(self, character):
        self.character = character
        self.left_node = None
        self.middle_node = None
        self.right_node = None
        self.value = None


class TST(object):

    def __init__(self):
        self.__root_node = None


    def put(self, key, value):
        print("* put node: { key: %s, value: %s } *" % (key, value))
        self.__root_node = self.__put_item(self.__root_node, key, value, 0)


    def __put_item(self, node, key, value, index):

        character = key[index]
        print("- character: %s -" % character)

        if node == None:
            node = Node(character)

        if character < node.character:
            print("<<< left <<<")
            node.left_node = self.__put_item(node.left_node, key, value, index)
        elif character > node.character:
            print(">>> right >>>")
            node.right_node = self.__put_item(node.right_node, key, value, index)
        elif index < len(key) - 1: # not in the ens of key world
            print("vvv bottom vvv")
            node.middle_node = self.__put_item(node.middle_node, key, value, index + 1)
        else:
            node.value = value
            print("= value: %s was inserted =" % value)

        return node


    def get(self, key):
        print("* get node by key: %s *" % key)
        node = self.__get_item(self.__root_node, key, 0)

        if node == None:
            print("= not found =")
            return None

        print("= node value: %s =" % node.value)
        return node.value


    def __get_item(self, node, key, index):

        if node == None:
            return None

        character = key[index]
        print("- character: %s -" % character)

        if character < node.character:
            print("<<< left <<<")
            return self.__get_item(node.left_node, key, index)
        elif character > node.character:
            print(">>> right >>>")
            return self.__get_item(node.right_node, key, index)
        elif index < len(key) - 1: # not in the ens of key world
            print("vvv bottom vvv")
            return self.__get_item(node.middle_node, key, index + 1)
        else:
            print("- node was founded -")
            return node


# ----

tst = TST()
print("!" * 30)

tst.put("apple", 23)
print("#" * 30)

# tst.get("app")
# print("#" * 30)

# tst.put("app", 8)
# print("#" * 30)

# tst.put("bee", 2)
# tst.put("beer", 18)
# tst.put("deer", 56)
# tst.put("ralabs", 100)
