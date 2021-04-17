n=int(input())
a=list(map(int,input().split()))
best = -100000
sum=0
left=0
right=0
current=0
for i in range(n):
    if (sum+a[i]<a[i]):
        current=i
        sum=a[i]
    else:
        sum+=a[i]
    if (best<sum):
        best=sum
        left=current
        right=i
print(left,right,best)