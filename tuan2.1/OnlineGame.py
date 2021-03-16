import io,os,sys
input=sys.stdin.readline
b = dict()
while True:
    try :
        a=list(map(int,input().split()))
        u = a[0]

        if u ==0 :
            break
        elif u==1:
            v = a[1]
            b[v] = 1     
                # inorder(root)
                # print("---------")
        elif u ==2 :
            v = a[1]
            try:
                
                sys.stdout.write(str(b[v]) + "\n")
                
            except:
                
                sys.stdout.write('0'+'\n')
        elif u == 3:
            v = a[1]
            try :
                del b[v]
            except:
                pass
                # inorder(root)
    except:
        pass