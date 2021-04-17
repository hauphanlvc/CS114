
import collections
class Node:
  def __init__(self,data):
    self.left=None
    self.right=None
    self.val=data
def insert_tree(root,data):
  if root is None:
    return Node(data)
  else:
    if root.val==data:
      return root
    elif root.val<data:
      root.right=insert_tree(root.right,data)
    else:
      root.left=insert_tree(root.left,data)
  return root
def Height(root):
  if root==None:
    return 0
  else:
    a=Height(root.left)
    b=Height(root.right)
  if (a>b): 
    return(a+1)
  else:
    return(b+1)
root=None
q=collections.deque()
while True:
  l=([int(x) for x in input().split()])
  if l[0]==3:
    break
  if l[0]==0:
    q.appendleft(l[1])
  if l[0]==1:
    q.append(l[1])
  if l[0]==2: 
    if q.count(l[2])!=0:
      vt=q.index(l[1],0,len(q))
      q.insert(vt+1,l[2])
    else:
      q.appendleft(l[2])
while len(q)!=0:
  x=q.popleft()
  root=insert_tree(root,x)
print(Height(root))