import io,os,sys
# input=sys.stdin.readline
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
n , m = map(int,input().split())
r , c = map(int,input().split())
a = list()
A = list()
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
    for j in b:
        A.append(j)
kq = [[None] * r ] * c
k = 0
print(kq)
for i in range(0,r):
    for j in range(0,c):
        
        print(k)
        
        kq[i][j] = A[k]
        k+=1
print(A[14])