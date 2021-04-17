# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
sys.stdin = open("InputDemNodeLa.txt","r")
sys.stdout = open("OutputDemNodela.txt","w")
class BST:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
def insert(root, key):
    if root is None:
        return BST(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
def CountLeafNodes(root):
    if root is None: return 0
    if root.left is None and root.right is None : return 1
    return CountLeafNodes(root.left) + CountLeafNodes(root.right)    
root = None
while True:
    x = int(input())
    if x == 0 :
        print(CountLeafNodes(root))
        break
    else :
        root = insert(root,x)