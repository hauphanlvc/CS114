import io,os,sys
# input=sys.stdin.readline
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
n,m=map(int,input().split())
arr=list()
Res = '' 
rr,c=map(int,input().split())
for i in range(n):
    a = list(map(int,input().split()))
    for x in a:
        Res+=str(x)
    arr.append(a)
if n*m!=rr*c:
    for i in range(n):
        print(*arr[i]) 
else:
    i=0
    j=c
    while rr>0:
        for k in range(i,j):
            print(Res[k],end=' ')
        print()
        i+=c
        j+=c
        rr-=1
    



