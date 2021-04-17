import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
l = LinkedList()

def add_head(l,data):
    if l.head is None:
        l.head = l.tail = Node(data)
    else:
        x = Node(data)
        x.next = l.head
        l.head = x
def add_tail(l,data):
    if l.head is None:
        l.head = l.tail = Node(data)
    else:
        x = Node(data)
        l.tail.next = x
        l.tail = x
def find_and_add(l,a,b):
    if l.head is None:
        add_head(l,b)
    else:
        p = l.head
        while p is not None:
            if p.data == a:
                break
            p = p.next
        if p is None:
            add_head(l,b)
            return
        if p==l.tail:
            add_tail(l,b)
        else:
            temp = p.next
            x = Node(b)
            p.next = x
            x.next = temp
def  find_and_delete(l,x):
    if l.head is not None:
        if l.head.data == x:
            delete_head(l)
            return
        p = l.head
        bef = None
        while p is not None:
            if p.data == x:
                break
            bef = p
            p = p.next
        if p is None:
            return
        if p == l.tail:
            l.tail = bef
            bef.next = None
        else:
            bef.next = p.next
def find_and_delete_all(l,x):
    if l.head == None:
        return
    while l.head.data == x:
        delete_head(l)
        if l.head is None:
            return
    p = l.head
    bef = l.head
    while p is not None:
        if p.data == x:
            if l.head == l.tail == p:
                l.head = l.tail = None
                return
            elif l.tail == p:
                l.tail = bef
                bef.next = None
                return
            else:
                temp = p.next
                bef.next = p.next
                p = temp
        else:
            bef = p
            p = p.next
def delete_head(l):
    if l.head ==l.tail:
        l.head = l.tail = None
    else:
        l.head = l.head.next

l = LinkedList()        
while True:
    inputs = [int(x) for x in input().split()]
    #inputs =get_ints()
    # inputs = list(map(int,inputs))
    if inputs[0]==0:
        add_head(l,inputs[1])
    elif inputs[0]==1:
        add_tail(l,inputs[1])
    elif inputs[0]==2:
        a = inputs[1]
        b = inputs[2]
        find_and_add(l, a, b)
    elif inputs[0]==3:
        x = inputs[1]
        find_and_delete(l, x)
    elif inputs[0]==4:
        x = inputs[1]
        find_and_delete_all(l,x)
    elif inputs[0]==5:
        delete_head(l)
    else:	
        break

p = l.head
arr = []
while p is not None:
    arr.append(p.data)
    p = p.next
if len(arr) == 0:
    print('blank')
else:
    sys.stdout.write(" ".join(map(str,arr)) + "\n")