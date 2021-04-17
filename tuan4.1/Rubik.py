import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputRubik.txt","r")
sys.stdout = open("OutputRubik.txt","w")
Mau = list(map(str,input().split()))
ThuTu = list(map(str,input().split()))
ThuTu.reverse()
Result = list()
for i in Mau:
    x = list()
    for k in range(9):
        x.append(i)
    Result.append(x)
# print(Result)
for x in ThuTu:
    if x == "R":  
        a , b, c = 3,1,0
        
        Result[a][0], Result[b][4] , Result[c][8] = Result[c][8], Result[a][0] , Result[b][4]
    elif x == "U":
        a,b,c = 0,2,3
        Result[a][0], Result[b][4] , Result[c][8] = Result[c][8], Result[a][0] , Result[b][4]
    elif x == "L":
        a,b,c = 2,0,1
        
        Result[a][0], Result[b][4] , Result[c][8] = Result[c][8],Result[a][0],Result[b][4]

    elif x == "B":
        a,b,c = 1 , 3 , 2
        
        Result[a][0], Result[b][4] , Result[c][8] = Result[c][8], Result[a][0],Result[b][4]
        
    elif x == "U'":
        a,b,c = 0,2,3
        
        Result[a][0], Result[b][4] , Result[c][8] = Result[b][4], Result[c][8],Result[a][0]
    elif x == "L'":
        a,b,c = 2,0,1
    
        Result[a][0], Result[b][4] , Result[c][8] = Result[b][4], Result[c][8],Result[a][0]
    elif x == "B'":
        a,b,c = 1 , 3 , 2
        
        Result[a][0], Result[b][4] , Result[c][8] = Result[b][4], Result[c][8],Result[a][0]
    elif x == "R'":
        a,b,c = 3,1,0
        Result[a][0], Result[b][4] , Result[c][8] = Result[b][4], Result[c][8],Result[a][0]
        
    elif x == "r":
        a,b,c = 3,1,0
        Temp = Result[c][:]
        Result[c][3] = Result[b][6]
        Result[c][6:] = [Result[b][1] ,Result[b][5] ,Result[b][4]]
        Result[b][1] = Result[a][3]
        Result[b][4:7] = [Result[a][0],Result[a][2],Result[a][1]]
        Result[a][:4] = [Temp[8],Temp[3],Temp[7],Temp[6]]
        
    elif x == "u":
        a,b,c = 0,2,3
        Temp = Result[a][:]
        Result[0][0:4] = [Result[c][8],Result[c][3],Result[c][7],Result[c][6]]
        Temp_1 = Result[b][:]
        Result[b][1] = Temp[3]
        Result[b][4:7] = [Temp[0],Temp[2],Temp[1]]
        Result[c][3] = Temp_1[6]
        Result[c][6:] = [Temp_1[1],Temp_1[5],Temp_1[4]]

    elif x == "l":
        a,b,c = 2,0,1
        Temp = Result[c][:]
        Result[c][3] = Result[b][6]
        Result[c][6:] = [Result[b][1],Result[b][5],Result[b][4]]
        Result[b][1] = Result[a][3]
        Result[b][4:7] = [Result[a][0],Result[a][2],Result[a][1]]
        Result[a][:4] = [Temp[8],Temp[3],Temp[7],Temp[6]]
    elif x == "b":
        a,b,c = 1,3,2
        Temp = Result[c][:]
        Result[c][3] = Result[b][6]
        Result[c][6:] = [Result[b][1],Result[b][5], Result[b][4]]
        Result[b][1] = Result[a][3]
        Result[b][4:7] = [Result[a][0],Result[a][2],Result[a][1]]
        Result[a][:4] = [Temp[8],Temp[3],Temp[7],Temp[6]]
    elif x == "u'":
        a,b,c = 0,2,3
        Temp = Result[a][:]
        Result[a][:4] = [Result[b][4],Result[b][6],Result[b][5],Result[b][1]]
        Result[b][1] = Result[c][6]
        Result[b][4:7] = [Result[c][8],Result[c][7],Result[c][3]]
        Result[c][3] = Temp[1]
        Result[c][6:]= [Temp[3],Temp[2],Temp[0]]

    elif x == "l'":
        a,b,c = 2,0,1
        Temp = Result[a][:]
        Result[a][:4] = [Result[b][4],Result[b][6],Result[b][5],Result[b][1]]
        Result[b][1] = Result[c][6]
        Result[b][4:7] = [Result[c][8],Result[c][7],Result[c][3]]
        Result[c][3] = Temp[1]
        Result[c][6:]= [Temp[3],Temp[2],Temp[0]]
        
    elif x == "b'":
        a,b,c = 1,3,2
        Temp = Result[a][:]
        Result[a][:4] = [Result[b][4],Result[b][6],Result[b][5],Result[b][1]]
        Result[b][1] = Result[c][6]
        Result[b][4:7] = [Result[c][8],Result[c][7],Result[c][3]]
        Result[c][3] = Temp[1]
        Result[c][6:]= [Temp[3],Temp[2],Temp[0]]
    elif x == "r'":
        a,b,c = 3,1,0
        Temp = Result[a][:]
        Result[a][:4] = [Result[b][4],Result[b][6],Result[b][5],Result[b][1]]
        Result[b][1] = Result[c][6]
        Result[b][4:7] = [Result[c][8],Result[c][7],Result[c][3]]
        Result[c][3] = Temp[1]
        Result[c][6:]= [Temp[3],Temp[2],Temp[0]] 
#     for i in Result:
#         print(*i)
#     print("________________")     
# print("*********")
for i in Result:
    print(*i)
