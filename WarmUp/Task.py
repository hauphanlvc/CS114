n = int(input())
k = int(input())
p = int(input())
q = int(input())

alice=p*2-1+(q-1)
if(alice>n or alice<1):
    print(-1)
else:
    if(alice-k>0):
        bob=alice-k
    else:
        bob=alice+k

    if(bob<=n):
        if(bob%2==0):
            v=2
        else: 
            v=1
        u=int(((bob-(v-1))+1)/2)
        print(u,v)
    else:
        print(-1)