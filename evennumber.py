# FIRST 10 EVEN NUMBER:
n=int(input("enter number: "))
count=0
i=1
while i<100:
	if i%2==0:
		print ("even number",i)
		count=count+1
		if count==10:	
			print (count)
			break
	i=i+1

# FIRST 14 ODD NUMBER:
i=2
count=0
while i<100:
	if i%2!=0:
		print ("odd number",i)
		count=count+1
		if count==14:
			print (count)
			break
	i=i+1

