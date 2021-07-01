sum = 0
average=0
n = 1
while n <= 11:
	weight = int(input("enter weight: "))
	sum = sum + weight
	n = n + 1
average= sum/n
print (sum)
print (average)
if average % 5 == 0:
	print ("5 se multiple hai")
else:
	print ("nahi hai")