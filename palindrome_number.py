n=int(input("enter number: "))
rev=0
org=n
while n>0:
	r=n%10
	rev=rev*10+r
	n=n//10
if rev==org:
	print ("PALINDROME NUMBER=",rev)
else:
	print ("NOT PALINDROME NUMBER")
