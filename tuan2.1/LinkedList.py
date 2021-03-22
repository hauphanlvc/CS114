import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import time
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def ThemDau(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def ThemCuoi(self,new_data):
        new_node = Node(new_data) 
        if self.head is None :
            self.head= self.tail = new_node
        else:
            
            self.tail.next = new_node
            self.tail = new_node
        
    def Tim(self,x):
        p = self.head
        while p is not None:
            if p.value == x : return p
            p = p.next
        return None
    def ThemSau(self,q,x):
        if q is None : self.ThemDau(x)
        elif q.next is None : self.ThemCuoi(x)
        else :
            p = Node(x)
            p.next = q.next
            q.next = p
    def XoaDau(self):
        if self.head is None:
            return
        if self.head == self.tail :
            self.head = self.tail = None
        else :
           self.head = self.head.next
    
    

    def PrintList(self):

        if self.head is None:
            print("blank")
        else :
            res = []
            temp = self.head
            while temp is not None :
                res.append(temp.value)
                temp = temp.next 
            sys.stdout.write(" ".join(map(str,res)) + "\n")
            
    def Dang0(self,x):
        self.ThemDau(x)
    def Dang1(self,x):
        self.ThemCuoi(x)
    def Dang2(self,a,b):
        p = self.head
        while p is not None:
            if p.value == a : 
                self.ThemSau(p,b)
                return
            p = p.next
        self.ThemDau(b)        
        
    def Dang3(self,a):
        if self.head is None : return
        if self.head.value == a:
            self.XoaDau()
            return
        x = self.head
        Truoc= x 
        while x is not None:
            if x is None : return
            if x.value == a :
                if x == self.head :
                    self.head = self.head.next
                    return
                elif self.tail== x :
                    Truoc.next = None
                    self.tail= Truoc 
                    return       
                elif x == self.head and self.tail == x :
                    self.head = self.tail = None
                    return
                else:
                    Truoc.next = x.next
                    x = x.next
                    return
                
            else :
                Truoc = x 
                x = x.next
        

    def Dang4(self,n):
        if self.head is None : return
        while self.head.value == n: 
            self.XoaDau()
            if self.head is None : return
        # print(self.head,self.tail)
        x = self.head
        Truoc= x 
        while x is not None:
            if x is None : return
            if x.value == n :
                if x == self.head :
                    self.head = self.head.next
                elif self.tail== x :
                    Truoc.next = None
                    self.tail= Truoc 
                    return       
                elif x == self.head and self.tail == x :
                    self.head = self.tail = None
                    return
                else:
                    Truoc.next = x.next
                    x = x.next
            else :
                Truoc = x 
                x = x.next



    def Dang5(self):
        self.XoaDau()
    def Dang6(self):
        self.PrintList()


ONLINE_JUDGE = False
if not ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
L = LinkedList()
while True :
    a = list
    T = a[0]
    if T == 6 :
        L.Dang6()
        # end = time.perf_counter() 
        # print(end - start)
        exit()
            
    elif T == 5 :
        L.Dang5()
        # print("5\n------")
        # L.PrintList()
    elif T == 4 :
        L.Dang4(a[1])
        # print(T,a[1])
        # print("-------")
        # L.PrintList()

    elif T == 3 :
        L.Dang3(a[1])
        # print(T,a[1])
        # print("-------")
        # L.PrintList()

    elif T ==2 :
        L.Dang2(a[1],a[2])
        # print(T,a[1],a[2])
        # print("-------")
        # L.PrintList()

    elif T == 1 :
        L.Dang1(a[1])
        # print(T,a[1])
        # print("-------")
        # L.PrintList()

    elif T == 0 :
        L.Dang0(a[1])
    #     print(T,a[1])
    #     print("-------")
    #     L.PrintList()
    # print("\n")

