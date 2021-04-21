import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputWrapLine.txt","r")
sys.stdout = open("hau.txt","w")
String = input()
n = int(input())
New_String = String
i = 0
from collections import deque
KhoangTrang = deque()

while i < len(String)-1:
    if String[i]!=" " and String[i+1]==" " :
        j = i+1
        while String[j] == " ":
            if String[j+1] != " ":
                break
            j+=1
        KhoangTrang.append(String[i+1:j+1])
        i = j + 1 
    elif String[i] ==" ":
        j = i
        while String[j] == " ":
            if String[j+1] != " ":
                break
            j+=1
        KhoangTrang.append(String[i:j+1])
        i = j + 1
    else: 
        i+=1
ListCharacter = list(String.split())
# print(KhoangTrang)
# for i in ListCharacter:
#     print(i)
if String[0]!=" ":
    i = 0 
    # print(KhoangTrang.popleft(),end='')
    while i < len(ListCharacter):
        if len(ListCharacter[i])> n :
            print(KhoangTrang.popleft() + ListCharacter[i])
            i+=1
        else :
            DoDaiLine = len(ListCharacter[i])
            Line = ListCharacter[i]
            Index = i 
            for j in range(i+1,len(ListCharacter)):
                x = KhoangTrang.popleft()
                
                DoDaiLine += len(ListCharacter[j]) + len(x) 
                if DoDaiLine > n :
                    break
                else :
                    Line += x + ListCharacter[j]
                    Index = j 
            print(Line)
            i = Index + 1
else :
    i = 0 
    # print(KhoangTrang.popleft(),end='')
    while i < len(ListCharacter):
        if len(ListCharacter[i])> n :
            print(KhoangTrang.popleft() + ListCharacter[i])
            i+=1
        else :
            DoDaiLine = len(ListCharacter[i])
            Line = ListCharacter[i]
            Index = i 
            for j in range(i+1,len(ListCharacter)):
                x = KhoangTrang.popleft()
                
                DoDaiLine += len(ListCharacter[j]) + len(x) 
                if DoDaiLine > n :
                    break
                else :
                    Line += x + ListCharacter[j]
                    Index = j 
            print(Line)
            i = Index + 1

