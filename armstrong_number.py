for i in range (1000):
	num=i
	result=0
	n=len(str(num))
	while i!=0:
		digit=i%10
		result=result+digit**n
		i=i//10
	if num==result:
		print (num)


# ARMSTRONG NUMBER:
i=int(input("enter number: "))
real_n=i
sum=0
while i>0:
	r=i%10
	sum=sum+r**3
	i=i//10
if real_n==sum:
	print (real_n,"ARMSTRONG NUMBER")
else:
	print (real_n,"NOT ARMSTRONG NUMBER")

