import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputPrintMang2d.txt","r")
sys.stdout = open("OutputPrintMang2d.txt","w")

r , c = map(int,input().split())
a = list()
for i in range(r):
    b = list(map(int,input().split()))
    a.append(b)
DoDaiCanLe = list()
for i in range(c):
    DoDaiCanLe.append(0)
for j in range(0,c):
    Max = 0
    for i in range(0,r):
        Max=max(Max,len(str(a[i][j])))
    DoDaiCanLe[j] = Max
# print(*DoDaiCanLe)
for i in range(0,r):
    for j in range(0,c):
        print("{:>{}}".format(a[i][j],DoDaiCanLe[j]),end= ' ')
    print()
    