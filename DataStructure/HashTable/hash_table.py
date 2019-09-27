CAPACITY = 20

class HashTable(object):

    def __init__(self):
        self.__size = CAPACITY
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size


    def put(self, key, value):
        index = self.__hash_function(key)

        # the linear probing
        while self.__keys[index] is not None:
            if self.__keys[index] == key:
                break

            index = (index + 1) % self.__size

        self.__keys[index] = key
        self.__values[index] = value

        print("the { %s : %s } was inserted on the position %s" % (key, value, index))


    def get(self, key):
        index = self.__hash_function(key)

        # the linear probing
        while self.__keys[index] is not None:
            if self.__keys[index] == key:
                return self.__values[index]

            index = (index + 1) % self.__size

        return None


    def __hash_function(self, key):
        sum = 0

        for i in range(len(key)):
            sum += ord(key[i])

        return sum % self.__size


# ----

hash = HashTable()

print(hash.get("batman"))

hash.put("batman", "Bruce Wayne")
print(hash.get("batman"))
