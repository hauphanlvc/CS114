def check(s,t):
    if s==t : return True

    for i in s:
        if i in t : return True
    return False
for _ in range(int(input())):
    s = str(input())
    t = str(input())
    if check(s,t): print("YES")
    else : print("NO")