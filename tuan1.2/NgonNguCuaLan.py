def isLan(x):
    for i in x:
        if i[-2:]=='os' :
            if i[-4:]!='lios' : return False
        elif i[-2:]=='la':
            if i[-5:]!='liala' : return False
        elif i[-2:]=='tr':
            if i[-3:]!='etr': return False
        elif i[-2:]=='ra':
            if i[-4:]!='etra': return False
        elif i[-2:]=='is':
            if i[-6:]!='initis': return False
        elif i[-2:]=='es':
            if i[-6:]!='inites': return False    
        elif i[-2:]!='os' or i[-2:]!='la' or i[-2:]!='tr' or i[-2:]!='ra' or i[-2:]!='is' or i[-2:]!='es' : return False
        return True
def CheckNoun(x):
    Noun = ['tr','ra']
    if x[-2:] in Noun : return True
    return False
def CheckAdj(x):
    Adj = ['os','la'] 
    if x[-2:] in Adj : return True
    return False
def CheckVerb(x):
    Verb = ['is','es']
    if x[-2:] in Verb : return True
    return False
def CheckGT(x):
    Nam = ['os','tr','is']
    if x[-2:] in Nam : return True 
    return False
def Solve(x):
    # print(isLan(x))
    if isLan(x)==False: 
        print("NO")
        return
    if len(x)==1 and (CheckAdj(x[0]) or CheckNoun(x[0]) or CheckVerb(x[0])) : 
        print("YES")
        return
    index = -1    
    CountNoun = 0
    for i in range(0,len(x))  :
        if index==-1 :
            if CheckNoun(x[i])== True:
                index = i
                CountNoun +=1 
        elif CheckNoun(x[i]) : CountNoun+=1
    if CountNoun > 1 : 
        print("NO")
        return
    for i in range(0,index):
        if CheckAdj(x[i])== False : 
            print("NO")
            return
    for i in range(index+1,len(x)):
        if CheckVerb(x[i])== False : 
            print("NO")
            return

    for i in range(0,len(x)) :
        if CheckGT(x[i])!= CheckGT(x[0]) :
            print("NO")
            return
    print("YES")

x = list(map(str,input().split()))
Solve(x)
