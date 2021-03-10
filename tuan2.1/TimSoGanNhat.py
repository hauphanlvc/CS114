def lower_bound(a,n,x):
    left = 0 
    right = n - 1
    i = (left + right)//2 
    while (left != i ) and (i!=right) :
        if a[i]> x : right = i 
        else : left = i 

    for i in range(left,right+1):
        if a[i] <= x : return i

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
        index = lower_bound(a,n,x)
        # count = 0
        left = index -1 
        right = index + 1
        Res = ''
        Res = Res + str(a[index])
        count = 0
        while (left >=0 ) and ( right < n) and (count < k):
            if (x - a[left] < a[right] - x):
                Res = str(a[left]) + ' ' + Res  
                left-=1
            elif x - a[left] > a[right] - x:
                Res = Res + ' ' +  str(a[right])
                right+=1
            else :
                Res = str(a[left]) + ' ' + Res  
                left-=1
        print(Res)
n = int(input())
a= list(map(int, input().split()))
k , x = map(int,input().split())
solve(a,k,x,n)

# printKclosest(a,x,k,n)