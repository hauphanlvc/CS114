import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputWrapLine.txt","r")
#  input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdout = open("hau.txt","w")
String = input()
n = int(input())
ListCharacter = list(String.split())
i = 0 
j = 0
while i < len(String)-1 and j < len(ListCharacter)-1:
    Line =''
    while len(Line) <= n :
        if i < len(String): 
            if String[i]== " " and len(Line) !=0:
                Line+=' '
                i+=1
            else:
                if j < len(ListCharacter):
                    if len(Line) ==0 or (len(Line) + len(ListCharacter[j]) <= n): 
                        Line+=ListCharacter[j]
                        i+=len(ListCharacter[j])
                        j+=1
                    else : 
                        break
                else : 
                    break
                    
                        
    print(Line)                
