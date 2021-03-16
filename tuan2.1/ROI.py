import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
input = sys.stdin.readline
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
h , w = map(int,input().split())
a = list()
for i in range(h):
    Hang = list(map(int,input().split()))
    a.append(Hang)
top,left,bottom,right = map(int,input().split())
Res = list()
for i in range(h):
    if i in range(top,bottom + 1 ):
        Hang = [0 for x in range(left)] + a[i][left:right+1] + [0 for x in range(right+1,w)]
        sys.stdout.write(" ".join(map(str,Hang))+ "\n")
    else :
        Hang = [0 for x in range(w)]
        sys.stdout.write(" ".join(map(str,Hang))+ "\n") 
  
    # print("\n")

    
