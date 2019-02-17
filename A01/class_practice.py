
#100以内加法
num=1
sum=0
while num<=100 :
    sum+=num
    num+=1
print(sum)


print("="*50)
#1000以内回文数
i=1
while i<1000 :
    if i<10 :
        print(i)
    if i>10 and i<=99 :
        if i%11==0:
            print(i)
    if i>100 and i<999 :
        j=i // 100
        k=i % 10
        if j==k:
            print(i)
    i+=1

print("="*50)




