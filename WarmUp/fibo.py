def fibo(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fibo(n-1) + fibo(n-2)

x = int(input())
if x <= 0 or x > 30 : 
    print("So {} khong nam trong khoang [1,30].".format(x))
else :
    print(fibo(x))
