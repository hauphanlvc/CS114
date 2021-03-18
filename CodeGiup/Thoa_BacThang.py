n = int(input())
if n < 10 :
    print(2)
else:
    a = list()
    a.append(0)
    a.append(0)

    for i in range(2,14):
        a.append(a[i-1]+ 18)
    SoChuSoCuaN = len(str(n))
    SoChuSoCuaNtru1 = len(str(n-1))
    n -= 1
    n = str(n)
    SoDauCuaNtru1 = n[0]
    print(SoChuSoCuaNtru1)