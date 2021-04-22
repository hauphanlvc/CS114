import io,os,sys
# # input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# sys.stdin = open("InputChia.txt","r")
sys.stdout = open("OuputChia.txt","w")
def Tinh(n):
    # n = (input())
    # n = str(int(n))
    n = str(n)
    Sum = 0 
    for i in n:
        Sum+=int(i)

    # return (int(n[0]))
    if n[0]!='9':
        i = 9
    # return (int(n[0]))
    # return (Sum)
        while i >= int(n[0])+1:
            Sum= Sum - int(n[0]) + i
            # return (Sum)
            if Sum % 3 ==0:
                # return (Sum)
                return (str(i)+n[1:])
                # exit()
                return
            else :
                Sum = Sum - i + int(n[0])
                i-=1 
        
    # return (Sum)
    New_Sum = Sum
    while New_Sum % 3 !=0:
        New_Sum+=1
    # return (New_Sum)
    KhoangCach = New_Sum - Sum
    # return (KhoangCach)
    k = 0
    KT = True
    # if KhoangCach ==0 : KhoangCach = 3
    while k < len(n):
            
        if n[k]!='9':
            i = 9
    # return (int(n[0]))
    # return (Sum)
            while i >= int(n[k])+1:
                Sum= Sum - int(n[k]) + i
            # return (Sum)
                if Sum % 3 ==0:
                    # return (Sum)
                    return (n[:k]+str(i)+n[k+1:])
                    KT = False
                    return 
                    # exit()
                else :
                    Sum = Sum - i + int(n[k])
                    i-=1 
            k+=1
        else : k+=1
            
        
    if KT == True:
            KhoangCach = 3 
            x = n[0:len(n)-1]
            
            return ( x+ str(9 - KhoangCach))
def SoSanh(x,k):
    x = str(x)
    k = str(k)
    Count = 0
    for i in range(len(x)):
        if x[i]!=k[i] : Count+=1
    if Count==1 : 
        return True
        # print("Đúng yeahhh")
    else : 
        return False
        # print("Sai rồi :((")

for x in range(100000000):
    
    k = Tinh(x)
    if SoSanh(x,k)== False :
        print(x,k)    
    
