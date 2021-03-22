from bisect import bisect_left,bisect_right
import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
def solve(a,k,x,n):
    Max = max(a)
    Min = min(a)
    if x <= Min:
        print(a[0],a[k-1])            
    elif x >= Max:
        print(a[n-k],a[n-1])
    else :
        index = bisect_left(a,x)
        # print(index)
        # count = 0
        left = index - 1
        right = index
        # Res = list()
        Min = 100000000000
        Max = -10000000000
        while k>0:
            if ((a[left]- x ) < (a[right]- x)):
                # Res.append(a[left])
                Min= min(a[left],Min)
                Max = max(a[left],Max)
                left-=1
            else :
                Min= min(a[left],Min)
                Max = max(a[left],Max)
                right+=1
            k-=1
        print(Max,Min)
n = int(input())
a= list(map(int, input().split()))
while True:
    try :
        k , x = map(int,input().split())
        solve(a,k,x,n)

    except:
        exit()

# printKclosest(a,x,k,n)