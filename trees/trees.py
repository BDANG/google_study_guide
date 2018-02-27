from queue import Queue
class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None, valueList=None, mode=None):
        if root:
            self.root = root
        elif valueList and mode == "generic":
            self.root = self.build_generic_tree(valueList)
        elif valueList and mode == "generic_bst":
            self.root = self.build_generic_bst(valueList)
        #elif valueList and mode == "preorder_bst"
        else:
            self.root = None

    # WIP: watch for empty valueList?
    def build_generic_tree(self, valueList):
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

    def build_generic_bst(self, valueList):
        rootNode = None

        for val in valueList:
            if not rootNode:
                rootNode = BinaryTreeNode(val)
                continue
            self.generic_bst_insert(rootNode, val)
        return rootNode

    def generic_bst_insert(self, root, val):
        if not root.left and val <= root.value:
            root.left = BinaryTreeNode(val)
            return
        elif not root.right and root.value < val:
            root.right = BinaryTreeNode(val)
            return

        if val <= root.value:
            self.generic_bst_insert(root.left, val)
        else:
            self.generic_bst_insert(root.right, val)
