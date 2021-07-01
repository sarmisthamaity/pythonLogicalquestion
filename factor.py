n=int(input("enter number: "))
fact=0
count=0
i=1
while i<=n:
	if n%i==0:
		count=count+1
		print (count)
	i=i+1
print ("fact: ",fact)
