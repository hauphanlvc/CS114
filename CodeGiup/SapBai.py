import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputCard.txt","r")
sys.stdout = open("OuputCard.txt","w")
from bisect import bisect_left
def DoiSo(x):
   

    if x[0] in ['2','3','4','5','6','7','8','9'] :
        Res = int(x[0])
    elif x[0] == 'T':
        Res = 10
    elif x[0] == 'J':
        Res = 11
    elif x[0] == 'Q':
        Res = 12
    elif x[0] == 'K':
        Res = 13
    elif x[0] == 'T':
        Res = 14
    if x[1]== 'C':
        Res = int(str(Res)+'4')
    elif x[1] == 'B':
        Res = int(str(Res)+'3')
    elif x[1] == 'R':
        Res = int(str(Res)+'2')
    elif x[1] == 'N':
        Res = int(str(Res)+'1')
    return Res
testCase = int(input())
for k in range(testCase):
    n = int(input())
    Adam = list()
    for i in range(n):
        Adam.append(DoiSo(str(input())))
    Eva = list()
    for i in range(n):
        Eva.append(DoiSo(str(input())))
    Eva.sort()
    # Adam.sort()
    print(Adam)
    print(Eva)
    print("-------")
    Count = 0
    for x in Adam:
        i = bisect_left(Eva,x)
        if i != len(Eva):
            Count +=1
            Eva.remove(Eva[i])
    print(Count)
        