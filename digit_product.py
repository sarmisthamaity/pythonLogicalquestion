num=int(input("enter number: "))
prd=1
while num>0:
	r=num%10
	prd=prd*r
	num=num//10
print (prd)
