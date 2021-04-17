import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
from bisect import bisect_left,bisect_right

def solve(a,k,x,n):
    Max = a[n-1]
    Min = a[0]
    if x <= Min:
        print(a[0:k])
    elif x >= Max:
        print(a[n-k: n ])
    else :
        index = bisect_left(a,x)
        # print(index)
        # count = 0
        print(index)
        if index < 0 :
            index = -index - 1
        low = max(0,index - k - 1)
        high = min(n-1,index+k-1)
        while high - low > k -1:
            if low < 0 or (x - a[low] <= a[high] - x ):
                high-=1
            elif high > n-1 or ( x - a[low]> a[high] - x ):
                low+=1
        print(a[low:high+1])    
n = int(input())
a= list(map(int, input().split()))
k , x = map(int,input().split())
solve(a,k,x,n)

# printKclosest(a,x,k,n)