n=int(input("enter number: "))
sum=0
prd=1
while n>0:
	r=n%10
	if r%2==0:
		sum=sum+r
	if r%2!=0:
		prd=prd*r
	n=n//10
print ("SUM OF EVEN NUMBER=",sum,"PRDOUCT OF ODD NUMBER=",prd)
