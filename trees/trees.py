from queue import Queue
class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None, valueList=None):
        if root:
            self.root = root
        elif valueList:
            self.root = self.build_tree(valueList)
        else:
            self.root = None

    # WIP: watch for empty valueList?
    def build_tree(self, valueList):
        rootNode = None
        currentNode = None
        q = Queue()
        for val in valueList:
            if not rootNode:
                rootNode = BinaryTreeNode(val)
                currentNode = rootNode
                continue

            if not currentNode.left:
                currentNode.left = BinaryTreeNode(val)
                q.put(currentNode.left)
                continue
            if not currentNode.right:
                currentNode.right = BinaryTreeNode(val)
                q.put(currentNode.right)
                currentNode = q.get()


        return rootNode
