# Note : xem cac ho chua va tram la truong hop cung ten hoa va thuong

import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputThoSuaOngNuoc.txt","r")
sys.stdout = open("OutputThoSuaOngNuoc.txt","w")
def MyFunction(x):
    return x[0]

def DuongDi (a,KiemTra,x):
    HuongX = [0,-1,0,-1]
    HuongY = [1,0,-1,0]
    StartX = x[0]
    StartY = x[1]
    Visited = []
    Queue = []
    Visited.append((StartX,StartY))
    Queue.append((StartX,StartY))
    while Queue:
        X , Y = Queue.pop()
        for i in range(4):
            X_new = X + HuongX[i]
            Y_new = Y + HuongY[i]
            if (X_new,Y_new) not in Visited and a[X_new][Y_new] :
                Visited.append((X_new,Y_new))
                Queue.append((X_new,Y_new))


n = int(input())
a = list()
ListTramBom = list()
ListHoChua = list()
for i in range(n):
    b = str(input())
    a.append(b)
ListTramBom = list()
ListHoChua = list()


for i in range(n):
    for j in range(len(a[0])):
        if a[i][j].isupper() :
            ListTramBom.append((ord(a[i][j]),i,j))
        elif a[i][j].islower():
            ListHoChua.append((ord(a[i][j]),i,j))
ListTramBom.sort(key=MyFunction)
ListHoChua.sort(key=MyFunction)
KiemTra = True
Sum  = 0
for x in ListTramBom:
    Sum += DuongDi(a,KiemTra,x) 
print(ListTramBom)
print(ListHoChua)
