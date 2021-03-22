import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputSoCoHau.txt","r")
sys.stdout = open("OutputSoCoHau.txt","w")
n , m = map(int,input().split())
if n > m : print(0)
elif n ==m : print(1)
else:
    x = len(str(n))
    m = str(m)
    n = str(n)
    if n == m[-len(n):]:
        print((int(m)-int(n))//10**len(n)+1)
    else:
        SoKhac = m[:-len(n)] + n
        if int(SoKhac) < int(m):
            print((int(m)-int(n))//10**len(n)+1)
        else :
            SoKhac = str(int(m[:-len(n)]) - 1 ) + n  
            print((int(SoKhac)-int(n))//10**len(n)+1)
            # print(SoKhac)