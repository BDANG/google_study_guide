from queue import Queue
def bfs(rootNode,values):
    q = Queue()
    node = rootNode
    while (node):
        values.append(node.value)
        q.put(node.left)
        q.put(node.right)
        node = q.get()
    return values
