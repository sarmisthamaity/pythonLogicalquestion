def strangenumber(N):
    i=0
    lis=[]
    count=0
    while i<=100:
        j=i
        sum=0
        while j>0:
            rem=j%10
            sum=sum+rem
            j=j//10
        if sum%9==0:
            count+=1
            lis.append(i)
            if count==N:
                print(i)
                break    
        i=i+1
    print(lis)
N=int(input("enter number: "))
strangenumber(N)
