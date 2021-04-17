def CheckTriangle(x,y,z):
    if x + y > z :
        if y + z > x :
            if x+ z > y:
                return True
    return False
def Check(x,y,z):
    if (x== y) and (y== z) : return 1 # tam giac deu 
    if (x== y) or (y==z) or (x==z) : return 0# tam giac can 
    if (x*x == y*y + z*z) or (y*y == x*x +z*z)  or (z*z == x*x + y*y) : return -1
    return 3 
def LamTron(x) :
    if x == int(x) : return int(x)
    x*=1000 
    k = x % 10 
    if ( k >=5 ) : 
        x/=10
        x+=1
    else : x/=10
    return int(x)/100   
def Result(x,y,z):
    if CheckTriangle(x,y,z) == False: 
        print("Khong phai tam giac")
        return  
    k = Check(x,y,z)
    Res = ''
    if (  k==1 ) : Res+="Tam giac deu, dien tich = "
    elif k== 0 : Res+="Tam giac can, dien tich = "
    elif k== -1 : Res+="Tam giac vuong, dien tich = "
    else: 
        Res+="Tam giac thuong, dien tich = "
    s = ( x + y + z )/ 2
    Area = sqrt(s*( s - x )*(s - y)*(s - z) )
    Area = LamTron(Area)
    if Area == int(Area): 
        print(Res+'{}'.format(int(Area)))
    else : 
        print(Res+'{}'.format(Area))
        
from math import sqrt
# x, y, z = map(float, input().split())
x = float(input())
y = float(input())
z = float(input())
Result(x,y,z)

