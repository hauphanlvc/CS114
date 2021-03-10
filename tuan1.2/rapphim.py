import math
m,n,a = map(int,input().split())
m = math.ceil(m/a)
n = math.ceil(n/a)
print(m*n)