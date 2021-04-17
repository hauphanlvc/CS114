import sys
# input = sys.stdin.readline
sys.stdin = open("InputPrintMang2d.txt","r")
sys.stdout = open("OutputPrintMang2d.txt","w")

a,b = map(int,input().split())
l = []
maxx =[0 for i in range(b)]
for i in range(a):
    l.append(list(map(str,input().split())))
    print(l)
for i in range(b):
    for j in range(a):
        maxx[i] = max(maxx[i],len(l[j][i]))
for i in range(b):
    print(maxx[i])
for i in range(0,a):
    for j in range(0,b):
        print('{:>{}}'.format(l[i][j],maxx[j]),end=' ')
    print('')