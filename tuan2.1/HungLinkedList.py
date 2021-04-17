import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None   
  
class LinkedList:  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):  
        new_node = Node(new_data) 
        new_node.next = self.head  
        self.head = new_node 
  
    def insertAfter(self, prev_node, new_data): 
 
        if prev_node is None: 
            self.push(new_data)
 
        new_node = Node(new_data)  
        new_node.next = prev_node.next
        prev_node.next = new_node  

    def append(self, new_data): 
        new_node = Node(new_data)  
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  new_node 

    def deleteNode(self, key):  
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return
        prev.next = temp.next
        temp = None

    def deletePosition(self, position): 
   
        if self.head == None: 
            return 
   
        temp = self.head 
  
        if position == 0: 
            self.head = temp.next
            temp = None
            return 

        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break 
        if temp is None: 
            return 
        if temp.next is None: 
            return  
        next = temp.next.next
 
        temp.next = None
  
        temp.next = next 
  
    def PrintList(self):
            print("blank")
        else :
            res = []
            temp = self.head
            while temp is not None :
                res.append(temp.data)
                temp = temp.next 
            sys.stdout.write(" ".join(map(str,res)) + "\n")
            
    def Dang0(self,x):
        self.push(x)
    
    def Dang1(self,x):
        self.append(x)
        
    def Dang2(self,a,b):
        l=self.head
        while l is not None:
            if l.data==a:
                self.insertAfter(l,b)
                return
            l=l.next
        self.push(b)
    def Dang3(self,n):
        self.deleteNode(n)
    
    def Dang4(self,n):
        x=self.head
        i=0
        j=0
        while x is not None:
            if x.data==n:
                i+=1
            x=x.next
        if i==0:
            return
        else:
            for j in range(i):
                self.deleteNode(n)
    def Dang5(self):
        self.deletePosition(0)

    def Dang6(self):
        self.PrintList()



L = LinkedList()
while True :
    a = list(map(int,input().split()))
    T = a[0]
    if T == 6 :
        L.Dang6()
        exit(0)
            
    elif T == 5 :
        L.Dang5()
    elif T == 4 :
        L.Dang4(a[1])

    elif T == 3 :
        L.Dang3(a[1])

    elif T ==2 :
        L.Dang2(a[1],a[2])

    elif T == 1 :
        L.Dang1(a[1])

    elif T == 0 :
        L.Dang0(a[1])