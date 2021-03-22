n = (input())
if int(n) < 10 :
    print(2)
else:
    # Sum = 1 + len(str(n))
    # x = dict()
    # for i in range(0,14):
    #     x[i] = 0
    # for i in range(2,n):
    #     if i % 10 == 0 :
    #         Sum+= len(str(i)) 
    #         # print(len(str(i)))
    #         x[len(str(i))] += 1
    # for i in range(0,14):
    #     if x[i] != 0 : 
    #         print(i,x[i])
    # print("-------\n{}".format(Sum))
    SoLuong = (((int(n) - 1)//10) * 10 - 10** (len(str(int(n)-1))-1))//10 + 1
    
    Sum1 = 1 + len(n)
    for i in range(2,len(n)):
        # print(i,i-2)
        Sum1 += i * 9 * (10 **(i-2 ))
        # print(i * 9 * (10 **(i-2 )))
    Sum1+= len(n)*SoLuong
    print(Sum1)