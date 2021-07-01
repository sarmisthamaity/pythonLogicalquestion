def harshad_number(num):
	sum1=0
	while num>0:
		r=num//10
		sum1=sum1+r
		num=num//10
	print (sum1)
	if num%sum1==0:
		return (True)
	else:
		print (False)

int1=int(input("enter number: "))

print(harshad_number(int1))


