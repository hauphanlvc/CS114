def Solve(x):
    x = x.lower()
    NguyenAm= ['a','o','y','e','u','i']
    Res = ''
    for i in x:
        if i not in  NguyenAm : Res+='.'+i
        
    return Res

x = str(input())
print(Solve(x))


