import math
def sum(a):
    i = 0
    s = 0
    while i < len(a):
        s = s+a[i]
        i = i+1
    return s

n = int(input())
i = 0
while i < n:
    m = int(input())
    a = list(map(int, input().split()))
    print(math.ceil(sum(a)/m))
    i = i + 1