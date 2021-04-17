def LamTron(x) :
    if x - int(x)== 0.0  : return int(x)
    x*=10000
    print(x)
    x= int(x) 
    print(x)
    k = x % 10 
    if ( k >=5 ) : 
        x/=10
        x+=1
    else : x/=10
    return int(x)/1000
 
# for i in range(14,100):
#     print( i / 13 )
#     print(LamTron(i/13))
#     print("{:0.4}".format(i/13))
#     print("-------")
print(LamTron(2.6675))
print(round(2.6675,3)) 