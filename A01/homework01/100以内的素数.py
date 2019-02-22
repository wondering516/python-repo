i=2
while i<100:
    k=2
    flag=0
    while k<i:
        if i%k==0:
            flag+=1
        k+=1
    if flag==0:
        print(i)
    i+=1