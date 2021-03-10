import io,os,sys
import random
sys.stdout = open("output.txt","w")
for i in range(0,10000000):
    x = random.randint(0,999)
    Dang = random.randint(0,5)
    if Dang ==0 :
        print(Dang,random.randint(0,999))
    elif Dang == 1:
        print(Dang,random.randint(0,999))
    elif Dang == 2:
        print(Dang,random.randint(0,999),random.randint(0,999))
    elif Dang == 3:
        print(Dang,random.randint(0,999))
    elif Dang == 4 :
        print(Dang,random.randint(0,999))
    elif Dang== 5 :
        print(Dang)
print("6")
