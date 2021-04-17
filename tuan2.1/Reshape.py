import io,os,sys
# input=sys.stdin.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
n , m = map(int,input().split())
r , c = map(int,input().split())
# a = list()
# for i in range(n):
#     b = list(map(int,input().split()))
#     a.append(b)

if n*m != r*c or (n == r and m==c ):
    for i in range(n):
        # sys.stdout.write(" ".join(map(str,a[i])) + "\n")
        x = input()
        print(x)

else :
   i = 0 
   stack = list()
   kq = list()
   while i < n or len(stack)>0 :
        while len(stack) < c :
           x = input()
           x = x.split()
           stack.extend(x)
           i+=1
        sys.stdout.write(" ".join(map(str,stack[:c])) + "\n")
        stack = stack[c:]