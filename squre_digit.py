i=int(input("enter number: "))
sum=0
while i>0:
	r=i%10
	sum=sum+r**2
	i=i//10
print (sum)