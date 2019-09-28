class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.value = None
        self.counter = 0
        self.word_finished = False

class Trie:
    def __init__(self):
        self.__root = Node("*")

    def insert(self, key, value):
        current = self.__root

        for char in key:
            if char in current.children:
                current = current.children[char]
            else:
                new_node = Node(char)
                current.children[char] = new_node
                current = new_node

            current.counter += 1

        current.word_finished = True
        current.value = value

        print("the { %s : %s } was inserted" % (key, value))


    def search(self, key):
        print("searching %s ..." % key)

        if not self.__root.children:
            return None

        current = self.__root

        for char in key:
            if char in current.children:
                current = current.children[char]
            else:
                return None

        return current.value if current.word_finished else None


# ----

trie = Trie()

trie.insert("test", 23)
trie.insert("pes", 8)
trie.insert("pesso", 92)

print("#" * 30)

print("Found: %s" % trie.search("p"))
print("Found: %s" % trie.search("pes"))
print("Found: %s" % trie.search("pesso"))
print("Found: %s" % trie.search("test"))
print("Found: %s" % trie.search("pe"))
print("Found: %s" % trie.search("pessoo"))
