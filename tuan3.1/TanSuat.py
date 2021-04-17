# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
sys.stdin = open("InputTanSuat.txt","r")
sys.stdout = open("OutputTanSuat.txt","w")
t = int(input())
for i in range(t):
    n ,k = map(int,input().split())
    a = list(map(int,input().split()))
    TS = dict()
    for i in a:
        TS[i]=0
    for i in a :
        TS[i]+=1
    try :
        print(TS[k])
    except:
        print(0)
