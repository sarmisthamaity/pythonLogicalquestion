i=int(input("enter number: "))
count=0
n=1
while n<=i:
	if i%n==0:
		count=count+1
	n=n+1
if count==2:
	print ("prime number")
else:
	print ("composite number")


