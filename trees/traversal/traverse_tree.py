import BFS
import DFS
import sys
sys.path.insert(0,'..')
from trees import BinaryTree
if __name__ == "__main__":
    bt = BinaryTree(valueList=[1,2,3,4,5,6,7])

    print("BFS: "+str(BFS.bfs(bt.root, []))+"\n")
    print("DFS Preorder: "+str(DFS.preorder(bt.root, [])))
    print("DFS Inorder: "+str(DFS.inorder(bt.root, [])))
    print("DFS Postorder: "+str(DFS.postorder(bt.root, [])))
