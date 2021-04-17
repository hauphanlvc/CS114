# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
sys.stdin = open("InputDuyetTheoChieuRongBST.txt","r")
sys.stdout = open("OutpuDuyetTheoChieuRongBST.txt","w")
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
import collections

def printRes(root):
    L = collections.deque()
    L.append(root)
    res = list()
    while L:
        x = L.popleft()
        res.append(x.val)
        if x.left is not None:
            L.append(x.left)
        if x.right is not None:
            L.append(x.right)

    print(*res)
        
root = None
while True:
    x = int(input())
    if x == 0 :
        printRes(root)
        break
    else :
        root = insert(root,x)
