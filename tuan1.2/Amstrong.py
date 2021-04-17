def Check(x):
    k = len(x)
    S = 0 
    for i in x :
        S += int(i)**k
        if S > int(x) : return False
    if S== int(x) : return True

x = str(input())
if Check(x): print("True")
else : print("False")