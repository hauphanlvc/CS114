import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import time
import sys
sys.stdin = open("InputOfHeightOfTree.txt","r")
sys.stdout = open("OutputOfHeightOfTree.txt","w")

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
def HeightOfTree(root):
    if root is None : return 0
    return 1 + max(HeightOfTree(root.left),HeightOfTree(root.right))
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

import collections
L = collections.deque()

while True :
    a = list(map(int,input().split()))
    T = a[0]
    if T == 3 :
        break
    elif T ==2 :
        # L.Dang2(a[1],a[2])
        # # if L.index(a[1]) is ValueError : pass
        # if L.index(a[1]) is not ValueError :
        # #     
        # x = L.index(a[1])
        # L.insert(x,a[2])
        # ValueError(L.appendleft(a[2]))
        try :
            L.insert(L.index(a[1])+1,a[2])
        except:
            L.appendleft(a[2])
    elif T == 1 :
        # L.Dang1(a[1])
        L.append(a[1])
    elif T == 0 :
       L.appendleft(a[1])
        

root = None 
# p = L.head
# while p is not None:
#     root = insert(root,p.value)
#     p = p.next
for i in L:
    root = insert(root,i)
print(HeightOfTree(root))