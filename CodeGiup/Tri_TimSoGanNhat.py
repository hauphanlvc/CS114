import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def binary_search(a, x):
    left = 0
    right = len(a) - 1
    mid = (left+right)//2
    while left <= right:
        if a[mid] == x:
            return mid
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left+right)//2
    if a[mid] < x:
        if mid == len(a) - 1:
            return mid
        u = x - a[mid]
        v = a[mid+1] - x
        if u < v:
            return mid
        return mid + 1
    else:
        if mid == 0:
            return mid
        u = a[mid] - x
        v = x - a[mid-1]
        if u < v:
            return mid
        return mid - 1
n = int(input())
a = list(map(int, input().split()))
while True:
    ip = list(map(int, input().split()))
    if len(ip) == 0:
        break
    t = binary_search(a, ip[1])
    truoc = t - 1
    sau = t + 1
    dem = 1
    while dem < ip[0]:
        if truoc < 0:
            print(a[0], a[ip[0]-1])
            break
        if sau > len(a) - 1:
            print(a[len(a) - ip[0]], a[len(a) - 1])
            break
        u = ip[1] - a[truoc]
        v = a[sau] - ip[1]
        if u <= v:
            truoc = truoc - 1
        else:
            sau = sau + 1
        dem = dem + 1
    if (truoc >= 0 and sau <= len(a) - 1) or dem == ip[0]:
        print(a[truoc+1], a[sau-1])