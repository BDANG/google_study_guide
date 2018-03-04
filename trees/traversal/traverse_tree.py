import BFS
import DFS
import sys
sys.path.insert(0,'..')
from trees import BinaryTree
if __name__ == "__main__":

    print("\n---Generic Binary Tree---")
    bt = BinaryTree(valueList=[1,2,3,4,5,6,7], mode="generic")
    print("BFS: "+str(BFS.bfs(bt.root, []))+"\n")
    print("DFS Preorder: "+str(DFS.preorder(bt.root, [])))
    print("DFS Inorder: "+str(DFS.inorder(bt.root, [])))
    print("DFS Postorder: "+str(DFS.postorder(bt.root, [])))

    print("\n---Generic CHAIN BST---")
    bst = BinaryTree(valueList=[1,2,3,4,5,6,7], mode="generic_bst")
    print("BFS: "+str(BFS.bfs(bst.root, []))+"\n")
    print("DFS Preorder: "+str(DFS.preorder(bst.root, [])))
    print("DFS Inorder: "+str(DFS.inorder(bst.root, [])))
    print("DFS Postorder: "+str(DFS.postorder(bst.root, [])))

    print("\n---Generic Random BST---")
    randbst = BinaryTree(valueList=[10,5,4,6,40,25,50], mode="generic_bst")
    print("BFS: "+str(BFS.bfs(randbst.root, []))+"\n")
    print("DFS Preorder: "+str(DFS.preorder(randbst.root, [])))
    print("DFS Inorder: "+str(DFS.inorder(randbst.root, [])))
    print("DFS Postorder: "+str(DFS.postorder(randbst.root, [])))

    search = 50
    print("Search "+str(search)+" "+str(randbst.search(search)))
    delete = 5
    print("Delete "+str(delete)+" "+str(randbst.delete(delete)))
    print("BFS: "+str(BFS.bfs(randbst.root, []))+"\n")

    print("\n---Preorder BST---")
    preorderbst = BinaryTree(valueList=[10,5,4,6,40,25,50], mode="preorder")
    print(preorderbst.root.value)
    print(preorderbst.root.left.value)
    print("BFS: "+str(BFS.bfs(preorderbst.root, []))+"\n")
    print("DFS Preorder: "+str(DFS.preorder(preorderbst.root, [])))
    print("DFS Inorder: "+str(DFS.inorder(preorderbst.root, [])))
    print("DFS Postorder: "+str(DFS.postorder(preorderbst.root, [])))
