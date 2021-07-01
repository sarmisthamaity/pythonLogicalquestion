a=[[2,3,4],
    [34,56,67],
    [12,10,11]]
i=0
s=len(a)-1
sum2=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            sum=sum+a[i][j]
        if i==s:
            sum2=sum2+a[i][j]
        j=j+1
    
    i=i+1
print(sum)
print(sum2)

