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

    def _linear_put(self, key, value):
        index = self._hash1(key)

        if not self.table[index]:
            self.table[index] = (key, value)
        else:
            searchindex = (index + 1) % self.size
            while True:
                if searchindex == index:
                    break
                if not self.table[searchindex]:
                    self.table[searchindex] = (key, value)
                    break
                searchindex = (searchindex + 1) % self.size


    def put(self, key, value=None):
        self.keys.add(key)
        if self.mode == "chain":
            self._chain_put(key, value)
        elif self.mode == "linear":
            # wip: handle resizing when hashtable is full
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

    def _linear_get(self, key):
        index = self._hash1(key)
        searchIndex = index
        while True:
            if self.table[searchIndex][0] == key:
                return self.table[searchIndex][1]

            searchIndex = (searchIndex+1) % self.size
            if searchIndex == index:
                break




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

    def _linear_delete(self, key):
        index = self._hash1(key)
        searchIndex = index
        while True:
            if not self.table[searchIndex] and self.table[searchIndex][0] == key:
                self.table[searchIndex] = None

            searchIndex = (searchIndex+1) % self.size
            if searchIndex == index:
                break

    def delete(self, key):
        if key not in self.keys:
            return
        self.keys.remove(key)

        if self.mode == "chain":
            self._chain_delete(key)
        elif self.mode == "linear":
            self._linear_delete(key)
        elif self.mode == "quadratic":
            self._quadratic_delete(key)
        elif self.mode == "double":
            self._double_delete(key)

def load_hashtable(table, testset):
    # put key-values into hashtable
    for key in testset.keys():
        table.put(key, testset[key])

def test_table_contents(table, testset):
    for key in testset.keys():
        val = table.get(key)
        if testset[key] != val:
            print(str(key)+": got "+str(val)+" | wanted "+str(testset[key]))

def test_chain_hashtable(testset):
    print("\n---TESTING SEPARATE CHAIN HASHTABLE---")
    table = Hashtable(mode="chain", size=3)

    load_hashtable(table, testset)

    print("\nChecking Chain get():")
    # check the key-values in hashtable
    test_table_contents(table, testset)

    # delete brian
    print("\nDeleting brian-"+testset["brian"]+":")
    table.delete("brian")
    test_table_contents(table, testset)

    # check the key-values after resizing
    print("\nResizing and re-adding brian-"+testset["brian"]+":")
    table.resize()
    table.put("brian", testset["brian"])
    test_table_contents(table, testset)

def test_linear_hashtable(testset):
    print("\n---TESTING LINEAR PROBE HASHTABLE---")
    table = Hashtable(mode="linear", size=len(testset.keys()))

    # put key-values into hashtable
    load_hashtable(table, testset)

    print("\nChecking Linear get():")
    # check the key-values in hashtable
    test_table_contents(table, testset)

    # delete Harrison-d
    print("\nDeleting Harrison-"+testset["Harrison"]+":")
    table.delete("Harrison")
    test_table_contents(table, testset)

    print("\nResizing and re-adding Harrison-"+testset["Harrison"])
    table.resize()
    table.put("Harrison", testset["Harrison"])
    test_table_contents(table, testset)

if __name__ == "__main__":
    testset = {"brian": "dang",
                  "thomas": "kang",
                  "Harrison": "d",
                  "sam": "hughes",
                  "Brian": "Caps"}
    test_chain_hashtable(testset)
    test_linear_hashtable(testset)
