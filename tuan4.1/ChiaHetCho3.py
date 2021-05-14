n = (input())
n = str(int(n))

# Tinh tong so cac chu so
Sum = 0 
for i in n:
    Sum+=int(i)
    
# Tim 1 chu so lam cho m lon nhat ma chia het cho 3 , khac m 
k = 0
KT = True
while k < len(n):
        
    if n[k]!='9': # nếu chữ số thứ k khác 9
        i = 9
        while i >= int(n[k])+1: #duyệt từ 9 đến chữ số đang xét cộng 1 
            Sum= Sum - int(n[k]) + i # tinh lai tong voi chu so i
            if Sum % 3 ==0: # nếu tổng các chữ số của nó chia hết cho 3 thì xuất ra đáp án
                print(n[:k]+str(i)+n[k+1:])
                KT = False
                exit()
            else : # ngược lại thì thì lại tổng các chữ số ban đầu
                Sum = Sum - i + int(n[k])
                i-=1 
        k+=1 # tìm đến chữ số tiếp theo
    else : k+=1 # tăng đến chữ số tiếp theo
        
# truong hop da duyet het 
if KT == True:
        KhoangCach = int(n) % 3
        x = n[0:len(n)-1]
        if KhoangCach == 0 :
            KhoangCach=3
        elif KhoangCach== 1:
            KhoangCach =1 
        else:
            KhoangCach = 2
        print( x+ str(int(n[-1])-KhoangCach))