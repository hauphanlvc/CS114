def Merge(a,b,na,nb):
    c = [None] * (na + nb)
    i , j , k = 0, 0, 0
    while i < na and j < nb:
        if a[i]< b[j]:
            c[k] = a[i]
            k+=1
            i+=1
        else:
            c[k]= b[j]
            k+=1
            j+=1
    while i < na:
        c[k] = a[i]
        k+=1
        i+=1
    while j < nb :
        c[k] = b[j]
        k+=1
        j+=1
    for i in c:
        print(i,end=' ')


na,nb = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
Merge(a,b,na,nb)
