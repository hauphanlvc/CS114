from bisect import bisect_left,bisect_right
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
def solve(a,k,x,n):
    Max = max(a)
    Min = min(a)
    if x <= Min:
        for i in range(k):
            print(a[i],end=' ')
    elif x >= Max:
        for i in range(n - k, n):
            print(a[i],end=' ')
    else :
        index = bisect_left(a,x)
        # print(index)
        # count = 0
        left = index - 1
        right = index
        Res = list()
        while k>0:
            if (abs(a[left]- x ) < abs(a[right]- x)):
                Res.append(a[left])
                left-=1
            else :
                Res.append(a[right])
                right+=1
            k-=1
        Res.sort()
        for i in Res:
            print(i,end=' ')

n = int(input())
a= list(map(int, input().split()))
k , x = map(int,input().split())
solve(a,k,x,n)

# printKclosest(a,x,k,n)