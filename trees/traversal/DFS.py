
def preorder(rootNode, values):
    '''
    Order: (root, left, right)
    '''
    if not rootNode:
        return values

    # record root value first
    values.append(rootNode.value)

    # check left subtree
    values = preorder(rootNode.left, values)

    # check right subtree
    values = preorder(rootNode.right, values)

    return values

def inorder(rootNode, values):
    '''
    Order: (left, root, right)
    '''
    if not rootNode:
        return values

    # check the left subtree
    values = inorder(rootNode.left, values)

    # record the value after left but before right
    values.append(rootNode.value)

    # check the right subtree
    values = inorder(rootNode.right, values)

    return values


def postorder(rootNode, values):
    '''
    Order: (left, right, root)
    '''
    if not rootNode:
        return values

    # check left and right subtrees before reporting the root
    values = postorder(rootNode.left, values)
    values = postorder(rootNode.right, values)
    values.append(rootNode.value)
    return values
