n=1
i=1
m=int(input("enter number: ")) 
while(n<=m):  
    j=1 
    ct=0
    while(j<=i):
        if(i%j==0):  
            ct=ct+1 
        j=j+1     
    if(ct==2): 
        print(i)
        n=n+1  
    i=i+1 