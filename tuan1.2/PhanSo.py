def UCLN(a, b):
    c = a%b
    while c != 0:
        a = b
        b = c
        c = a%b
    return b
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = UCLN(a, b)
    a = a//c
    b = b//c
    
    if b == 1:
        print(a)
    else:
        print(a, b)