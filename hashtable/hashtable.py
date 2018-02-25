import hashlib
class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class Hashtable:
    def __init__(self, mode, size=25):
        '''
        mode - a string in the set {"chain", "linear", "quadratic", "double"}
        '''
        if mode in ["chain", "linear", "quadratic", "double"]:
            self.mode = mode
            self.size = size
            self.numKeys = 0
            self.table = [None for i in range(size)]
            self.keys = set()
        else:
            return None

    def resize(self, size=None):
        oldpairs = []
        for key in self.keys:
            oldpairs.append((key, self.get(key)))

        if not size:
            self.size = self.size*2
        else:
            self.size = size

        self.table = [None for i in range(self.size)]
        for pair in oldpairs:
            self.put(pair[0], pair[1])



    def _hash1(self, key):
        encoded = key.encode()
        return int(hashlib.sha1(encoded).hexdigest(), 16) % self.size


    def _chain_put(self, key, value):
        self.keys.add(key)
        index = self._hash1(key)
        #print("Putting: "+str(key)+"-"+str(value)+" in index "+str(index))

        node = LLNode(key, value)

        # empty index
        if not self.table[index]:
            self.table[index] = (node, node)
        else:
            # add node to the tail of the LL
            self.table[index][1].next = node

            # update the tail
            self.table[index] = (self.table[index][0], node)

    def put(self, key, value=None):
        if self.mode == "chain":
            self._chain_put(key, value)
        elif self.mode == "linear":
            self._linear_put(key, value)
        elif self.mode == "quadratic":
            self._quadratic_put(key, value)
        elif self.mode == "double":
            self._double_put(key, value)

    def _chain_get(self, key):
        index = self._hash1(key)
        node = self.table[index][0]
        while node:
            if node.key == key:
                return node.value
            node = node.next



    def get(self, key):
        if key not in self.keys:
            return None
        if self.mode == "chain":
            return self._chain_get(key)
        elif self.mode == "linear":
            return self._linear_get(key)
        elif self.mode == "quadratic":
            return self._quadratic_get(key)
        elif self.mode == "double":
            return self._double_get(key)

    def _chain_delete(self, key):
        self.keys.remove(key)

        index = self._hash1(key)

        head = self.table[index][0]
        tail = self.table[index][1]
        if head.key == key and tail.key == key:

            self.table[index] = None
            return
        elif head.key == key:
            newhead = head.next
            head.next = None
            self.table[index] = (newhead, self.table[index][1])


        previous = head
        node = head.next
        while node:
            if node.key == key:
                previous.next = node.next
                node.next = None
                return
            previous = node
            node = node.next


    def delete(self, key):
        if key not in self.keys:
            return
        if self.mode == "chain":
            self._chain_delete(key)
        elif self.mode == "linear":
            self._linear_delete(key)
        elif self.mode == "quadratic":
            self._quadratic_delete(key)
        elif self.mode == "double":
            self._double_delete(key)

if __name__ == "__main__":
    chain = Hashtable(mode="chain", size=3)
    testStrStr = {"brian": "dang",
                  "thomas": "kang",
                  "Harrison": "d",
                  "sam": "hughes",
                  "Brian": "Caps"}
    # put key-values into hashtable
    for key in testStrStr.keys():
        chain.put(key, testStrStr[key])


    print("\nChecking Chain get():")
    # check the key-values in hashtable
    for key in testStrStr.keys():
        val = chain.get(key)
        if testStrStr[key] != val:
            print("WRONG: got "+str(val)+" | wanted "+str(testStrStr[key]))

    # delete brian
    print("\nDeleting \"brian\":")
    chain.delete("brian")
    for key in testStrStr.keys():
        val = chain.get(key)
        if testStrStr[key] != val:
            print("WRONG: got "+str(val)+" | wanted "+str(testStrStr[key]))

    # check the key-values after resizing
    print("\nResizing and readding brian-dang:")
    chain.resize()
    chain.put("brian", "dang")
    for key in testStrStr.keys():
        val = chain.get(key)
        if testStrStr[key] != val:
            print("WRONG: got "+str(val)+" | wanted "+str(testStrStr[key]))
