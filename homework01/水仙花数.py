#水仙花数
n=int(input("输入一个三位数："))
if n<100 or n>1000:
     print("error input!!!!!!!!!")
else:
    i=n//100
    j=(n-100*i)//10
    k=n%10
    if i*i*i+j*j*j+k*k*k==n:
        print(n,end=' ')
        print("is a Daffodils")