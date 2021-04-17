k = int(input())
t = int(input())  
if k==0:
    print(0)
else:
    if t==0:
        print(0)
    elif t<=k:
        print(t)
    else:
        temp = t//k
        if temp%2==1:
            print(k-t%k)
        else:
            print(t%k)