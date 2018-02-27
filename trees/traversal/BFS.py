from queue import Queue
def oldbfs(rootNode,values):
    '''
    Old version that assumed perfect tree
    '''
    q = Queue()
    node = rootNode
    while (node):
        values.append(node.value)
        q.put(node.left)
        q.put(node.right)
        node = q.get()
    return values

def bfs(rootNode, values):
    q = Queue()
    #node = rootNode
    q.put(rootNode)
    while not q.empty():
        node = q.get()
        if node:
            values.append(node.value)
            q.put(node.left)
            q.put(node.right)
        else:
            values.append(None)
    return values
