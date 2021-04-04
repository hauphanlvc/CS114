from bisect import bisect_left,bisect_right,bisect
import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
def solve(arr,k,x,n):
    res = list()
    index = bisect_left(arr,x)
    # print(n==len(arr))
    n = len(arr)
    if x <= arr[0]: 
        res =  arr[:k]
    elif x >= arr[-1]: 
        res =  arr[-k:]
    else :
        
        # print(index)
        right = index + 1
        left = index -1
        
        res.append(arr[index])

        k -= 1 
        while k > 0 :
            if 0<= left and right< n :
                if arr[right] - x < x - arr[left]:
                    res.append(arr[right])
                    right+=1
                else :
                    res.append(arr[left])
                    left-=1
            elif right >= n:
                res.append(arr[left])
                left-=1
            else :
                res.append(arr[right])
                right +=1
            k -= 1

    # print(res)
    print(min(res),max(res)) 
n = int(input())
a= list(map(int, input().split()))
while True:
    try :
        k , x = map(int,input().split())
        solve(a,k,x,n)

    except:
        exit()
# printKclosest(a,x,k,n)