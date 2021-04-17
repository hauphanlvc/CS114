import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    S = sum(a)
    print(math.ceil(S/n))